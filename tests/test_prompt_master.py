import pytest

from app.prompt_library.prompt_master import PromptMaster


def test_get_prompt_replaces_variables():
    pm = PromptMaster("response_master")
    incoming_msg = "What is your name?"
    docs = "Connor is a software engineer."

    prompt = pm.get_prompt("master_response", incoming_msg=incoming_msg, docs=docs)

    assert isinstance(prompt, str)
    assert incoming_msg in prompt
    assert docs in prompt
    # Basic sanity check that prompt contains instruction header
    assert "----------INSTRUCTIONS-------------" in prompt
