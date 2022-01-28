import os
import logging
from uuid import uuid4
from datetime import datetime


logger = logging.getLogger(__name__)
logger.setLevel(os.getenv("LOG_LEVEL", logging.DEBUG))

# TODO: TechDebt: Place in constants package
DATETIME_FORMAT = '%Y-%m-%dT%H:%M:%SZ'


class SpecialMathCalc:
    """
    An instance of the special math calculator
    """
    special_cache = None

    def __init__(self):
        self.special_cache = {}

    def calculate_special_value(self, n: int) -> int:
        """
        Calculates a number from the given input n
        :param n: The number to run the special algorithm on
        :return: The calculation of n, it is special
        """

        if n in self.special_cache:
            return self.special_cache[n]
        if n <= 1:
            return n

        special_number = n + self.calculate_special_value(n - 1) + self.calculate_special_value(n - 2)

        self.special_cache[n] = special_number

        return special_number


# TODO: TechDebt: Move this func and utils package to stand alone to avoid duplication
class RequestUtils:
    """
    Utility for the client request
    """

    def __init__(self):
        self.request_time = datetime.utcnow()
        self.request_timestamp = self.request_time.strftime(DATETIME_FORMAT)
        self.request_id = uuid4()

    def get_request_context(self) -> dict:
        """
        Get the request context members, such as a unique id and the request-time to pass back to the client for their
        records
        :return: A dictionary with the context of the request
        """
        return {
            "request-id": self.request_id,
            "request-time": self.request_timestamp
        }
