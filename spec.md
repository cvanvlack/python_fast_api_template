# FastAPI Backend Template Specification

## Overview
A template backend web service using FastAPI to demonstrate best practices for new developers. The template implements a simple Todo API with in-memory storage.

## Tech Stack
- FastAPI
- Pydantic for data validation and type hints
- Black for code formatting
- Ruff for linting
- Mypy for type checking
- Pre-commit hooks for code quality checks
- Pytest for testing
- Python-dotenv for environment variable management

## Todo Data Model
- `id`: Unique identifier
- `title`: Title of the todo item
- `description`: Detailed description of the todo item
- `done`: Boolean indicating if the todo is complete (open/done status)

## API Endpoints

### GET /todos/{todo_id}
- Retrieves a specific todo by ID
- Returns 404 if todo not found

### GET /todos/
- Lists all todos
- Optional query parameters for filtering

### POST /todos/
- Creates a new todo
- Validates request body using Pydantic model

### PUT /todos/{todo_id}
- Updates an existing todo
- Can mark a todo as done
- Returns 404 if todo not found

### DELETE /todos/{todo_id}
- Deletes a todo by ID
- Returns 404 if todo not found

## Project Structure
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
│   │   └── config.py        # App configuration
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
│       └── test_todo.py     # Service layer tests
├── .env.example             # Example environment variables
├── .pre-commit-config.yaml  # Pre-commit hooks configuration
├── pyproject.toml           # Project dependencies and configuration
└── README.md                # Project documentation
```

## Development Environment Setup
1. Python 3.10+ recommended
2. Virtual environment creation
3. Install dependencies: `pip install -e ".[dev]"`
4. Install pre-commit hooks: `pre-commit install`

## Code Quality Tools
- **Black**: Auto-formatting code to a consistent style
- **Ruff**: Fast Python linter
- **Mypy**: Static type checking
- **Pre-commit**: Runs checks before each commit
  - Includes black, ruff, mypy, and pytest

## Testing Strategy
- Unit tests for services
- Integration tests for API endpoints
- Test fixtures for reusable components
- Use pytest for test running

## Documentation
- OpenAPI/Swagger documentation auto-generated by FastAPI
- Accessible at `/docs` endpoint
- Example requests and responses included

## Future Enhancements (Not Implemented in Initial Version)
- Authentication and authorization
- Database integration
- Containerization with Docker
- CI/CD configuration
- Logging configuration
