from fastapi import APIRouter
from fastapi.responses import StreamingResponse

from api.dependencies import get_rag_engine

router = APIRouter()

rag_engine = get_rag_engine()


@router.get("/health")
def health():

    return {
        "status": "healthy"
    }


@router.post("/chat")
def chat(request: dict):

    response = rag_engine.ask(
        request["question"]
    )

    return response.model_dump()


@router.post("/stream-chat")
def stream_chat(request: dict):

    question = request["question"]

    generator = rag_engine.stream_answer(question)

    return StreamingResponse(
        generator,
        media_type="text/plain"
    )


@router.post("/search")
def search(request: dict):

    results = rag_engine.retriever.search(
        request["query"]
    )

    return [
        item.model_dump()
        for item in results
    ]


@router.get("/documents")
def documents():

    docs = rag_engine.knowledge_manager.list_documents()

    return [
        item.filename
        for item in docs
    ]


@router.post("/index")
def index(request: dict):

    rag_engine.knowledge_manager.index_pdf(
        request["filename"]
    )

    return {
        "message": "Indexed Successfully."
    }