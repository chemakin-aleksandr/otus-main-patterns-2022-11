import logging

from space_invaders.engine.interfaces.command import Command

log = logging.getLogger(__name__)


class LogWriter(Command):
    """Команда, которая записывает информацию о выброшенном исключении в лог"""

    def __init__(self, exc: Exception):
        self._exc = exc

    def execute(self) -> None:
        log.exception(self._exc)
