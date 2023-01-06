import pytest
from space_invaders.engine import exceptions
from space_invaders.engine.interfaces import StraightLinePositionController
from space_invaders.engine.commands.change_straight_line_position import ChangeStraightLinePosition

class MockStraightLinePositionController(StraightLinePositionController):
    def __init__(self, current_position: [int,int], position_correction: [int,int]):
        self._moveable = True
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

    @property
    def moveable(self) -> bool:
        return self._moveable

    @moveable.setter
    def moveable(self, value: bool) -> None:
        self._moveable = value


@pytest.mark.parametrize(
    ("current_position", "position_correction", "expected_exception"),
    (
            ((3, 4), None, exceptions.ENoneStraightLinePositionError),
            (None, (3, 4), exceptions.ENoneStraightLinePositionError),
            ((1, 2), (1, None), exceptions.ENoneStraightLinePositionError),
            ((1, 2), (None, 2), exceptions.ENoneStraightLinePositionError),
            ((None, 4), (3, 4), exceptions.ENoneStraightLinePositionError),
            ((3, None), (3, 4), exceptions.ENoneStraightLinePositionError),
    ),
)

def test_pos_none(current_position, position_correction, expected_exception):
    obj = MockStraightLinePositionController(current_position=current_position, position_correction=position_correction)
    with pytest.raises(expected_exception):
        ChangeStraightLinePosition(obj).execute()


@pytest.mark.parametrize(
    ("current_position", "position_correction", "expected_exception"),
    (
            ((3, 4), (1, 2), exceptions.EObjectNotMoveableError),
    ),
)

def test_change_stable(current_position, position_correction, expected_exception):
    obj = MockStraightLinePositionController(current_position=current_position, position_correction=position_correction)
    obj.moveable = False
    with pytest.raises(expected_exception):
        ChangeStraightLinePosition(obj).execute()


@pytest.mark.parametrize(
    ("current_position", "position_correction", "expected_position"),
    (
            ((12,5), (-7,3), (5,8)),
            ((3,5), (7,-7), (10,-2)),
            ((-3, -5), (7, -7), (4, -12)),
            ((0, 0), (7, 13), (7, 13)),
    ),
)


def test_change_straight_line_position(current_position, position_correction, expected_position):
    obj = MockStraightLinePositionController(current_position=current_position, position_correction=position_correction)
    ChangeStraightLinePosition(obj).execute()
    assert obj.current_position == expected_position


