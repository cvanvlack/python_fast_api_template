from pydantic import BaseModel, Field


class TodoBase(BaseModel):
    """
    Base Todo model with common attributes.
    """

    title: str = Field(
        ..., min_length=1, max_length=100, description="Title of the todo item"
    )
    description: str = Field(
        default="", max_length=1000, description="Detailed description of the todo item"
    )
    done: bool = Field(default=False, description="Indicates if the todo is completed")


class TodoCreate(TodoBase):
    """
    Model for creating a new Todo.
    """

    pass


class TodoResponse(TodoBase):
    """
    Model for Todo responses, includes all fields from TodoBase plus the ID.
    """

    id: str = Field(..., description="Unique identifier for the todo item")
