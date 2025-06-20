from types import SimpleNamespace

import pytest

from app.helpers import pinecone_handler as ph


class FakeEmbeddingHandler:
    """Stub embedding handler that returns a predictable embedding."""

    @staticmethod
    def get_embedding(_text):
        return [0.1, 0.2]


class FakeIndex:
    """Stub Index object returned by FakePinecone."""

    def __init__(self):
        self.last_upsert = None

    def upsert(self, vectors, namespace):  # noqa: D401
        self.last_upsert = (vectors, namespace)
        # Mimic Pinecone upsert which returns dict or None; does not matter
        return None

    def query(self, *args, **kwargs):  # For completeness in other calls
        return SimpleNamespace(matches=[])


class FakePinecone:
    """Minimal stub replicating pinecone.Pinecone interface used in code."""

    def __init__(self, api_key=None):  # pylint: disable=unused-argument
        self.index = FakeIndex()

    def Index(self, _index_name):  # pylint: disable=invalid-name
        return self.index


def test_pc_upsert_success(monkeypatch):
    # Patch Pinecone and embeddingHandler used in PineconeHandler
    monkeypatch.setattr(ph, "Pinecone", FakePinecone)
    monkeypatch.setattr(ph, "embeddingHandler", FakeEmbeddingHandler)

    handler = ph.PineconeHandler()

    success = handler.pc_upsert(
        index_name="test-index",
        text="hello world",
        namespace="test",
        metadata={"text": "hello world"},
    )

    assert success is True
    # Verify the fake index captured the upsert data
    assert handler._get_index("test-index").last_upsert is not None
