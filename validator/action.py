import json
import re
import github_action_utils as gha
from validator.model import ActionInput, ActionOutput


class Action:
    def __init__(self, action_input: ActionInput):
        self.action_input = action_input

    def _print_result(self, match_successful: bool) -> None:
        result_dict = self.action_input.model_dump()
        result_dict["match"] = match_successful
        gha.debug(json.dumps(result_dict))

    def run(self) -> ActionOutput:
        match = getattr(re, self.action_input.regex_match_type)(
            pattern=self.action_input.regex_pattern, string=self.action_input.text
        )
        match_successful = bool(match)
        self._print_result(match_successful)
        return ActionOutput(match=match_successful)
