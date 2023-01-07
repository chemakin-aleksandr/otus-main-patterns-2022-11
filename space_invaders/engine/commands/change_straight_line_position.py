from space_invaders.engine import exceptions
from space_invaders.engine.interfaces import Command
from space_invaders.engine.interfaces import MoveController
import operator


class Move(Command):
    """Команда прямолинейного движения"""

    def __init__(self, obj: MoveController):
        self._obj = obj

    def execute(self) -> None:
        if None in [self._obj.position, self._obj.velocity]:
            raise exceptions.ENoneMoveError

        if None in self._obj.position + self._obj.velocity:
            raise exceptions.ENoneMoveError

        self._obj.position = \
            tuple(map(operator.add, self._obj.position,
                      self._obj.velocity))
