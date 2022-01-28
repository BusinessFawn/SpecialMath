from tests.test_utils.utils import *

# + special math with input of 7
def test_special_math_7(client) -> None:
    res = client.get('specialmath/7')
    assert res.status_code == 200
    assert res.is_json == True
    root_response = res.json
    evaluate_root_keys(root_response)
    context = root_response['context']
    evaluate_context_keys(context)
    evaluate_request_time(context['request-time'])
    response = root_response['response']
    evaluate_success_keys(response)
    assert response['special-calculation'] == 79


# + special math with input of 17
def test_special_math_17(client) -> None:
    res = client.get('specialmath/7')
    assert res.status_code == 200
    assert res.is_json == True
    root_response = res.json
    evaluate_root_keys(root_response)
    context = root_response['context']
    evaluate_context_keys(context)
    evaluate_request_time(context['request-time'])
    response = root_response['response']
    evaluate_success_keys(response)
    assert response['special-calculation'] == 79


# + special math with input of 90
def test_special_math_90(client) -> None:
    res = client.get('specialmath/90')
    assert res.status_code == 200
    assert res.is_json == True
    root_response = res.json
    evaluate_root_keys(root_response)
    context = root_response['context']
    evaluate_context_keys(context)
    evaluate_request_time(context['request-time'])
    response = root_response['response']
    evaluate_success_keys(response)
    assert response['special-calculation'] == 19740274219868223074


# - special math input value too high
def test_special_math_input_too_high(client) -> None:
    res = client.get('specialmath/10000')
    assert res.status_code == 400
    assert res.is_json == True
    response = res.json
    evaluate_root_keys(response, is_error=True)
    context = response['context']
    evaluate_context_keys(context)
    error = response['error']
    evaluate_error_keys(error)
    assert isinstance(error['message'], str)
    assert 'Invalid special math request: request 10000 exceeds maximum value of 1000' in error['message']
    assert error['name'] == 'InvalidRequestParameter'


# - special math with invalid input type
def test_special_math_invalid_input(client) -> None:
    res = client.get('specialmath/error')
    assert res.status_code == 404
    assert res.is_json == True
    response = res.json
    evaluate_root_keys(response, is_error=True)
    context = response['context']
    evaluate_context_keys(context)
    error = response['error']
    evaluate_error_keys(error)
    assert isinstance(error['message'], str)
    assert 'The requested URL was not found on the server.' in error['message']
    assert error['name'] == 'NotFound'


# - special math with server error
def test_special_math_server_error(client, mocked_special_calc) -> None:
    res = client.get('specialmath/1')
    assert res.status_code == 500
    assert res.is_json == True
    response = res.json
    evaluate_root_keys(response, is_error=True)
    context = response['context']
    evaluate_context_keys(context)
    error = response['error']
    evaluate_error_keys(error)
    assert isinstance(error['message'], str)
    assert 'Unexpected error encountered. Please retry your request. If this error ' \
           'persists reach out to John because he did something wrong.' in error['message']
    assert error['name'] == 'InternalServerError'

