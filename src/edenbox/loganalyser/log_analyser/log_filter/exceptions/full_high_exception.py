#!/usr/bin/env python3.7

from .log_filter_exception import LogFilterException


class FullHighException(LogFilterException):
    """
    Exception raised when an entry is added to a full High Priority queue
    """
    pass
