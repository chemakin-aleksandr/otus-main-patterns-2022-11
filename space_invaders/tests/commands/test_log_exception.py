import pytest
from unittest.mock import Mock

from space_invaders.engine.commands.log_exception import LogException, log


class TestLogWriter:
    def test_success(self, caplog):
        error_message = 'Some exception'
        exc = ValueError(error_message)

        LogException(exc).execute()

        assert [error_message] == [rec.message for rec in caplog.records]

    def test_fail(self):
        log.exception = Mock()
        log.exception.side_effect = AttributeError('Some went wrong')
        exc = AttributeError('Some exception')

        try:
            raise exc
        except AttributeError:
            with pytest.raises(AttributeError):
                LogException(exc).execute()

        log.exception.assert_called_once_with(exc)
