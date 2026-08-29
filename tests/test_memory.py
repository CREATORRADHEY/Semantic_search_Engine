from memory.conversation_memory import ConversationMemory


def test_memory_storage():

    memory = ConversationMemory(max_messages=4)

    memory.add_user_message("Hello")
    memory.add_assistant_message("Hi")

    assert len(memory.get_history()) == 2

    assert "Hello" in memory.format_history()

    