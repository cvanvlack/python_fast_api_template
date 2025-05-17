# Python FastAPI Template

A modern FastAPI project template with type checking, testing, and development tools pre-configured.

## Requirements

- Python 3.12.2 (as specified in `.python-version`)
- [uv](https://github.com/astral-sh/uv) - Fast Python package installer and resolver

## Getting Started

1. **Install uv** (if you haven't already):
   ```bash
   curl -LsSf https://astral.sh/uv/install.sh | sh
   ```

2. **Create and activate a virtual environment**:
   ```bash
   uv venv
   source .venv/bin/activate  # On Unix/macOS
   # or
   .venv\Scripts\activate  # On Windows
   ```

3. **Install dependencies**:
   ```bash
   uv pip install -e .
   ```

4. **Install development dependencies**:
   ```bash
   uv pip install -e ".[dev]"
   ```

## Development

The project uses several development tools that are pre-configured:

- **Black**: Code formatting
- **Ruff**: Fast Python linter
- **MyPy**: Static type checking
- **Pytest**: Testing framework with coverage reporting
- **pre-commit**: Git hooks for code quality

### Setting up pre-commit hooks

1. **Install pre-commit**:
   ```bash
   uv pip install pre-commit
   ```

2. **Install the pre-commit hooks**:
   ```bash
   pre-commit install
   ```

The following pre-commit hooks are configured:
- **Black** (v24.2.0): Automatic code formatting
- **Ruff** (v0.3.2): Fast Python linter with auto-fix capability
- **MyPy** (v1.15.0): Static type checking with strict mode

You can manually run the pre-commit hooks on all files:
```bash
pre-commit run --all-files
```

### Running Tests

```bash
pytest
```

### Type Checking

```bash
mypy app
```

### Code Formatting

```bash
black .
```

### Linting

```bash
ruff check .
```
