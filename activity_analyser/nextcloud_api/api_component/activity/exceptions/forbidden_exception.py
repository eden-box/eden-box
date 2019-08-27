#!/usr/bin/env python3.7

from .activity_api_exception import ActivityApiException


class ForbiddenException(ActivityApiException):
    """
    Exception raised when the offset activity belongs to a different user or the user is not correctly logged in
    """
    pass
