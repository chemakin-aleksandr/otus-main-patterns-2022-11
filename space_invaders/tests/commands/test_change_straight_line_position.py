import pytest
from space_invaders.engine import exceptions
from space_invaders.engine.interfaces import StraightLinePositionController
from space_invaders.engine.commands.change_straight_line_position import ChangeStraightLinePosition

class MockStraightLinePositionController(StraightLinePositionController):
    def __init__(self, current_position: [int,int], position_correction: [int,int]):
        self._current_position = current_position
        self._position_correction = position_correction

    @property
    def current_position(self) -> [int,int]:
        return self._current_position

    @current_position.setter
    def current_position(self, value: [int,int]) -> None:
        self._current_position = value

    @property
    def position_correction(self) -> [int,int]:
        return self._position_correction

@pytest.mark.parametrize(
    ("current_position", "position_correction", "expected_exception"),
    (
            ((3, 4), None, exceptions.NoneStraightLinePositionError),
            (None, (3, 4), exceptions.NoneStraightLinePositionError),
            ((1, 2), (1, None), exceptions.NoneStraightLinePositionError),
            ((1, 2), (None, 2), exceptions.NoneStraightLinePositionError),
            ((None, 4), (3, 4), exceptions.NoneStraightLinePositionError),
            ((3, None), (3, 4), exceptions.NoneStraightLinePositionError),
    ),
)

def test_pos_none(current_position, position_correction, expected_exception):
    obj = MockStraightLinePositionController(current_position=current_position, position_correction=position_correction)
    with pytest.raises(expected_exception):
        ChangeStraightLinePosition(obj).execute()


@pytest.mark.parametrize(
    ("current_position", "position_correction", "expected_position"),
    (
            ((3,5), (7,-7), (10,-2)),
            ((-3, -5), (7, -7), (4, -12)),
            ((0, 0), (7, 13), (7, 13)),
    ),
)


def test_change_straight_line_position(current_position, position_correction, expected_position):
    obj = MockStraightLinePositionController(current_position=current_position, position_correction=position_correction)
    ChangeStraightLinePosition(obj).execute()
    assert obj.current_position == expected_position


