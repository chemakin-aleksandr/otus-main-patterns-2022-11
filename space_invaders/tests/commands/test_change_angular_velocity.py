import pytest

from space_invaders.engine import exceptions
from space_invaders.engine.commands.change_angular_velocity import ChangeAngularVelocity
from space_invaders.engine.interfaces import AngularVelocityController


class MockAngularVelocityController(AngularVelocityController):
    def __init__(self, velocity: int, correction: int):
        self._velocity = velocity
        self._correction = correction

    @property
    def angular_velocity(self) -> int:
        return self._velocity

    @angular_velocity.setter
    def angular_velocity(self, value: int) -> None:
        self._velocity = value

    @property
    def angular_velocity_correction(self) -> int:
        return self._correction


@pytest.mark.parametrize(
    ('velocity', 'correction', 'expected_velocity'),
    [(3, 5, 8), (0, 2, 2), (6, -2, 4)],
)
def test_change_linear_velocity(velocity, correction, expected_velocity):
    obj = MockAngularVelocityController(velocity=velocity, correction=correction)
    ChangeAngularVelocity(obj).execute()
    assert obj.angular_velocity == expected_velocity


@pytest.mark.parametrize(
    ('velocity', 'correction', 'expected_exception'),
    [(3, -5, exceptions.NegativeAngularVelocityError)],
)
def test_velocity_negative(velocity, correction, expected_exception):
    obj = MockAngularVelocityController(velocity=velocity, correction=correction)
    with pytest.raises(expected_exception):
        ChangeAngularVelocity(obj).execute()
