from memory.conversation_memory import ConversationMemory


memory = ConversationMemory(max_messages=6)

memory.add_user_message(
    "What is Python?"
)

memory.add_assistant_message(
    "Python is a programming language."
)

memory.add_user_message(
    "Who created it?"
)

memory.add_assistant_message(
    "Guido van Rossum created Python."
)

memory.add_user_message(
    "When was it released?"
)

print("=" * 60)
print("Conversation History")
print("=" * 60)

print(memory.format_history())