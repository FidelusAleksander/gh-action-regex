import json
import re
import sys
import os
import github_action_utils as gha

SUPPORTED_REGEX_MATCH_TYPES = ["search", "fullmatch", "match"]


class Action:
    def __init__(self, regex_pattern: str, text: str, regex_match_type: str):
        self.regex_match_type = regex_match_type
        self.regex_pattern = regex_pattern
        self.text = text

        self._validate_input()

    @classmethod
    def from_environ(cls):
        return cls(
            regex_pattern=os.environ["INPUT_REGEX_PATTERN"],
            text=os.environ["INPUT_TEXT"],
            regex_match_type=os.environ["INPUT_REGEX_MATCH_TYPE"],
        )

    def _validate_input(self) -> None:
        if self.regex_match_type not in SUPPORTED_REGEX_MATCH_TYPES:
            gha.error(
                f"Regex match type {self.regex_match_type} has to be one of {SUPPORTED_REGEX_MATCH_TYPES}"
            )
            sys.exit(1)

    def _print_result(self, match_successful: bool) -> None:
        body = vars(self)
        body["match"] = match_successful
        gha.debug(json.dumps(body))

    def run(self) -> None:
        match = getattr(re, self.regex_match_type)(
            pattern=self.regex_pattern, string=self.text
        )
        match_successful = bool(match)
        self._print_result(match_successful)
        gha.set_output(name="match", value=json.dumps(match_successful))
        sys.exit(0 if match_successful else 1)


if __name__ == "__main__":
    action = Action.from_environ()
    action.run()
