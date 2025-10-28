# pytauri-next-starter

Cross-platform desktop application starter built with Pytauri, Next.js (TypeScript), and Python Wheel — combining modern web UIs with powerful Python backends.

---

## 🛠️ Project Initialization Guide

Follow these steps to set up the project after cloning the repository.

---

### 1. Clone the Repository

```bash
git clone https://github.com/JeenLabs/pytauri-next-starter.git
cd pytauri-next-starter
```

### 2. Set Up Python Environment (Backend)

Make sure you have [uv](https://github.com/astral-sh/uv) installed.

If not, install it:

```bash
pip install uv
```

Then create and activate a virtual environment:

```bash
uv venv .venv
```

Activate it:

* **macOS/Linux** :
  ```bash
  source .venv/bin/activate
  ```
* **Windows (PowerShell)** :
  ```bash
  .venv\Scripts\Activate.ps1
  ```

### 3. Install Python Dependencies

Install all project dependencies declared in `pyproject.toml`:

```bash
uv sync
```

### 4. Install NextJS dependencies

Install all nextjs dependencies declared in `package.json`:

```bash
pnpm install
```

### 5. Run Application

**For Development Mode (with hot reload):**
1. First, start the Next.js development server:
   ```bash
   pnpm dev
   ```
2. Then, in a separate terminal, run the Python app with development mode:

   **Windows PowerShell:**
   ```powershell
   $env:PYTAURI_NEXTJS_DEV="1"; python main.py
   ```

   **Windows Command Prompt:**
   ```cmd
   set PYTAURI_NEXTJS_DEV=1 && python main.py
   ```

   **macOS/Linux:**
   ```bash
   PYTAURI_NEXTJS_DEV=1 python main.py
   ```

**For Production Mode:**
1. Build the Next.js frontend:
   ```bash
   pnpm build
   ```
2. Run the Python app:
   ```bash
   python main.py
   ```
---