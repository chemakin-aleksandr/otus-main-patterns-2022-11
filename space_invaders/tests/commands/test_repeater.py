import pytest
from unittest.mock import Mock

from space_invaders.engine.commands.repeater import Repeater
from space_invaders.engine.interfaces.command import Command


class TestRepeater:
    def test_success(self):
        mock_cmd = Mock()

        Repeater(mock_cmd).execute()

        mock_cmd.execute.assert_called_once_with()

    def test_success_with_raise_exception(self):
        mock_cmd = Mock(Command, side_effect=AttributeError)

        with pytest.raises(AttributeError):
            Repeater(mock_cmd()).execute()
