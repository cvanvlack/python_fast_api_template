from fastapi import APIRouter, Depends, status

from app.models.todo import TodoCreate, TodoResponse
from app.services.todo import TodoService, get_todo_service

# We no longer need to import HTTPException as we're using custom exceptions

router = APIRouter(prefix="/todos", tags=["todos"])


@router.get("/{todo_id}", response_model=TodoResponse)
async def get_todo(
    todo_id: str, todo_service: TodoService = Depends(get_todo_service)
) -> TodoResponse:
    """
    Get a todo by ID.

    Args:
        todo_id: The ID of the todo to retrieve
        todo_service: The todo service for interacting with todos

    Returns:
        TodoResponse: The requested todo

    Raises:
        TodoNotFoundError: If the todo is not found
    """
    return todo_service.get_todo(todo_id)


@router.get("/", response_model=list[TodoResponse])
async def get_todos(
    todo_service: TodoService = Depends(get_todo_service),
) -> list[TodoResponse]:
    """
    Get all todos.

    Args:
        todo_service: The todo service for interacting with todos

    Returns:
        list[TodoResponse]: List of all todos
    """
    return todo_service.get_todos()


@router.post("/", response_model=TodoResponse, status_code=status.HTTP_201_CREATED)
async def create_todo(
    todo_in: TodoCreate, todo_service: TodoService = Depends(get_todo_service)
) -> TodoResponse:
    """
    Create a new todo.

    Args:
        todo_in: The todo data to create
        todo_service: The todo service for interacting with todos

    Returns:
        TodoResponse: The created todo
    """
    return todo_service.create_todo(todo_in)


@router.put("/{todo_id}", response_model=TodoResponse)
async def update_todo(
    todo_id: str,
    todo_in: TodoCreate,
    todo_service: TodoService = Depends(get_todo_service),
) -> TodoResponse:
    """
    Update a todo.

    Args:
        todo_id: The ID of the todo to update
        todo_in: The updated todo data
        todo_service: The todo service for interacting with todos

    Returns:
        TodoResponse: The updated todo

    Raises:
        TodoNotFoundError: If the todo is not found
    """
    return todo_service.update_todo(todo_id, todo_in)


@router.delete("/{todo_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_todo(
    todo_id: str, todo_service: TodoService = Depends(get_todo_service)
) -> None:
    """
    Delete a todo.

    Args:
        todo_id: The ID of the todo to delete
        todo_service: The todo service for interacting with todos

    Raises:
        TodoNotFoundError: If the todo is not found
    """
    todo_service.delete_todo(todo_id)
