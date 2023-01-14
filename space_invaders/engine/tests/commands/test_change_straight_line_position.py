import pytest

from space_invaders.engine import exceptions
from space_invaders.engine.commands import Move
from space_invaders.engine.interfaces import MoveController


class MockMoveController(MoveController):
    def __init__(self, position: [int, int], velocity: [int, int]):
        self._position = position
        self._velocity = velocity

    @property
    def position(self) -> [int, int]:
        return self._position

    @position.setter
    def position(self, value: [int, int]) -> None:
        self._position = value

    @property
    def velocity(self) -> [int, int]:
        return self._velocity


@pytest.mark.parametrize(
    ('position', 'velocity', 'expected_exception'),
    [
        ((3, 4), None, exceptions.EGetVelocityError),
        ((1, 2), (1, None), exceptions.EGetVelocityError),
        ((1, 2), (None, 2), exceptions.EGetVelocityError),
        (None, (3, 4), exceptions.EGetPositionError),
        ((None, 4), (3, 4), exceptions.EGetPositionError),
        ((3, None), (3, 4), exceptions.EGetPositionError),
    ],
)
def test_pos_none(position, velocity, expected_exception):
    obj = MockMoveController(position=position, velocity=velocity)
    with pytest.raises(expected_exception):
        Move(obj).execute()


@pytest.mark.parametrize(
    ('position', 'velocity', 'expected_position'),
    [
        ((12, 5), (-7, 3), (5, 8)),
        ((3, 5), (7, -7), (10, -2)),
        ((-3, -5), (7, -7), (4, -12)),
        ((0, 0), (7, 13), (7, 13)),
    ],
)
def test_change_straight_line_position(position, velocity, expected_position):
    obj = MockMoveController(position=position, velocity=velocity)
    Move(obj).execute()
    assert obj.position == expected_position
