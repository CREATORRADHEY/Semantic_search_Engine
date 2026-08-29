from models.message import Message


class ConversationMemory:
    """
    Stores recent conversation history for multi-turn RAG.
    """

    def __init__(self, max_messages: int = 10):
        self.max_messages = max_messages
        self.messages: list[Message] = []

    def add_user_message(self, text: str) -> None:
        self.messages.append(
            Message(role="user", content=text)
        )
        self._trim()

    def add_assistant_message(self, text: str) -> None:
        self.messages.append(
            Message(role="assistant", content=text)
        )
        self._trim()

    def get_history(self) -> list[Message]:
        return self.messages

    def format_history(self) -> str:
        history = []

        for message in self.messages:
            history.append(
                f"{message.role.upper()}: {message.content}"
            )

        return "\n".join(history)

    def clear(self) -> None:
        self.messages = []

    def _trim(self) -> None:
        if len(self.messages) > self.max_messages:
            self.messages = self.messages[-self.max_messages:]