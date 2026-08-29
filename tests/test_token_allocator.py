from context.token_allocator import TokenAllocator


def test_token_allocator():

    allocator = TokenAllocator(
        total_budget=1000,
        memory_ratio=0.30
    )

    budget = allocator.allocate()

    assert budget["memory_budget"] == 300

    assert budget["knowledge_budget"] == 700