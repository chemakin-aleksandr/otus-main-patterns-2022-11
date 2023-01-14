import pytest

from space_invaders.engine import exceptions
from space_invaders.engine.commands.change_linear_velocity import ChangeLinearVelocity
from space_invaders.engine.interfaces.linear_velocity_controller import LinearVelocityController


class MockLinearVelocityController(LinearVelocityController):
    def __init__(self, velocity: int, correction: int):
        self._velocity = velocity
        self._velocity_correction = correction

    @property
    def linear_velocity(self) -> int:
        return self._velocity

    @linear_velocity.setter
    def linear_velocity(self, value: int) -> None:
        self._velocity = value

    @property
    def linear_velocity_correction(self) -> int:
        return self._velocity_correction


@pytest.mark.parametrize(
    ('velocity', 'correction', 'expected_velocity'),
    [
        (250, 11, 261),
        (300, -100, 200),
        (111, 0, 111),
    ],
)
def test_change_linear_velocity(velocity, correction, expected_velocity):
    obj = MockLinearVelocityController(velocity=velocity, correction=correction)
    ChangeLinearVelocity(obj).execute()
    assert obj.linear_velocity == expected_velocity


@pytest.mark.parametrize(
    ('velocity', 'correction', 'expected_exception'),
    [
        (20, -22, exceptions.NegativeLinearVelocityError),
        (0, -1, exceptions.NegativeLinearVelocityError),
    ],
)
def test_velocity_negative(velocity, correction, expected_exception):
    obj = MockLinearVelocityController(velocity=velocity, correction=correction)
    with pytest.raises(expected_exception):
        ChangeLinearVelocity(obj).execute()
