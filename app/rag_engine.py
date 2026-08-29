from citation.citation_builder import CitationBuilder
from models.answer_response import AnswerResponse

from memory.memory_retriever import MemoryRetriever
from context.context_fusion import ContextFusionEngine
from context.compression_pipeline import CompressionPipeline


class RAGEngine:

    def __init__(
        self,
        retriever,
        llm,
        context_builder,
        prompt_builder,
        token_budget,
        memory,
        memory_manager
    ):

        self.retriever = retriever
        self.llm = llm

        self.context_builder = context_builder
        self.prompt_builder = prompt_builder

        self.token_budget = token_budget

        self.context_fusion = ContextFusionEngine()

        self.memory = memory

        self.memory_manager = memory_manager

        self.memory_retriever = MemoryRetriever(
            memory_manager
        )

        self.citation_builder = CitationBuilder()

        self.pipeline = CompressionPipeline()

    def ask(self, question: str):

        self.memory.add_user_message(question)

        memory_results = self.memory_retriever.retrieve(
            question,
            top_k=2
        )

        document_results = self.retriever.search(
            query=question,
            top_k=5
        )

        fused_context = self.context_fusion.build(
            memories=memory_results,
            documents=document_results
        )

        compressed_context = self.pipeline.compress(
            query=question,
            memory_records=memory_results,
            knowledge_context=fused_context
        )

        if self.token_budget is not None:

            compressed_context = (
                self.token_budget.trim_context(
                    compressed_context
                )
            )

        history = self.memory.format_history()

        prompt = self.prompt_builder.build(
            question=question,
            context=compressed_context,
            history=history
        )

        answer = self.llm.generate(prompt)

        self.memory.add_assistant_message(
            answer
        )

        self.memory_manager.add_memory(
            user_message=question,
            assistant_message=answer,
            metadata={
                "source": "conversation"
            }
        )

        self.memory_manager.save()

        citations = self.citation_builder.build(
            document_results
        )

        return AnswerResponse(
            answer=answer,
            citations=citations
        )