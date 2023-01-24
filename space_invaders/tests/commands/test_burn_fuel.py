import pytest

from space_invaders.engine import exceptions
from space_invaders.engine.commands import BurnFuel
from space_invaders.engine.interfaces import FuelBurner
from space_invaders.tests.utils import build_mock_object


@pytest.mark.parametrize(
    ('fuel_level', 'fuel_consumption', 'expected_fuel_level'),
    [
        (10, 1, 9),
        (10, -1, 11),
        (10, 10, 0),
    ],
)
def test_burn_fuel_positive(fuel_level, fuel_consumption, expected_fuel_level):
    mock = build_mock_object(FuelBurner, fuel_level=fuel_level, fuel_consumption=fuel_consumption)
    BurnFuel(mock).execute()
    assert mock.fuel_level == expected_fuel_level


@pytest.mark.parametrize(
    ('fuel_level', 'fuel_consumption', 'expected_exception'),
    [
        (1, 10, exceptions.NegativeFuelLevelError),
        (0, 1, exceptions.NegativeFuelLevelError),
    ],
)
def test_burn_fuel_negative(fuel_level, fuel_consumption, expected_exception):
    mock = build_mock_object(FuelBurner, fuel_level=fuel_level, fuel_consumption=fuel_consumption)
    with pytest.raises(expected_exception):
        BurnFuel(mock).execute()
