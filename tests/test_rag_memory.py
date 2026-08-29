from memory.conversation_memory import ConversationMemory


def test_memory_trim():

    memory = ConversationMemory(max_messages=2)

    memory.add_user_message("A")
    memory.add_assistant_message("B")
    memory.add_user_message("C")

    history = memory.get_history()

    assert len(history) == 2

    assert history[0].content == "B"

    assert history[1].content == "C"