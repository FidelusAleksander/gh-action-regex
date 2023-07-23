import github_action_utils as gha
from validator.model import ActionInput
from validator.action import Action
import os

action_input = ActionInput(
    regex_pattern=os.environ["INPUT_REGEX_PATTERN"],
    text=os.environ["INPUT_TEXT"],
    regex_match_type=os.environ["INPUT_REGEX_MATCH_TYPE"],
)
action = Action(action_input=action_input)
action.run()
