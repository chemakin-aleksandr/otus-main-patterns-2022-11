from abc import ABC, abstractmethod


class FuelBurner(ABC):
    """Объект, обладающий свойством изменения уровня топлива."""

    @property
    @abstractmethod
    def fuel_level(self) -> int:
        """Уровень топлива."""

    @fuel_level.setter
    @abstractmethod
    def fuel_level(self, value: int) -> None:
        """Уровень топлива."""

    @property
    @abstractmethod
    def fuel_consumption(self) -> int:
        """Расход топлива."""
