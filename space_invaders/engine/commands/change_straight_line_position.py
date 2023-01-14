import operator

from space_invaders.engine import exceptions
from space_invaders.engine.interfaces import Command, MoveController


class Move(Command):
    """Команда прямолинейного движения"""

    def __init__(self, obj: MoveController):
        self._obj = obj

    def execute(self) -> None:
        if self._obj.position is None or any(map(lambda elem: elem is None, self._obj.position)):
            raise exceptions.EGetPositionError

        if self._obj.velocity is None or any(map(lambda elem: elem is None, self._obj.velocity)):
            raise exceptions.EGetVelocityError

        self._obj.position = tuple(map(operator.add, self._obj.position, self._obj.velocity))
