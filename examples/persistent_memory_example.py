from memory.memory_manager import MemoryManager

print("=" * 60)
print("Persistent Memory Demo")
print("=" * 60)

manager = MemoryManager()

manager.add_memory(
    "What is Kubernetes?",
    "Kubernetes orchestrates containers across clusters.",
    metadata={"topic": "Cloud"}
)

manager.save()

print("Memory Saved.")
print()

print("Restart Simulation")
print("-" * 60)

new_manager = MemoryManager()

results = new_manager.search(
    "container orchestration",
    top_k=1
)

for score, memory in results:

    print(f"Score : {score:.4f}")
    print(memory.user_message)
    print(memory.assistant_message)