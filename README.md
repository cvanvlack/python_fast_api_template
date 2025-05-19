# Python FastAPI Template

A modern FastAPI project template with type checking, testing, and development tools pre-configured. This template implements a simple Todo API with in-memory storage.

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
   .\.venv\bin\activate.ps1  # On Windows
   ```

3. **Install dependencies**:
   ```bash
   uv pip install -e .
   ```

4. **Install development dependencies**:
   ```bash
   uv pip install -e ".[dev]"
   ```

5. **Run the application**:
   ```bash
   uvicorn app.main:app --reload
   ```

   The API will be available at http://localhost:8000.

## API Documentation

Once the server is running, you can access the auto-generated API documentation:

- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## API Endpoints

The template implements a RESTful Todo API with the following endpoints:

### Get All Todos

```
GET /api/todos/
```

Returns a list of all todos.

**Response Example:**
```json
[
  {
    "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
    "title": "Buy groceries",
    "description": "Need to buy milk, eggs, and bread",
    "done": false
  }
]
```

### Get a Todo by ID

```
GET /api/todos/{todo_id}
```

Returns a specific todo by ID.

**Response Example:**
```json
{
  "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
  "title": "Buy groceries",
  "description": "Need to buy milk, eggs, and bread",
  "done": false
}
```

### Create a Todo

```
POST /api/todos/
```

Creates a new todo.

**Request Body Example:**
```json
{
  "title": "Study FastAPI",
  "description": "Complete FastAPI tutorial by weekend",
  "done": false
}
```

**Response Example:**
```json
{
  "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
  "title": "Study FastAPI",
  "description": "Complete FastAPI tutorial by weekend",
  "done": false
}
```

### Update a Todo

```
PUT /api/todos/{todo_id}
```

Updates an existing todo.

**Request Body Example:**
```json
{
  "title": "Study FastAPI",
  "description": "Complete FastAPI tutorial by weekend",
  "done": true
}
```

**Response Example:**
```json
{
  "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
  "title": "Study FastAPI",
  "description": "Complete FastAPI tutorial by weekend",
  "done": true
}
```

### Delete a Todo

```
DELETE /api/todos/{todo_id}
```

Deletes a todo by ID.

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

## Project Structure

The project follows a modular structure with clear separation of concerns:

```
/
├── app/
│   ├── __init__.py
│   ├── main.py              # FastAPI application initialization
│   ├── api/
│   │   ├── __init__.py
│   │   └── routes/
│   │       ├── __init__.py
│   │       └── todos.py     # Todo endpoints
│   ├── core/
│   │   ├── __init__.py
│   │   ├── config.py        # App configuration
│   │   └── exceptions/      # Custom exception handling
│   ├── models/
│   │   ├── __init__.py
│   │   └── todo.py          # Todo Pydantic models
│   └── services/
│       ├── __init__.py
│       └── todo.py          # Todo business logic and storage
├── tests/
│   ├── __init__.py
│   ├── conftest.py          # Test fixtures
│   ├── test_api/
│   │   ├── __init__.py
│   │   └── test_todos.py    # API endpoint tests
│   └── test_services/
│       ├── __init__.py
│       ├── test_todo.py     # Service layer tests
│       └── test_todo_exceptions.py # Exception tests
├── .env.example             # Example environment variables
├── .pre-commit-config.yaml  # Pre-commit hooks configuration
├── pyproject.toml           # Project dependencies and configuration
└── README.md                # Project documentation
```
