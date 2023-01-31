from space_invaders.engine.interfaces import Command
from space_invaders.engine.interfaces.move import Movable


class Move(Command):
    def __init__(self, m: Movable):
        self._m = m

    def execute(self) -> None:
        self._m.position = self._m.position.add(self._m.velocity)
