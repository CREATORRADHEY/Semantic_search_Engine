from fastapi import FastAPI

from api.routes import router

app = FastAPI(
    title="Semantic Search Engine API",
    version="11.0",
    description="Enterprise Multi-PDF RAG Assistant"
)

app.include_router(router)