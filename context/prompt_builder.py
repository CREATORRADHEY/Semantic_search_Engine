class PromptBuilder:

    SYSTEM_PROMPT = """
You are an AI assistant.

Use BOTH:

1. Previous conversation memory.
2. Retrieved knowledge context.

If memory helps answer the question,
use it.

If the answer is unavailable,
say you don't know.
"""

    def build(
        self,
        question,
        context,
        history=""
    ):

        prompt = f"""
{self.SYSTEM_PROMPT}

================ HISTORY ================

{history}

================ CONTEXT ================

{context}

=========================================

Question:
{question}

Answer:
"""

        return prompt.strip()