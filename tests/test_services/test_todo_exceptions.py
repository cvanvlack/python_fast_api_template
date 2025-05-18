import pytest

from app.core.exceptions.todo_exceptions import TodoNotFoundError
from app.models.todo import TodoCreate
from app.services.todo import TodoService


class TestTodoServiceExceptions:
    """Tests for the TodoService class exception handling."""

    @pytest.fixture
    def todo_service(self) -> TodoService:
        """Return a fresh TodoService instance for each test."""
        return TodoService()

    def test_get_todo_raises_exception_when_not_found(
        self, todo_service: TodoService
    ) -> None:
        """Test that get_todo raises TodoNotFoundError when the todo is not found."""
        # Act/Assert
        with pytest.raises(TodoNotFoundError) as exc_info:
            todo_service.get_todo("nonexistent-id")

        assert "nonexistent-id" in str(exc_info.value)
        assert exc_info.value.todo_id == "nonexistent-id"

    def test_update_todo_raises_exception_when_not_found(
        self, todo_service: TodoService
    ) -> None:
        """Test that update_todo raises TodoNotFoundError when the todo is not found."""
        # Arrange
        update_data = TodoCreate(title="Updated Title")

        # Act/Assert
        with pytest.raises(TodoNotFoundError) as exc_info:
            todo_service.update_todo("nonexistent-id", update_data)

        assert "nonexistent-id" in str(exc_info.value)
        assert exc_info.value.todo_id == "nonexistent-id"

    def test_delete_todo_raises_exception_when_not_found(
        self, todo_service: TodoService
    ) -> None:
        """Test that delete_todo raises TodoNotFoundError when the todo is not found."""
        # Act/Assert
        with pytest.raises(TodoNotFoundError) as exc_info:
            todo_service.delete_todo("nonexistent-id")

        assert "nonexistent-id" in str(exc_info.value)
        assert exc_info.value.todo_id == "nonexistent-id"
