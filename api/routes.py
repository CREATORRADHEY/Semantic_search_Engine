from fastapi import APIRouter, Depends

from api.schemas import (
    ChatRequest,
    SearchRequest,
    IndexRequest,
    HealthResponse,
    SearchResponse
)

from api.dependencies import get_rag_engine

router = APIRouter()


@router.get("/health", response_model=HealthResponse)
async def health():
    return HealthResponse(
        status="healthy",
        version="11.0"
    )


@router.post("/chat")
async def chat(
    request: ChatRequest,
    engine=Depends(get_rag_engine)
):
    answer = engine.ask(request.question)

    return answer


@router.post("/search")
async def search(
    request: SearchRequest,
    engine=Depends(get_rag_engine)
):
    results = engine.retriever.search(
        request.query,
        top_k=request.top_k
    )

    response = []

    for result in results:
        response.append(
            SearchResponse(
                score=result.score,
                text=result.text,
                source=result.metadata["source"]
            )
        )

    return response


@router.get("/documents")
async def documents(
    engine=Depends(get_rag_engine)
):
    return engine.retriever.knowledge_base.list_documents()


@router.post("/index")
async def index_document(
    request: IndexRequest,
    engine=Depends(get_rag_engine)
):
    return {
        "message": f"Indexed {request.file_path}",
        "category": request.category
    }