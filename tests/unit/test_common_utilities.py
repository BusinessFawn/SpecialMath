from special_math.common_utilities import SpecialMathCalc, RequestUtils
from tests.test_utils.utils import DATETIME_FORMAT
from datetime import datetime
import pytest


def test_calc_init():
    mock_calculator = SpecialMathCalc()
    assert mock_calculator is not None
    assert mock_calculator.special_cache is not None


def test_calculate_special_value_7():
    mock_calculator = SpecialMathCalc()
    assert mock_calculator.calculate_special_value(7) == 79


def test_calculate_special_value_17():
    mock_calculator = SpecialMathCalc()
    assert mock_calculator.calculate_special_value(17) == 10926


def test_calculate_special_value_90():
    mock_calculator = SpecialMathCalc()
    assert mock_calculator.calculate_special_value(90) == 19740274219868223074


def test_calculate_special_value_failure():
    mock_calculator = SpecialMathCalc()
    try:
        mock_calculator.calculate_special_value(200000)
    except RecursionError as e:
        assert 'maximum recursion depth exceeded in comparison' in e.args


def test_request_utils_init():
    request_utils = RequestUtils()
    assert request_utils is not None


def test_get_context():
    context_keys = ['request-id', 'request-time']
    context = RequestUtils().get_request_context()
    for key in context_keys:
        assert key in context
    try:
        datetime.strptime(context['request-time'], DATETIME_FORMAT)
    except ValueError as ve:
        pytest.fail(f"Incorrect data format, should be {DATETIME_FORMAT}: {ve}")
    except Exception as e:
        pytest.fail(f"Unknown exception evaluating datetime format: {e}")

