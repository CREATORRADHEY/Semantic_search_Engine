from context.token_allocator import TokenAllocator

allocator = TokenAllocator(
    total_budget=1500,
    memory_ratio=0.30
)

budget = allocator.allocate()

print("=" * 60)
print("Token Allocation")
print("=" * 60)

print(budget)