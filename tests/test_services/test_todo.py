import pytest

from app.core.exceptions.todo_exceptions import TodoNotFoundError
from app.models.todo import TodoCreate
from app.services.todo import TodoService


class TestTodoService:
    """Tests for the TodoService class."""

    @pytest.fixture
    def todo_service(self) -> TodoService:
        """Return a fresh TodoService instance for each test."""
        return TodoService()

    def test_create_todo(self, todo_service: TodoService) -> None:
        """Test creating a new todo."""
        # Arrange
        todo_in = TodoCreate(title="Test Todo")

        # Act
        created_todo = todo_service.create_todo(todo_in)

        # Assert
        assert created_todo.id is not None
        assert created_todo.title == "Test Todo"
        assert created_todo.description == ""
        assert created_todo.done is False

    def test_get_todo_existing(self, todo_service: TodoService) -> None:
        """Test getting an existing todo by ID."""
        # Arrange
        todo_in = TodoCreate(title="Test Todo")
        created_todo = todo_service.create_todo(todo_in)

        # Act
        retrieved_todo = todo_service.get_todo(created_todo.id)

        # Assert
        assert retrieved_todo is not None
        assert retrieved_todo.id == created_todo.id
        assert retrieved_todo.title == created_todo.title

    def test_get_todo_nonexistent(self, todo_service: TodoService) -> None:
        """Test getting a nonexistent todo by ID."""
        # Act & Assert
        with pytest.raises(TodoNotFoundError):
            todo_service.get_todo("nonexistent-id")

    def test_get_todos_empty(self, todo_service: TodoService) -> None:
        """Test getting all todos when none exist."""
        # Act
        todos = todo_service.get_todos()

        # Assert
        assert isinstance(todos, list)
        assert len(todos) == 0

    def test_get_todos_multiple(self, todo_service: TodoService) -> None:
        """Test getting all todos when multiple exist."""
        # Arrange
        todo_service.create_todo(TodoCreate(title="Todo 1"))
        todo_service.create_todo(TodoCreate(title="Todo 2"))
        todo_service.create_todo(TodoCreate(title="Todo 3"))

        # Act
        todos = todo_service.get_todos()

        # Assert
        assert isinstance(todos, list)
        assert len(todos) == 3
        assert {todo.title for todo in todos} == {"Todo 1", "Todo 2", "Todo 3"}

    def test_update_todo_existing(self, todo_service: TodoService) -> None:
        """Test updating an existing todo."""
        # Arrange
        created_todo = todo_service.create_todo(TodoCreate(title="Original Title"))
        update_data = TodoCreate(
            title="Updated Title", description="New description", done=True
        )

        # Act
        updated_todo = todo_service.update_todo(created_todo.id, update_data)

        # Assert
        assert updated_todo is not None
        assert updated_todo.id == created_todo.id
        assert updated_todo.title == "Updated Title"
        assert updated_todo.description == "New description"
        assert updated_todo.done is True

    def test_update_todo_nonexistent(self, todo_service: TodoService) -> None:
        """Test updating a nonexistent todo."""
        # Arrange
        update_data = TodoCreate(title="Updated Title")

        # Act & Assert
        with pytest.raises(TodoNotFoundError):
            todo_service.update_todo("nonexistent-id", update_data)

    def test_delete_todo_existing(self, todo_service: TodoService) -> None:
        """Test deleting an existing todo."""
        # Arrange
        created_todo = todo_service.create_todo(TodoCreate(title="Test Todo"))

        # Act
        todo_service.delete_todo(created_todo.id)

        # Assert
        with pytest.raises(TodoNotFoundError):
            todo_service.get_todo(created_todo.id)

    def test_delete_todo_nonexistent(self, todo_service: TodoService) -> None:
        """Test deleting a nonexistent todo."""
        # Act & Assert
        with pytest.raises(TodoNotFoundError):
            todo_service.delete_todo("nonexistent-id")
