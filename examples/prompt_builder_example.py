from context.context_builder import ContextBuilder
from context.prompt_builder import PromptBuilder

from models.search_result import SearchResult


results = [

    SearchResult(
        document_id="python",
        chunk_id="1",
        text="Python supports object-oriented programming using classes and objects.",
        score=9,
        metadata={"source": "python.pdf"}
    ),

    SearchResult(
        document_id="python",
        chunk_id="2",
        text="Classes allow reusable software components.",
        score=8,
        metadata={"source": "python.pdf"}
    )

]

context_builder = ContextBuilder()

context = context_builder.build(results)

prompt_builder = PromptBuilder()

prompt = prompt_builder.build(
    question="Explain Python classes in simple language.",
    context=context
)

print("=" * 60)
print("LLM Prompt")
print("=" * 60)
print(prompt)