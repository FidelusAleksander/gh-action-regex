from validator.model import ActionInput
from validator.action import Action


def test_action_no_match():
    action_input = ActionInput(
        regex_pattern="^text",
        text="test_validate_input",
    )
    action = Action(action_input=action_input)
    action_output = action.run()
    assert action_output.match_ == False


def test_action_beginning_match():
    action_input = ActionInput(
        regex_pattern="^test",
        text="test_validate_input",
    )
    action = Action(action_input=action_input)
    action_output = action.run()
    assert action_output.match_ == True


def test_action_end_match():
    action_input = ActionInput(
        regex_pattern="input$",
        text="test_validate_input",
    )
    action = Action(action_input=action_input)
    action_output = action.run()
    assert action_output.match_ == True


def test_action_beginning_end_match():
    action_input = ActionInput(
        regex_pattern="^test_validate_input$",
        text="test_validate_input",
    )
    action = Action(action_input=action_input)
    action_output = action.run()
    assert action_output.match_ == True
