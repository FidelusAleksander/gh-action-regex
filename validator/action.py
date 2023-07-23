import json
import re
import sys
import github_action_utils as gha
from validator.model import ActionInput


class Action:
    def __init__(self, action_input: ActionInput):
        self.action_input = action_input

    def _print_result(self, match_successful: bool) -> None:
        body = vars(self)
        body["match"] = match_successful
        gha.debug(json.dumps(body))

    def run(self) -> None:
        match = getattr(re, self.action_input.regex_match_type)(
            pattern=self.action_input.regex_pattern, string=self.action_input.text
        )
        match_successful = bool(match)
        self._print_result(match_successful)
        gha.set_output(name="match", value=json.dumps(match_successful))
        sys.exit(0 if match_successful else 1)
