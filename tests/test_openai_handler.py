from types import SimpleNamespace

import pytest

from app.helpers import openai_handler as oh


class FakeOpenAI:
    """Minimal stub for openai.OpenAI used in embeddingHandler."""

    class embeddings:  # pylint: disable=too-few-public-methods
        @staticmethod
        def create(*_args, **_kwargs):
            return SimpleNamespace(data=[SimpleNamespace(embedding=[0.1, 0.2, 0.3])])


def test_get_embedding_returns_vector(monkeypatch):
    # Patch the OpenAI class inside the module with our fake implementation
    monkeypatch.setattr(oh, "OpenAI", FakeOpenAI)

    handler = oh.embeddingHandler()
    vector = handler.get_embedding("test text")

    assert isinstance(vector, list)
    assert vector == [0.1, 0.2, 0.3]
    # Ensure the vector has floats
    assert all(isinstance(v, float) for v in vector)
