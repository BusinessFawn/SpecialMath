import os
from special_math.common_utilities import SpecialMathCalc, RequestUtils
from special_math import MAX_SPECIAL_NUMBER_ENTRY
import logging

from flask import Blueprint

bp = Blueprint('specialmath', __name__, url_prefix='/specialmath')

logger = logging.getLogger(__name__)
logger.setLevel(os.getenv("LOG_LEVEL", logging.DEBUG))

special_calculator = SpecialMathCalc()


@bp.route('/<int:n>')
def special_math(n: int):
    """
    Takes an integer input and computes the special value for that number
    :param n: The path value given to calculate the special value from
    :return: a dict with context and response and a status code
    """

    request_context = RequestUtils().get_request_context()

    logger.debug(f'Received request for {n}, request_id: {request_context["request-id"]}')
    if n > MAX_SPECIAL_NUMBER_ENTRY:
        return {'context': request_context, 'error': {'message': f'Invalid special math request: request '
                                                                 f'{n} exceeds maximum value of '
                                                                 f'{MAX_SPECIAL_NUMBER_ENTRY}',
                                                      'name': 'InvalidRequestParameter'}}, 400
    try:
        special_number = special_calculator.calculate_special_value(n)
    except Exception as e:
        logger.error("Experienced error attempting to calculate special number")
        logger.critical(e)
        return {'context': request_context, 'error': {'message': 'Unexpected error encountered. '
                                                                 'Please retry your request. If this error persists '
                                                                 'reach out to John because he did something wrong.',
                                                      'name': 'InternalServerError'}}, 500
    logger.debug(f'Calculated special number: {special_number}')

    response = {"context": request_context,
                "response": {
                    "special-calculation": special_number
                }
                }

    logger.info(f"Successfully processed request {n}: {response}")
    return response
