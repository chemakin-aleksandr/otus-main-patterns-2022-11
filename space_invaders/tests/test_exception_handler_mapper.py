import pytest
from unittest.mock import Mock

from space_invaders.engine import ExceptionHandlerMapper
from space_invaders.engine.interfaces import Command


@pytest.fixture
def mapper():
    return ExceptionHandlerMapper()


@pytest.fixture
def dummy_command_class():
    class dummy_command(Command):
        def execute(self) -> None:
            pass

    return dummy_command


@pytest.fixture
def command_1():
    return Mock(Command)


@pytest.fixture
def command_2():
    return Mock(Command)


@pytest.fixture
def exception_1():
    class Exception_1(Exception):
        pass

    return Exception_1


@pytest.fixture
def exception_2():
    class Exception_2(Exception):
        pass

    return Exception_2


def test_single_handler(command_1, exception_1):

    mapper = ExceptionHandlerMapper()  # mapper instance on test

    handler = Mock(Command)

    mapper.register_handler(handler=handler, command=command_1, exception=exception_1)
    mapper.handle(command_1, exception_1)

    handler.execute.assert_called_once()


def test_multiple_handlers(command_1, command_2, exception_1, exception_2):

    mapper = ExceptionHandlerMapper()  # mapper instance on test

    handler_1 = Mock(Command)
    handler_2 = Mock(Command)

    mapper.register_handler(handler=handler_1, command=command_1, exception=exception_1)
    mapper.register_handler(handler=handler_2, command=command_1, exception=exception_2)
    mapper.register_handler(handler=handler_2, command=command_2, exception=exception_1)
    mapper.register_handler(handler=handler_2, command=command_2, exception=exception_2)
    mapper.handle(command_1, exception_1)  # должен вызвать handler_1
    mapper.handle(command_1, exception_2)  # должен вызвать handler_2
    mapper.handle(command_2, exception_1)  # должен вызвать handler_2
    mapper.handle(command_2, exception_2)  # должен вызвать handler_2

    handler_1.execute.assert_called_once()
    assert handler_2.execute.call_count == 3


def test_default_handler(command_1, exception_1, exception_2):

    default_handler = Mock(Command)
    mapper = ExceptionHandlerMapper(default_handler=default_handler)  # mapper instance on test

    handler_1 = Mock(Command)

    mapper.register_handler(handler=handler_1, exception=exception_1)
    mapper.handle(command_1, exception_2)  # должен вызвать default_handler

    handler_1.execute.assert_not_called()
    default_handler.execute.assert_called_once()


def test_any_command_to_one_exception(command_1, command_2, exception_1):

    mapper = ExceptionHandlerMapper()  # mapper instance on test

    handler_1 = Mock(Command)

    mapper.register_handler(handler=handler_1, exception=exception_1)
    mapper.handle(command_1, exception_1)  # должен вызвать handler_1
    mapper.handle(command_2, exception_1)  # должен вызвать handler_1

    assert handler_1.execute.call_count == 2


def test_any_exception_of_one_command(command_1, exception_1, exception_2):

    mapper = ExceptionHandlerMapper()  # mapper instance on test

    handler_1 = Mock(Command)

    mapper.register_handler(handler=handler_1, command=command_1)
    mapper.handle(command_1, exception_1)  # должен вызвать handler_1
    mapper.handle(command_1, exception_2)  # должен вызвать handler_1

    assert handler_1.execute.call_count == 2


def test_command_and_exception_prioritization(command_1, command_2, exception_1, exception_2):

    mapper = ExceptionHandlerMapper()  # mapper instance on test

    handler_1 = Mock(Command)
    handler_2 = Mock(Command)
    handler_3 = Mock(Command)

    mapper.register_handler(handler=handler_1, command=command_1)  # низкий приоритет
    mapper.register_handler(handler=handler_2, exception=exception_2)  # низкий приоритет
    mapper.register_handler(handler=handler_3, command=command_1, exception=exception_2)  # высокий приоритет

    mapper.handle(command_1, exception_1)  # должен вызвать handler_1

    handler_1.execute.assert_called_once()
    handler_2.execute.assert_not_called()
    handler_3.execute.assert_not_called()

    handler_1.reset_mock()
    handler_2.reset_mock()
    handler_3.reset_mock()

    mapper.handle(command_2, exception_2)  # должен вызвать handler_2

    handler_1.execute.assert_not_called()
    handler_2.execute.assert_called_once()
    handler_3.execute.assert_not_called()

    handler_1.reset_mock()
    handler_2.reset_mock()
    handler_3.reset_mock()

    mapper.handle(command_1, exception_2)  # должен вызвать handler_3

    handler_1.execute.assert_not_called()
    handler_2.execute.assert_not_called()
    handler_3.execute.assert_called_once()
