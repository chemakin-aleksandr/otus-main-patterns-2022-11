from space_invaders.engine import exceptions
from space_invaders.engine.interfaces import AngularVelocityController, Command


class ChangeAngularVelocity(Command):
    """Команда изменения угловой скорости"""

    def __init__(self, obj: AngularVelocityController):
        self._obj = obj

    def execute(self) -> None:
        velocity = self._obj.angular_velocity + self._obj.angular_velocity_correction
        if velocity < 0:
            raise exceptions.NegativeAngularVelocityError
        self._obj.angular_velocity = velocity
