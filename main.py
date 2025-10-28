"""PyTauri Barebones App."""

import sys
from os import environ
from pathlib import Path

from pytauri_wheel.lib import builder_factory, context_factory

# Configuration
BACKEND_DIR = Path(__file__).parent.absolute()
DEV_MODE = environ.get("PYTAURI_NEXTJS_DEV") == "1"


def main() -> int:
    """Run the minimal Tauri app."""
    if DEV_MODE:
        tauri_config = {
            "build": {"frontendDist": "http://localhost:3000"},
        }
    else:
        tauri_config = None

    app = builder_factory().build(
        context=context_factory(BACKEND_DIR, tauri_config=tauri_config),
        invoke_handler=None,
    )
    return app.run_return()


if __name__ == "__main__":
    sys.exit(main())
