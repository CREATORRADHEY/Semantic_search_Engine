from citation.citation_builder import CitationBuilder
from models.answer_response import AnswerResponse

from context.context_fusion import ContextFusionEngine
from context.compression_pipeline import CompressionPipeline
from memory.memory_retriever import MemoryRetriever


class RAGEngine:
    """
    Enterprise Production RAG Engine
    """

    def __init__(
        self,
        retriever,
        llm,
        context_builder,
        prompt_builder,
        token_budget,
        memory,
        memory_manager,
        knowledge_manager=None,
    ):
        self.retriever = retriever
        self.llm = llm

        self.context_builder = context_builder
        self.prompt_builder = prompt_builder
        self.token_budget = token_budget

        self.memory = memory
        self.memory_manager = memory_manager
        self.knowledge_manager = knowledge_manager

        self.memory_retriever = MemoryRetriever(memory_manager)

        self.context_fusion = ContextFusionEngine()
        self.pipeline = CompressionPipeline()

        self.citation_builder = CitationBuilder()

    def _build_prompt(self, question):

        self.memory.add_user_message(question)

        memories = self.memory_retriever.retrieve(
            question,
            top_k=2,
        )

        documents = self.retriever.search(
            query=question,
            top_k=5,
        )

        context = self.context_fusion.build(
            memories=memories,
            documents=documents,
        )

        context = self.pipeline.compress(
            context=context,
            question=question,
        )

        if self.token_budget:
            context = self.token_budget.trim_context(context)

        history = self.memory.format_history()

        prompt = self.prompt_builder.build(
            question=question,
            context=context,
            history=history,
        )

        citations = self.citation_builder.build(documents)

        return prompt, citations

    def ask(self, question):

        prompt, citations = self._build_prompt(question)

        answer = self.llm.generate(prompt)

        self.memory.add_assistant_message(answer)

        self.memory_manager.add_memory(
            user_message=question,
            assistant_message=answer,
            metadata={"source": "conversation"},
        )

        self.memory_manager.save()

        return AnswerResponse(
            answer=answer,
            citations=citations,
        )

    def stream_answer(self, question):
        """
        Streams answer token by token.
        """

        _, citations = self._build_prompt(question)

        if hasattr(self.llm, "stream_generate"):

            complete = ""

            for token in self.llm.stream_generate(question):
                complete += token
                yield token

        else:

            complete = self.llm.generate(question)

            for token in complete.split():
                yield token + " "

        self.memory.add_assistant_message(complete)

        self.memory_manager.add_memory(
            user_message=question,
            assistant_message=complete,
            metadata={"source": "conversation"},
        )

        self.memory_manager.save()