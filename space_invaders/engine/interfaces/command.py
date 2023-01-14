from abc import ABC, abstractmethod


class Command(ABC):
    """Interface of command"""

    @abstractmethod
    def execute(self) -> None:
        """Выполнить команду."""
