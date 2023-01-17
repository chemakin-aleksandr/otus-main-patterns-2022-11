import pytest
from unittest.mock import Mock

from space_invaders.engine.commands import SimpleMacroCommand
from space_invaders.engine.interfaces import Command


def test_simple_macro_command():
    command_first = Mock(Command)
    command_second = Mock(Command)

    SimpleMacroCommand(commands=[command_first, command_second]).execute()

    command_first.execute.assert_called_once()
    command_second.execute.assert_called_once()


def test_simple_macro_command_with_exception():
    command_first = Mock(Command)
    command_second = Mock(Command)

    exception = Exception
    command_first.execute.side_effect = exception()

    with pytest.raises(exception):
        SimpleMacroCommand(commands=[command_first, command_second]).execute()

    command_first.execute.assert_called_once()
    command_second.execute.assert_not_called()
