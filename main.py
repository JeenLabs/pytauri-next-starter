"""PyTauri Barebones App."""

import sys
from os import environ
from pathlib import Path

from anyio import create_task_group
from anyio.abc import TaskGroup
from anyio.from_thread import start_blocking_portal
from pydantic import BaseModel, ConfigDict
from pydantic.alias_generators import to_camel
from pytauri import Commands
from pytauri.webview import WebviewWindow
from pytauri_plugins import opener
from pytauri_wheel.lib import builder_factory, context_factory

# Configuration
BACKEND_DIR = Path(__file__).parent.absolute()
DEV_MODE = environ.get("PYTAURI_NEXTJS_DEV") == "1"

commands = Commands()


# === Pydantic Models ===

class _BaseModel(BaseModel):
    """Base model that accepts camelCase from JS and snake_case from Python."""

    model_config = ConfigDict(
        alias_generator=to_camel,
        populate_by_name=True,
    )


class GreetRequest(_BaseModel):
    """Greet request model."""
    name: str


# === Commands ===

@commands.command()
async def greet(body: GreetRequest, webview_window: WebviewWindow) -> str:
    """Greet a user with a personalized message."""
    #webview_window.set_title(f"Hello {body.name}!")
    return f"Hello, {body.name}! Welcome to PyTauri Next.js Starter."


# === App Setup ===

task_group: TaskGroup


def main() -> int:
    """Run the Tauri app."""
    global task_group

    with (
        start_blocking_portal("asyncio") as portal,
        portal.wrap_async_context_manager(
            portal.call(create_task_group)
        ) as task_group,
    ):
        if DEV_MODE:
            tauri_config = {
                "build": {"frontendDist": "http://localhost:3000"},
            }
        else:
            tauri_config = None

        app = builder_factory().build(
            context=context_factory(BACKEND_DIR, tauri_config=tauri_config),
            invoke_handler=commands.generate_handler(portal),
            plugins=(opener.init(),),
        )
        return app.run_return()


if __name__ == "__main__":
    sys.exit(main())
