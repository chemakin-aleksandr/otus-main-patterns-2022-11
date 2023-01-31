from abc import ABC, abstractmethod

from space_invaders.engine.interfaces.command import Command


class BaseExceptionHandler(ABC):
    """Обработчик исключения."""

    @abstractmethod
    def handle(self, cmd: Command, exc: Exception) -> None:
        """Обработать исключение.

        Args:
            command: Команда, вызвавшая исключение.
            exception: Исключение, вызванное командой.
        """
