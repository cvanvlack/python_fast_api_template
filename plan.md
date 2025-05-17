# FastAPI Todo API - TDD Project Plan

## Project Overview

This project involves building a Todo API using FastAPI with a focus on Test-Driven Development (TDD). The API will provide CRUD operations for todo items with in-memory storage. The implementation follows best practices for Python development, including type checking, linting, and comprehensive testing.

## Implementation Strategy

We'll follow a bottom-up TDD approach, starting with the core data models and services before building the API endpoints. This ensures that our business logic is solid before exposing it through HTTP endpoints.

## Development Steps

### Phase 1: Project Setup and Configuration
1. Create basic project structure
2. Set up configuration for development tools
3. Configure testing environment

### Phase 2: Todo Model and Service Layer Implementation
1. Define Todo Pydantic models
2. Implement Todo service with in-memory storage
3. Write comprehensive tests for service layer

### Phase 3: API Routes Implementation
1. Implement API endpoints for CRUD operations
2. Write API integration tests
3. Configure API application with proper error handling

### Phase 4: Documentation and Refinement
1. Add API documentation
2. Refine error handling
3. Add example environment configuration

## Detailed Implementation Plan

### Step 1: Project Structure Setup
- Create necessary directories and files according to project specification
- Implement basic application configuration

### Step 2: Todo Model Implementation
- Define Todo Pydantic models
- Create base model, creation model, and response model with proper validation

### Step 3: Todo Service Layer
- Implement in-memory storage for todos
- Create CRUD operations in the service layer
- Write unit tests for the service layer

### Step 4: API Endpoints Implementation
- Create router for todo endpoints
- Implement CRUD endpoints with proper status codes and error handling
- Write integration tests for API endpoints

### Step 5: Main Application Setup
- Configure the main FastAPI application
- Set up proper dependency injection
- Add middleware and error handling

### Step 6: Documentation and Final Testing
- Add API documentation
- Perform final testing
- Add usage examples in README

## TDD Implementation Prompts

Below are the step-by-step prompts for implementing this project following TDD principles.

```
## Prompt 1: Project Structure Setup

Create the basic project structure as specified in the requirements. This includes:

1. Set up the directory structure with all required files and folders
2. Create empty __init__.py files in each directory to make them proper Python packages
3. Set up the basic config.py file to load environment variables using python-dotenv
4. Create a .pre-commit-config.yaml file with the required hooks
5. Create a .env.example file with placeholder variables

Don't implement any functionality yet, just set up the structure so we can build incrementally.
```

```
## Prompt 2: Todo Model Implementation

Implement the Todo Pydantic models in app/models/todo.py:

1. Create a TodoBase model with title, description, and done fields
2. Create a TodoCreate model that inherits from TodoBase
3. Create a TodoResponse model that inherits from TodoBase and adds an id field
4. Add proper type hints and validations as follows:
   - id: Unique identifier (UUID or integer)
   - title: String with character limits
   - description: Optional string
   - done: Boolean with default value of False

Write tests in tests/test_models/test_todo.py to verify model validation and conversion.
```

```
## Prompt 3: Todo Service Implementation - Part 1

Implement the foundation of the Todo service in app/services/todo.py:

1. Create a TodoService class with an in-memory storage (a dictionary or list)
2. Implement the create_todo method that adds a new todo to storage
3. Implement the get_todo method that retrieves a todo by ID
4. Use proper type hints throughout

Write tests in tests/test_services/test_todo.py to verify:
- A todo can be created with valid data
- A todo can be retrieved by ID
- Appropriate errors are raised when a todo doesn't exist
```

```
## Prompt 4: Todo Service Implementation - Part 2

Extend the TodoService class in app/services/todo.py:

1. Implement get_todos method to list all todos
2. Implement update_todo method to update an existing todo
3. Implement delete_todo method to remove a todo

Add tests in tests/test_services/test_todo.py to verify:
- All todos can be retrieved
- A todo can be updated with new data
- A todo can be deleted
- Appropriate errors are raised for invalid operations
```

```
## Prompt 5: API Routes Implementation - Part 1

Implement the Todo API endpoints in app/api/routes/todos.py:

1. Create a router with the prefix /todos
2. Implement GET /todos/{todo_id} endpoint to get a specific todo
3. Implement GET /todos/ endpoint to list all todos
4. Use dependency injection to get the TodoService instance
5. Ensure proper error handling and status codes (404 when not found)

Write tests in tests/test_api/test_todos.py to verify:
- A specific todo can be retrieved via API
- All todos can be listed via API
- Proper error response is returned when a todo doesn't exist
```

```
## Prompt 6: API Routes Implementation - Part 2

Complete the Todo API endpoints in app/api/routes/todos.py:

1. Implement POST /todos/ endpoint to create a new todo
2. Implement PUT /todos/{todo_id} endpoint to update a todo
3. Implement DELETE /todos/{todo_id} endpoint to delete a todo
4. Ensure proper request validation and response models
5. Return appropriate status codes (201 for creation, 204 for deletion)

Add tests in tests/test_api/test_todos.py to verify:
- A todo can be created via API
- A todo can be updated via API
- A todo can be deleted via API
- Invalid requests are handled correctly
```

```
## Prompt 7: Main Application Setup

Set up the main FastAPI application in app/main.py:

1. Create a FastAPI instance with proper metadata
2. Include the todos router
3. Set up middleware if needed
4. Configure CORS if needed
5. Create a function to get the application instance (for testing purposes)

Write tests in tests/test_app.py to verify:
- The application starts correctly
- The correct routes are registered
- The API documentation is accessible
```

```
## Prompt 8: Error Handling and Validation

Enhance error handling and validation:

1. Create custom exception classes in app/core/exceptions.py
2. Implement exception handlers in app/core/handlers.py
3. Register exception handlers in main.py
4. Update service methods to use custom exceptions
5. Ensure consistent error responses across the API

Add tests to verify:
- Custom exceptions are raised correctly
- Exception handlers return appropriate responses
- Validation errors are handled consistently
```

```
## Prompt 9: API Documentation

Enhance API documentation and usability:

1. Add detailed docstrings to API endpoints
2. Configure OpenAPI details in the FastAPI app
3. Add example requests and responses
4. Create a startup script or instructions to run the application
5. Update README.md with usage examples and API documentation

Test the OpenAPI documentation at /docs endpoint to ensure it's complete and accurate.
```

```
## Prompt 10: Final Testing and Refinement

Complete the implementation with final touches:

1. Perform end-to-end testing to ensure all components work together
2. Verify that all tests pass and have good coverage
3. Ensure all files have proper type hints and pass mypy check
4. Ensure code passes black and ruff checks
5. Update README.md with complete setup and usage instructions

Apply any refinements or bug fixes identified during testing.
```

## Development Workflow

For each step in this TDD process:

1. Write tests first that define the expected behavior
2. Implement the minimum code required to pass those tests
3. Refactor the code to improve design while ensuring tests continue to pass
4. Move to the next feature once current implementation is solid

This approach ensures each component is thoroughly tested and that the project grows incrementally with a solid foundation.