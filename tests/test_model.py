from validator.model import ActionInput, ActionOutput
import pytest


@pytest.mark.parametrize("regex_match_type", ["not_supported_match_type", "MATCH"])
def test_validate_incorrect_action_input(regex_match_type: str):
    with pytest.raises(SystemExit) as exc_info:
        ActionInput(
            regex_match_type=regex_match_type,
            regex_pattern="^test",
            text="test_validate_input",
        )

    assert exc_info.value.code == 1


def test_action_output_alias():
    action_output = ActionOutput(match=True)
    assert action_output.model_dump() == {"match_": True}
    assert action_output.model_dump(by_alias=True) == {"match": True}
