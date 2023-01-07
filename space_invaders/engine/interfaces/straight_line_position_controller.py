from abc import ABC, abstractmethod


class MoveController(ABC):
    """Интерфейс для перемещаемого объекта."""

    @property
    @abstractmethod
    def position(self):
        """Возвращает текущие координаты"""

    @position.setter
    @abstractmethod
    def position(self, value) -> None:
        """Изменяет текущие координаты"""

    @property
    @abstractmethod
    def velocity(self):
        """Возвращает координаты после перемещения"""
