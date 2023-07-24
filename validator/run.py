import json

from validator.model import ActionInput
from validator.action import Action
import github_action_utils as gha
import sys
import os

action_input = ActionInput(
    regex_pattern=os.environ["INPUT_REGEX_PATTERN"],
    text=os.environ["INPUT_TEXT"],
    regex_match_type=os.environ["INPUT_REGEX_MATCH_TYPE"],
    fail_when_no_match=os.environ["INPUT_FAIL_WHEN_NO_MATCH"],
)

action = Action(action_input=action_input)

action_output = action.run()
gha.set_output(name="match", value=json.dumps(action_output.match_))
sys.exit(0 if action_output.match_ else 1)
