from validator.main import Action
import pytest


@pytest.mark.parametrize("regex_match_type", ["not_supported_match_type", "MATCH"])
def test_validate_incorrect_input(regex_match_type: str):
    with pytest.raises(SystemExit) as exc_info:
        Action(
            regex_match_type=regex_match_type,
            regex_pattern="^test",
            text="test_validate_input",
        )

    assert exc_info.value.code == 1
