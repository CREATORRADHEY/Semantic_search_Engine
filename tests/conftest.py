import pytest

from api.dependencies import get_rag_engine


@pytest.fixture
def mock_engine():
    """
    Reuse the application's dependency graph exactly as production does.
    This avoids constructor mismatches after refactors.
    """
    engine = get_rag_engine()

    engine.memory_manager.clear()
    engine.memory.clear()

    return engine