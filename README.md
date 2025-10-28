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
### 5. Run NextJS frontend

```bash
pnpm dev
#or
npm run dev
# or
yarn dev
# or
bun dev
```
Open [http://localhost:3000](http://localhost:3000) with your browser to see the result.

You can start editing the page by modifying `app/page.tsx`. The page auto-updates as you edit the file.

### 6. Run Application

Run backend python application:

```bash
python -m main
#or
python main.py
```
---