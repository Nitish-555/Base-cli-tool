# Review Checker

Python CLI tool to verify NeatCode backend review quality and accuracy.

## Setup

```bash
# Install with uv (creates venv automatically)
uv sync

# Or install dependencies directly
uv pip install -r requirements.txt
```

## Usage

```bash
# Check backend health
python cli.py health

# Check features (placeholder for now)
python cli.py check --installation-id 999 --owner test-org --repo test-repo
```

## Configuration

Set environment variable:
```bash
export NEATCODE_BACKEND_URL=http://localhost:3000
```

## Current Features

- ✅ Backend health check
- ⏳ Knowledge graph verification (to be added)
- ⏳ Code embeddings verification (to be added)
- ⏳ Grep search verification (to be added)

