from abc import ABC, abstractmethod


class AngularVelocityController(ABC):
    """Интерфейс для объекта с изменяемой угловой скоростью."""

    @property
    @abstractmethod
    def angular_velocity(self) -> int:
        """Возвращает текущую угловую скорость"""

    @angular_velocity.setter
    @abstractmethod
    def angular_velocity(self, velocity: int) -> None:
        """Устанавливает текущую угловую скорость"""

    @property
    @abstractmethod
    def angular_velocity_correction(self) -> int:
        """Возвращает величину коррекции угловой скорости"""
