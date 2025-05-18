import uuid
from typing import Dict, List

from app.core.exceptions.todo_exceptions import TodoNotFoundError
from app.models.todo import TodoCreate, TodoResponse


class TodoService:
    """
    Service for managing Todo items with in-memory storage.
    """

    def __init__(self) -> None:
        """Initialize an empty in-memory storage for todos."""
        self.todos: Dict[str, TodoResponse] = {}

    def create_todo(self, todo_in: TodoCreate) -> TodoResponse:
        """
        Create a new todo.

        Args:
            todo_in: The todo data to create

        Returns:
            TodoResponse: The created todo
        """
        todo_id = str(uuid.uuid4())
        todo = TodoResponse(id=todo_id, **todo_in.model_dump())
        self.todos[todo_id] = todo
        return todo

    def get_todo(self, todo_id: str) -> TodoResponse:
        """
        Get a todo by ID.

        Args:
            todo_id: The ID of the todo to retrieve

        Returns:
            TodoResponse: The requested todo

        Raises:
            TodoNotFoundError: If the todo is not found
        """
        todo = self.todos.get(todo_id)
        if todo is None:
            raise TodoNotFoundError(todo_id)
        return todo

    def get_todos(self) -> List[TodoResponse]:
        """
        Get all todos.

        Returns:
            List[TodoResponse]: List of all todos
        """
        return list(self.todos.values())

    def update_todo(self, todo_id: str, todo_in: TodoCreate) -> TodoResponse:
        """
        Update a todo.

        Args:
            todo_id: The ID of the todo to update
            todo_in: The updated todo data

        Returns:
            TodoResponse: The updated todo

        Raises:
            TodoNotFoundError: If the todo is not found
        """
        if todo_id not in self.todos:
            raise TodoNotFoundError(todo_id)

        todo = TodoResponse(id=todo_id, **todo_in.model_dump())
        self.todos[todo_id] = todo
        return todo

    def delete_todo(self, todo_id: str) -> None:
        """
        Delete a todo.

        Args:
            todo_id: The ID of the todo to delete

        Raises:
            TodoNotFoundError: If the todo is not found
        """
        if todo_id not in self.todos:
            raise TodoNotFoundError(todo_id)

        del self.todos[todo_id]


# Singleton instance of TodoService
_todo_service: TodoService | None = None


def get_todo_service() -> TodoService:
    """
    Get or create the TodoService singleton.

    Returns:
        TodoService: The TodoService instance
    """
    global _todo_service
    if _todo_service is None:
        _todo_service = TodoService()
    return _todo_service
