import json
import re
import sys
import os


class Action:
    SUPPORTED_REGEX_MATCH_TYPES = ["search", "fullmatch", "match"]

    def __init__(self, regex_pattern: str, text: str, regex_match_type: str):
        self.REGEX_MATCH_TYPE = regex_match_type
        self.REGEX_PATTERN = regex_pattern
        self.TEXT = text

        self._validate_input()

    @classmethod
    def from_environ(cls):
        return cls(
            regex_pattern=os.environ["INPUT_REGEX_PATTERN"],
            text=os.environ["INPUT_TEXT"],
            regex_match_type=os.environ["INPUT_REGEX_MATCH_TYPE"],
        )

    def _validate_input(self):
        if self.REGEX_MATCH_TYPE not in self.SUPPORTED_REGEX_MATCH_TYPES:
            print(
                f"Regex match type {self.REGEX_MATCH_TYPE} has to be one of {self.SUPPORTED_REGEX_MATCH_TYPES}"
            )
            sys.exit(1)

    def _print_result(self, successful: bool):
        body = vars(self)
        body["MATCH"] = successful
        print(json.dumps(body))
        print(f"::set-output name=MATCH::{json.dumps(successful)}")

    def run(self):
        result = getattr(re, self.REGEX_MATCH_TYPE)(
            pattern=self.REGEX_PATTERN, string=self.TEXT
        )
        self._print_result(bool(result))
        sys.exit(0 if result else 1)


if __name__ == "__main__":
    action = Action.from_environ()
    action.run()
