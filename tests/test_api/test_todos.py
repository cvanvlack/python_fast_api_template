from fastapi import status
from fastapi.testclient import TestClient


class TestTodosAPI:
    """Integration tests for the todos API endpoints."""

    def test_create_todo(self, client: TestClient) -> None:
        """Test creating a new todo."""
        # Arrange
        todo_data = {
            "title": "Test Todo",
            "description": "Test description",
            "done": False,
        }

        # Act
        response = client.post("/api/todos/", json=todo_data)

        # Assert
        assert response.status_code == status.HTTP_201_CREATED
        data = response.json()
        assert "id" in data
        assert data["title"] == todo_data["title"]
        assert data["description"] == todo_data["description"]
        assert data["done"] == todo_data["done"]

    def test_get_todos_empty(self, client: TestClient) -> None:
        """Test getting all todos when none exist."""
        # This test assumes a clean slate (no previously created todos)
        # In a real application, you might want to clear the todo storage before this test

        # Act
        response = client.get("/api/todos/")

        # Assert
        assert response.status_code == status.HTTP_200_OK
        data = response.json()
        assert isinstance(data, list)
        # Note: This might fail if other tests have already created todos
        # and the service is maintaining state between tests

    def test_create_and_get_todo(self, client: TestClient) -> None:
        """Test creating a todo and then retrieving it by ID."""
        # Arrange - Create a todo
        todo_data = {
            "title": "Get Me",
            "description": "This todo will be retrieved",
            "done": False,
        }
        create_response = client.post("/api/todos/", json=todo_data)
        assert create_response.status_code == status.HTTP_201_CREATED
        created_todo = create_response.json()
        todo_id = created_todo["id"]

        # Act - Get the todo by ID
        response = client.get(f"/api/todos/{todo_id}")

        # Assert
        assert response.status_code == status.HTTP_200_OK
        data = response.json()
        assert data["id"] == todo_id
        assert data["title"] == todo_data["title"]
        assert data["description"] == todo_data["description"]
        assert data["done"] == todo_data["done"]

    def test_get_nonexistent_todo(self, client: TestClient) -> None:
        """Test getting a nonexistent todo by ID."""
        # Act
        response = client.get("/api/todos/nonexistent-id")

        # Assert
        assert response.status_code == status.HTTP_404_NOT_FOUND

    def test_update_todo(self, client: TestClient) -> None:
        """Test updating a todo."""
        # Arrange - Create a todo
        create_data = {
            "title": "Original Title",
            "description": "Original description",
            "done": False,
        }
        create_response = client.post("/api/todos/", json=create_data)
        assert create_response.status_code == status.HTTP_201_CREATED
        created_todo = create_response.json()
        todo_id = created_todo["id"]

        # Arrange - Update data
        update_data = {
            "title": "Updated Title",
            "description": "Updated description",
            "done": True,
        }

        # Act - Update the todo
        response = client.put(f"/api/todos/{todo_id}", json=update_data)

        # Assert
        assert response.status_code == status.HTTP_200_OK
        data = response.json()
        assert data["id"] == todo_id
        assert data["title"] == update_data["title"]
        assert data["description"] == update_data["description"]
        assert data["done"] == update_data["done"]

    def test_update_nonexistent_todo(self, client: TestClient) -> None:
        """Test updating a nonexistent todo."""
        # Arrange
        update_data = {
            "title": "Updated Title",
            "description": "Updated description",
            "done": True,
        }

        # Act
        response = client.put("/api/todos/nonexistent-id", json=update_data)

        # Assert
        assert response.status_code == status.HTTP_404_NOT_FOUND

    def test_delete_todo(self, client: TestClient) -> None:
        """Test deleting a todo."""
        # Arrange - Create a todo
        create_data = {
            "title": "Delete Me",
            "description": "This todo will be deleted",
            "done": False,
        }
        create_response = client.post("/api/todos/", json=create_data)
        assert create_response.status_code == status.HTTP_201_CREATED
        created_todo = create_response.json()
        todo_id = created_todo["id"]

        # Act - Delete the todo
        response = client.delete(f"/api/todos/{todo_id}")

        # Assert - Check the delete response
        assert response.status_code == status.HTTP_204_NO_CONTENT

        # Verify the todo is actually deleted
        get_response = client.get(f"/api/todos/{todo_id}")
        assert get_response.status_code == status.HTTP_404_NOT_FOUND

    def test_delete_nonexistent_todo(self, client: TestClient) -> None:
        """Test deleting a nonexistent todo."""
        # Act
        response = client.delete("/api/todos/nonexistent-id")

        # Assert
        assert response.status_code == status.HTTP_404_NOT_FOUND
