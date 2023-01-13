from abc import ABC, abstractmethod


class Command(ABC):
    """Командный интерфейс"""

    @abstractmethod
    def execute(self) -> None:
        """Выполнить команду"""
        ...
