from space_invaders.engine.interfaces.command import Command
from space_invaders.engine.interfaces.rotate import Rotable


class Rotate(Command):
    """Команда вращения вокруг своей оси"""

    def __init__(self, rotable: Rotable):
        """Инициализация команды вращения"""
        self._rotable = rotable

    def execute(self):
        """Выполнить вращение вокруг своей оси"""
        self._rotable.direction = self._rotable.direction + \
                                  self._rotable.angular_velocity % \
                                  self._rotable.directions_number
