from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass
class Vector:
    x: int
    y: int

    def add(self, vec: "Vector") -> "Vector":
        return Vector(self.x + vec.x, self.y + vec.y)


class Movable(ABC):
    """ Movable interface"""

    @property
    @abstractmethod
    def position(self) -> Vector:
        """
        get position
        :return: Vector
        """
        ...

    @position.setter
    @abstractmethod
    def position(self, v: Vector) -> None:
        """
        set position
        :return: Vector
        """
        ...

    @property
    @abstractmethod
    def velocity(self) -> Vector:
        """
        get velocity
        :return: Vector velocity
        """
        ...

    @velocity.setter
    @abstractmethod
    def velocity(self, value: Vector) -> None:
        """
        setter velocity
        :value: Vector
        :return: None
        """
        ...
