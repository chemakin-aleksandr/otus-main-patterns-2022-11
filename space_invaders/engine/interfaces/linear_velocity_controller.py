from abc import ABC, abstractmethod


class LinearVelocityController(ABC):
    """Интерфейс к объекту, обладающему возможностью изменения линейной скорости."""

    @property
    @abstractmethod
    def linear_velocity(self) -> int:
        """Возвращает текущую линейную скорость движения"""

    @linear_velocity.setter
    @abstractmethod
    def linear_velocity(self, velocity: int) -> None:
        """Устанавливает текущую линейную скорость движения"""

    @property
    @abstractmethod
    def linear_velocity_correction(self) -> int:
        """Возвращает величину коррекции линейной скорости движения"""
