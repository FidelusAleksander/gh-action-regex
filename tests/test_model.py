from validator.model import ActionOutput


def test_action_output_alias():
    action_output = ActionOutput(match=True)
    assert action_output.model_dump() == {"match_": True}
    assert action_output.model_dump(by_alias=True) == {"match": True}
