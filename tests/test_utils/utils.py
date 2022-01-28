from datetime import datetime
import pytest

DATETIME_FORMAT = '%Y-%m-%dT%H:%M:%SZ'
DEFAULT_ENCODING = 'UTF-8'
REQUIRED_EXPECTED_ROOT_KEYS = ['context']
CONTEXT_EXPECTED_KEYS = ['request-id', 'request-time']
SUCCESSFUL_EXPECTED_ROOT_KEYS = ['response'] + REQUIRED_EXPECTED_ROOT_KEYS
SUCCESSFUL_EXPECTED_RESPONSE_KEYS = ['special-calculation']
ERROR_EXPECTED_ROOT_KEYS = ['error'] + REQUIRED_EXPECTED_ROOT_KEYS
ERROR_EXPECTED_ERROR_KEYS = ['name', 'message']


# + make sure all root level keys exist, error response or not
def evaluate_root_keys(response: dict, is_error: bool = False) -> None:
    if is_error:
        for key in ERROR_EXPECTED_ROOT_KEYS:
            assert key in response
    else:
        for key in SUCCESSFUL_EXPECTED_ROOT_KEYS:
            assert key in response


# + make sure all expected context keys exist
def evaluate_context_keys(context: dict) -> None:
    for key in CONTEXT_EXPECTED_KEYS:
        assert key in context


# + make sure all the expected keys for a success exist
def evaluate_success_keys(success: dict) -> None:
    for key in SUCCESSFUL_EXPECTED_RESPONSE_KEYS:
        assert key in success


# + make sure all the keys in an error object exist
def evaluate_error_keys(error: dict) -> None:
    for key in ERROR_EXPECTED_ERROR_KEYS:
        assert key in error


# + check the request time format is what its supposed to be
def evaluate_request_time(request_time: str) -> None:
    try:
        datetime.strptime(request_time, DATETIME_FORMAT)
    except ValueError as ve:
        pytest.fail(f"Incorrect data format, should be {DATETIME_FORMAT}: {ve}")
    except Exception as e:
        pytest.fail(f"Unknown exception evaluating datetime format: {e}")