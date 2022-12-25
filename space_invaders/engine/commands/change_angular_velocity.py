from space_invaders.engine.interfaces.command import Command
from space_invaders.engine.interfaces.angular_velocity import AngularVelocityController


class NegativeAngularVelocityError(Exception):
    pass


class ChangeAngularVelocity(Command):

    def __init__(self, obj: AngularVelocityController):
        self._obj = obj

    def execute(self) -> None:
        velocity = self._obj.angular_velocity + self._obj.angular_velocity_correction
        if velocity < 0:
            raise NegativeAngularVelocityError
        self._obj.angular_velocity = velocity
