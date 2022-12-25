import unittest
from space_invaders.engine.interfaces.angular_velocity import AngularVelocityController
from space_invaders.engine.commands.change_angular_velocity import ChangeAngularVelocity, NegativeAngularVelocityError


class MockAngularVelocityController(AngularVelocityController):
    def __init__(self, velocity: int, correction: int):
        self._velocity = velocity
        self._correction = correction

    @property
    def angular_velocity(self) -> int:
        return self._velocity

    @angular_velocity.setter
    def angular_velocity(self, value: int) -> None:
        self._velocity = value

    @property
    def angular_velocity_correction(self) -> int:
        return self._correction


class TestChangeAngularVelocity(unittest.TestCase):
    def test_exec(self):
        test_cases = [
            (3, 5, 8),
            (0, 2, 2),
            (6, -2, 4)
        ]
        for velocity, correction, expected in test_cases:
            obj = MockAngularVelocityController(velocity, correction)
            ChangeAngularVelocity(obj).execute()
            self.assertEqual(obj.angular_velocity, expected)

    def test_neg_velocity(self):
        with self.assertRaises(NegativeAngularVelocityError):
            obj = MockAngularVelocityController(3, -5)
            ChangeAngularVelocity(obj).execute()


if __name__ == '__main__':
    unittest.main()
