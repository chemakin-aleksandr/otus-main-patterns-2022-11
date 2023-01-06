from space_invaders.engine import exceptions
from space_invaders.engine.interfaces import Command
from space_invaders.engine.interfaces import StraightLinePositionController
import operator


class ChangeStraightLinePosition(Command):
    """Команда прямолинейного движения"""

    def __init__(self, obj: StraightLinePositionController):
        self._obj = obj

    def execute(self) -> None:
        if not self._obj.moveable:
            raise exceptions.EObjectNotMoveableError
        if None in [self._obj.current_position, self._obj.position_correction]:
            raise exceptions.ENoneStraightLinePositionError
        if None in self._obj.current_position + self._obj.position_correction:
            raise exceptions.ENoneStraightLinePositionError
        self._obj.current_position = \
            tuple(map(operator.add, self._obj.current_position, self._obj.position_correction))
