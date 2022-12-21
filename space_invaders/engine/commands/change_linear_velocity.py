from space_invaders.engine import exceptions
from space_invaders.engine.interfaces import Command, LinearVelocityController


class ChangeLinearVelocity(Command):
    """Команда изменения линейной скорости"""

    def __init__(self, obj: LinearVelocityController) -> None:
        self._obj = obj

    def execute(self) -> None:
        velocity = self._obj.linear_velocity + self._obj.linear_velocity_correction
        if velocity < 0:
            raise exceptions.NegativeLinearVelocityError
        self._obj.linear_velocity = velocity
