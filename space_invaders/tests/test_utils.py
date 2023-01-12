from unittest.mock import Mock

from space_invaders.engine import utils
from space_invaders.engine.interfaces import Command, ExceptionHandler


def test_safely_run_command_positive():
    command = Mock(Command)
    exception_handler = Mock(ExceptionHandler)

    utils.safely_run_command(command=command, exception_handler=exception_handler)

    command.execute.assert_called()
    exception_handler.handle.assert_not_called()


def test_safely_run_command_negative():
    command = Mock(Command)
    exception_handler = Mock(ExceptionHandler)

    exception = ZeroDivisionError()
    command.execute.side_effect = exception

    utils.safely_run_command(command=command, exception_handler=exception_handler)

    command.execute.assert_called()
    exception_handler.handle.assert_called_with(command=command, exception=exception)
