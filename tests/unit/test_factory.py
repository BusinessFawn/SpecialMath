from special_math import create_app, get_request_context, internal_server_error, not_found_error, bad_request_error
from tests.test_utils.utils import evaluate_context_keys, evaluate_request_time, evaluate_root_keys, evaluate_error_keys
from werkzeug.exceptions import InternalServerError, BadRequest, NotFound


def test_config():
    assert not create_app().testing
    assert create_app({'TESTING': True}).testing


def test_get_context():
    context = get_request_context()
    evaluate_context_keys(context)
    evaluate_request_time(context['request-time'])


def test_internal_server_error():
    err_resp, status_code = internal_server_error(InternalServerError("GenericServerError"))
    assert status_code == 500
    evaluate_root_keys(err_resp, is_error=True)
    context = err_resp['context']
    evaluate_context_keys(context)
    error_response = err_resp['error']
    evaluate_error_keys(error_response)
    assert "GenericServerError" in error_response['message']


def test_generic_bad_request():
    err_resp, status_code = bad_request_error(BadRequest("GenericBadRequest"))
    assert status_code == 400
    evaluate_root_keys(err_resp, is_error=True)
    context = err_resp['context']
    evaluate_context_keys(context)
    error_response = err_resp['error']
    evaluate_error_keys(error_response)
    assert "GenericBadRequest" in error_response['message']


def test_not_found_error():
    err_resp, status_code = not_found_error(NotFound("GenericNotFound"))
    assert status_code == 404
    evaluate_root_keys(err_resp, is_error=True)
    context = err_resp['context']
    evaluate_context_keys(context)
    error_response = err_resp['error']
    evaluate_error_keys(error_response)
    assert "GenericNotFound" in error_response['message']
