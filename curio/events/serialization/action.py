from curio.core.exceptions import LLMMalformedActionError
from curio.events.action.action import Action
from curio.events.action.agent import (
    AgentDelegateAction,
    AgentFinishAction,
    AgentRejectAction,
    ChangeAgentStateAction,
)
from curio.events.action.browse import BrowseInteractiveAction, BrowseURLAction
from curio.events.action.commands import (
    CmdRunAction,
    IPythonRunCellAction,
)
from curio.events.action.empty import NullAction
from curio.events.action.files import FileReadAction, FileWriteAction
from curio.events.action.message import MessageAction
from curio.events.action.tasks import AddTaskAction, ModifyTaskAction

actions = (
    NullAction,
    CmdRunAction,
    IPythonRunCellAction,
    BrowseURLAction,
    BrowseInteractiveAction,
    FileReadAction,
    FileWriteAction,
    AgentFinishAction,
    AgentRejectAction,
    AgentDelegateAction,
    AddTaskAction,
    ModifyTaskAction,
    ChangeAgentStateAction,
    MessageAction,
)

ACTION_TYPE_TO_CLASS = {action_class.action: action_class for action_class in actions}  # type: ignore[attr-defined]


def action_from_dict(action: dict) -> Action:
    if not isinstance(action, dict):
        raise LLMMalformedActionError('action must be a dictionary')
    action = action.copy()
    if 'action' not in action:
        raise LLMMalformedActionError(f"'action' key is not found in {action=}")
    if not isinstance(action['action'], str):
        raise LLMMalformedActionError(
            f"'{action['action']=}' is not defined. Available actions: {ACTION_TYPE_TO_CLASS.keys()}"
        )
    action_class = ACTION_TYPE_TO_CLASS.get(action['action'])
    if action_class is None:
        raise LLMMalformedActionError(
            f"'{action['action']=}' is not defined. Available actions: {ACTION_TYPE_TO_CLASS.keys()}"
        )
    args = action.get('args', {})
    try:
        decoded_action = action_class(**args)
        if 'timeout' in action:
            decoded_action.timeout = action['timeout']
    except TypeError:
        raise LLMMalformedActionError(f'action={action} has the wrong arguments')
    return decoded_action
