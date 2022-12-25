from abc import ABC, abstractmethod


class AngularVelocityController(ABC):
    """Angular velocity interface."""

    @property
    @abstractmethod
    def angular_velocity(self) -> int:
        """Return current angular velocity"""

    @angular_velocity.setter
    @abstractmethod
    def angular_velocity(self, velocity: int) -> None:
        """Setup angular velocity"""

    @property
    @abstractmethod
    def angular_velocity_correction(self) -> int:
        """Return correction of angular velocity"""
