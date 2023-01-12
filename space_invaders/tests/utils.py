from unittest.mock import Mock


def build_mock_object(cls, **attributes):
    mock = Mock(cls)
    for attribute, value in attributes.items():
        setattr(mock, attribute, value)
    return mock
