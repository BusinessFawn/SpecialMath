import pytest
from special_math import create_app


@pytest.fixture
def app():
    mock_app = create_app({
        'TESTING': True
    })

    yield mock_app


@pytest.fixture
def client(app):
    return app.test_client()


@pytest.fixture
def runner(app):
    return app.test_cli_runner()


@pytest.fixture()
def mocked_special_calc(mocker):
    mocker.patch('special_math.common_utilities.SpecialMathCalc.calculate_special_value',
                 side_effect=Exception("GenericException"))
