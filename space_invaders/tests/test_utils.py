from unittest.mock import Mock

from space_invaders.engine import utils
from space_invaders.engine.errors.exception_handler import ExceptionHandler
from space_invaders.engine.interfaces import Command


class TestRunCommand:
    def test_success(self):
        cmd = Mock(Command)
        exception_handler = Mock(ExceptionHandler)

        utils.run_command(cmd=cmd, exception_handler=exception_handler)

        cmd.execute.assert_called()
        exception_handler.handle.assert_not_called()

    def test_fail(self):
        cmd = Mock(Command)
        exception_handler = Mock(ExceptionHandler)

        exception = ZeroDivisionError()
        cmd.execute.side_effect = exception

        utils.run_command(cmd=cmd, exception_handler=exception_handler)

        cmd.execute.assert_called()
        exception_handler.handle.assert_called_with(cmd=cmd, exc=exception)
