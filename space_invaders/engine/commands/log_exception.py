import logging

from space_invaders.engine.interfaces.command import Command

log = logging.getLogger(__name__)


class LogException(Command):
    """Команда, которая записывает информацию о выброшенном исключении в лог"""

    def __init__(self, exception: Exception):
        self._exception = exception

    def execute(self) -> None:
        log.exception(self._exception)
