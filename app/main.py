from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.routes import todos
from app.core.config import settings
from app.core.exceptions.handlers import register_exception_handlers


def create_application() -> FastAPI:
    """
    Create and configure the FastAPI application.

    Returns:
        FastAPI: Configured FastAPI application instance
    """
    application = FastAPI(
        title=settings.PROJECT_NAME,
        description=settings.PROJECT_DESCRIPTION,
        version=settings.VERSION,
        openapi_url=f"{settings.API_PREFIX}/openapi.json",
        docs_url="/docs",
        redoc_url="/redoc",
    )

    # Configure CORS
    application.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],  # Allow all origins
        allow_credentials=True,
        allow_methods=["*"],  # Allows all methods
        allow_headers=["*"],  # Allows all headers
    )

    # Include routers
    application.include_router(todos.router, prefix=settings.API_PREFIX)

    # Register exception handlers
    register_exception_handlers(application)

    return application


app = create_application()
