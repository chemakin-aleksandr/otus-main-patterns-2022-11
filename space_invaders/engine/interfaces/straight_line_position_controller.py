from abc import ABC, abstractmethod


class MoveController(ABC):
    """Interface of movable object."""

    @property
    @abstractmethod
    def position(self):
        """Returning current location"""

    @position.setter
    @abstractmethod
    def position(self, value) -> None:
        """Changing current location"""

    @property
    @abstractmethod
    def velocity(self):
        """Returning moment velocity"""
