from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse

from app.core.exceptions.todo_exceptions import TodoNotFoundError, TodoValidationError


def register_exception_handlers(app: FastAPI) -> None:
    """Register all exception handlers with the FastAPI application."""

    @app.exception_handler(TodoNotFoundError)
    async def todo_not_found_handler(
        request: Request, exc: TodoNotFoundError
    ) -> JSONResponse:
        """
        Handle TodoNotFoundError exceptions.

        Args:
            request: The request that caused the exception
            exc: The exception instance

        Returns:
            JSONResponse: A JSON response with a 404 status code
        """
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content={"detail": exc.message},
        )

    @app.exception_handler(TodoValidationError)
    async def todo_validation_error_handler(
        request: Request, exc: TodoValidationError
    ) -> JSONResponse:
        """
        Handle TodoValidationError exceptions.

        Args:
            request: The request that caused the exception
            exc: The exception instance

        Returns:
            JSONResponse: A JSON response with a 422 status code
        """
        return JSONResponse(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            content={"detail": exc.message},
        )
