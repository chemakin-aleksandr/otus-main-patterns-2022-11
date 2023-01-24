import pytest
from unittest.mock import Mock

from space_invaders.engine import exceptions
from space_invaders.engine.commands.change_linear_velocity import ChangeLinearVelocity
from space_invaders.engine.interfaces.linear_velocity_controller import LinearVelocityController


@pytest.mark.parametrize(
    ('velocity', 'correction', 'expected_velocity'),
    [
        (250, 11, 261),
        (300, -100, 200),
        (111, 0, 111),
    ],
)
def test_change_linear_velocity(velocity, correction, expected_velocity):
    mock = Mock(LinearVelocityController)
    mock.linear_velocity = velocity
    mock.linear_velocity_correction = correction
    ChangeLinearVelocity(mock).execute()
    assert mock.linear_velocity == expected_velocity


@pytest.mark.parametrize(
    ('velocity', 'correction', 'expected_exception'),
    [
        (20, -22, exceptions.NegativeLinearVelocityError),
        (0, -1, exceptions.NegativeLinearVelocityError),
    ],
)
def test_velocity_negative(velocity, correction, expected_exception):
    mock = Mock()
    mock.linear_velocity = velocity
    mock.linear_velocity_correction = correction
    with pytest.raises(expected_exception):
        ChangeLinearVelocity(mock).execute()
