from abc import ABC, abstractmethod

__all__ = [
    'Rotable',
]


class Rotable(ABC):
    """Интерфейс вращения объекта вокруг своей оси.
    Вариант реализации с целыми координатами.
    """

    @property
    @abstractmethod
    def direction(self) -> int:
        """Номер текущего направления"""
        ...

    @direction.setter
    @abstractmethod
    def direction(self, direction: int) -> None:
        """Номер текущего направления"""
        ...

    @property
    @abstractmethod
    def directions_number(self) -> int:
        """Количество направлений"""
        ...

    @property
    @abstractmethod
    def angular_velocity(self) -> int:
        """Угловая скорость"""
        ...
