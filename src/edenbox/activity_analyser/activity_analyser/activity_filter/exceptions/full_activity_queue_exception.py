#!/usr/bin/env python3.7

from .activity_filter_exception import ActivityFilterException


class FullActivityQueueException(ActivityFilterException):
    """
    Exception raised when an activity is added to a full activity queue
    """
    pass
