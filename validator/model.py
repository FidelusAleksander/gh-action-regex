from pydantic import BaseModel, field_validator
import sys
import github_action_utils as gha

SUPPORTED_REGEX_MATCH_TYPES = ["search", "fullmatch", "match"]


class ActionInput(BaseModel):
    text: str
    regex_pattern: str
    regex_match_type: str

    @field_validator("regex_match_type")
    def name_must_contain_space(cls, v):
        if v not in SUPPORTED_REGEX_MATCH_TYPES:
            gha.error(
                f"Regex match type {v} has to be one of {SUPPORTED_REGEX_MATCH_TYPES}"
            )
            sys.exit(1)
        return v
