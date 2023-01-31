from unittest.mock import Mock

from space_invaders.engine.commands import Rotate
from space_invaders.engine.commands.log_writer import LogWriter
from space_invaders.engine.commands.repeater import Repeater, DoubleRepeater
from space_invaders.engine.errors.exception_handler import ExceptionHandler


def fake_start(self):
    while not self._queue.empty():
        cmd = self._queue.get()
        try:
            cmd.execute()
        except Exception as exc:
            self.ex_handler.handle(cmd, exc)


class TestExceptionHandler:

    def test_log_handler_put(self):
        mock_obj = Mock()
        mock_queue = Mock()
        exc_handler = ExceptionHandler(mock_queue)

        exc_handler.log_handler(cmd=Rotate(mock_obj), exc=ValueError('some exception'))

        mock_queue.put.assert_called_once()
        assert isinstance(mock_queue.put.call_args[0][0], LogWriter)
        assert mock_queue.put.call_args[0][0]._exc.args[0] == 'some exception'

    def test_log_handler_queue(self):
        exc = ValueError('some exception')
        mock_obj, mock_queue = Mock(), Mock()
        mock_queue.get.return_value = LogWriter(exc=exc)
        exc_handler = ExceptionHandler(mock_queue)

        exc_handler.log_handler(cmd=Rotate(mock_obj), exc=exc)
        cmd = mock_queue.get()

        assert isinstance(cmd, LogWriter)
        assert cmd._exc.args[0] == 'some exception'

    def test_repeater_handler_put(self):
        mock_obj = Mock()
        mock_queue = Mock()
        exc_handler = ExceptionHandler(mock_queue)

        exc_handler.repeater_handler(
            cmd=Rotate(mock_obj), exc=ValueError('some exception')
        )

        mock_queue.put.assert_called_once()
        assert isinstance(mock_queue.put.call_args[0][0], Repeater)

    def test_repeater_handler_queue(self):
        exc = ValueError('some exception')
        mock_obj, mock_queue = Mock(), Mock()
        mock_queue.get.return_value = Repeater(cmd=mock_obj)
        exc_handler = ExceptionHandler(mock_queue)

        exc_handler.repeater_handler(cmd=Rotate(mock_obj), exc=exc)
        cmd = mock_queue.get()

        assert isinstance(cmd, Repeater)

    def test_double_repeater_handler_put(self):
        mock_obj = Mock()
        mock_queue = Mock()
        exc_handler = ExceptionHandler(mock_queue)

        exc_handler.double_repeater_handler(
            cmd=Rotate(mock_obj), exc=ValueError('test exception')
        )

        mock_queue.put.assert_called()
        mock_queue.put.assert_called_once()
        assert isinstance(mock_queue.put.call_args[0][0], DoubleRepeater)

    def test_double_repeater_handler_queue(self):
        mock_obj, mock_queue = Mock(), Mock()
        mock_queue.get.return_value = DoubleRepeater(cmd=mock_obj)
        exc_handler = ExceptionHandler(mock_queue)

        exc_handler.double_repeater_handler(
            cmd=Rotate(mock_obj), exc=ValueError('test exception')
        )

        cmd = mock_queue.get(timeout=3)
        assert isinstance(cmd, DoubleRepeater)
