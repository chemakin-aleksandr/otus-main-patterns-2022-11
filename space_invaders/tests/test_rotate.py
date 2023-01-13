import pytest
from space_invaders.engine.commands import Rotate
from space_invaders.engine.interfaces.rotate import Rotable


class MockObjRotate(Rotable):

    def __init__(self, direction: int, directions_number: int, angular_velocity: int):
        self._direction = direction
        self._directions_number = directions_number
        self._angular_velocity = angular_velocity

    @property
    def direction(self) -> int:
        return self._direction

    @direction.setter
    def direction(self, direction: int) -> None:
        self._direction = direction

    @property
    def directions_number(self) -> int:
        return self._directions_number

    @property
    def angular_velocity(self) -> int:
        return self._angular_velocity


@pytest.mark.parametrize(
    "direction, directions_number, angular_velocity, result_direction",
    [
        (2, 7, 1, 3),
        (3, 5, 3, 6)
    ]
)
def test_success(direction, directions_number, angular_velocity, result_direction):
    rotable_obj = MockObjRotate(
        direction=direction,
        directions_number=directions_number,
        angular_velocity=angular_velocity
    )
    Rotate(rotable_obj).execute()
    assert rotable_obj.direction == result_direction
