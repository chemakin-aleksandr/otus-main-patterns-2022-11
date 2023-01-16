from abc import ABC, abstractmethod

from space_invaders.engine.interfaces.command import Command


class ExceptionHandler(ABC):
    """Обработчик исключения."""

    @abstractmethod
    def handle(self, command: Command, exception: Exception) -> None:
        """Обработать исключение.

        Args:
            command: Команда, вызвавшая исключение.
            exception: Исключение, вызванное командой.
        """
