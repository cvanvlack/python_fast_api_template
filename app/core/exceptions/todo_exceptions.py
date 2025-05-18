class TodoException(Exception):
    """Base exception for Todo-related errors."""

    pass


class TodoNotFoundError(TodoException):
    """Exception raised when a todo item is not found."""

    def __init__(self, todo_id: str) -> None:
        self.todo_id = todo_id
        self.message = f"Todo with ID {todo_id} not found"
        super().__init__(self.message)


class TodoValidationError(TodoException):
    """Exception raised when todo data validation fails."""

    def __init__(self, message: str) -> None:
        self.message = message
        super().__init__(self.message)
