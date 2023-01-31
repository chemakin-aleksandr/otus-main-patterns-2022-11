from space_invaders.engine.errors import exceptions
from space_invaders.engine.interfaces import Command, FuelBurner


class BurnFuel(Command):
    """Выполнить изменение уровня топлива.

    Args:
        obj: Объект, для которого выполняется изменение уровня топлива.
    """

    def __init__(self, obj: FuelBurner):
        self.obj = obj

    def execute(self) -> None:
        """Выполнить действие.

        Raises:
            NegativeFuelLevelError.
        """
        new_fuel_level = self.obj.fuel_level - self.obj.fuel_consumption
        if new_fuel_level < 0:
            raise exceptions.NegativeFuelLevelError
        self.obj.fuel_level = new_fuel_level
