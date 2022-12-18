import pytest

from space_invaders.engine import exceptions
from space_invaders.engine.commands import BurnFuel
from space_invaders.engine.interfaces import FuelBurner


class MockFuelBurner(FuelBurner):

    def __init__(self, fuel_level: int, fuel_consumption: int):
        self._fuel_level = fuel_level
        self._fuel_consumption = fuel_consumption

    @property
    def fuel_level(self) -> int:
        return self._fuel_level

    @fuel_level.setter
    def fuel_level(self, value: int) -> None:
        self._fuel_level = value

    @property
    def fuel_consumption(self) -> int:
        return self._fuel_consumption


@pytest.mark.parametrize("fuel_level, fuel_consumption, expected_fuel_level", (
    (10, 1, 9),
    (10, -1, 11),
    (10, 10, 0),
))
def test_burn_fuel_positive(fuel_level, fuel_consumption, expected_fuel_level):
    obj = MockFuelBurner(fuel_level=fuel_level, fuel_consumption=fuel_consumption)
    BurnFuel(obj).execute()
    assert obj.fuel_level == expected_fuel_level


@pytest.mark.parametrize("fuel_level, fuel_consumption, expected_exception", (
    (1, 10, exceptions.NegativeFuelLevelError),
    (0, 1, exceptions.NegativeFuelLevelError),
))
def test_burn_fuel_negative(fuel_level, fuel_consumption, expected_exception):
    obj = MockFuelBurner(fuel_level=fuel_level, fuel_consumption=fuel_consumption)
    with pytest.raises(expected_exception):
        BurnFuel(obj).execute()
