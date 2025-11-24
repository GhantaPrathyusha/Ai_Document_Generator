from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.openapi.utils import get_openapi

from .database import engine
from .models import Base as ModelsBase

# Routers
from .auth.routes import router as auth_router
from .content.routes import router as content_router
from .documents.routes import router as documents_router

# Create FastAPI app
app = FastAPI(title="AI Doc Generator")


# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Routers
app.include_router(auth_router, prefix="/auth")
app.include_router(content_router, prefix="/content")
app.include_router(documents_router, prefix="/documents")


# Database tables
ModelsBase.metadata.create_all(bind=engine)


# Root endpoint
@app.get("/")
def read_root():
    return {"message": "AI Doc Generator backend running. See /docs"}


# -------------------------
# Custom OpenAPI (Swagger)
# -------------------------
def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema

    openapi_schema = get_openapi(
        title="AI Doc Generator API",
        version="1.0",
        routes=app.routes,
    )

    # Add Bearer Auth
    openapi_schema["components"]["securitySchemes"] = {
        "BearerAuth": {
            "type": "http",
            "scheme": "bearer",
            "bearerFormat": "JWT",
        }
    }

    # Apply BearerAuth globally
    for path in openapi_schema["paths"].values():
        for method in path.values():
            method.setdefault("security", [{"BearerAuth": []}])

    app.openapi_schema = openapi_schema
    return app.openapi_schema


# Override default OpenAPI generator
app.openapi = custom_openapi
