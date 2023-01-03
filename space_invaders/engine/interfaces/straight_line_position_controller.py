from abc import ABC, abstractmethod


class StraightLinePositionController(ABC):
    """Интерфейс для перемещаемого объекта."""

    @property
    @abstractmethod
    def current_position(self) -> [int,int]:
        """Возвращает текущие координаты"""

    @current_position.setter
    @abstractmethod
    def current_position(self, value: [int,int]) -> None:
        """Изменяет текущие координаты"""

    @property
    @abstractmethod
    def position_correction(self) -> [int,int]:
        """Возвращает величину последнего перемещения"""
