#!/usr/bin/env python3.7

from .activity_api_exception import ActivityApiException


class NotFoundException(ActivityApiException):
    """
    Exception raised when the filter is unknown
    """
    pass
