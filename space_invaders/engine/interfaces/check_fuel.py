from abc import ABC, abstractmethod


class Fuelable(ABC):
    """ Fuel interface"""

    @property
    @abstractmethod
    def fuel(self) -> int:
        """ getter for fuel """
        ...

    @fuel.setter
    @abstractmethod
    def fuel(self, value: int) -> None:
        """ setter for fuel """
        ...

    @property
    @abstractmethod
    def fuel_rate(self) -> int:
        """ fuel rate per move """
        ...
