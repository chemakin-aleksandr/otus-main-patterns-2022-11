from abc import ABC, abstractmethod


class Command(ABC):
    """Интерфейс команды."""

    @abstractmethod
    def execute(self) -> None:
        """Выполнить команду."""