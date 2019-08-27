#!/usr/bin/env python3.7

from .entry_queue_exception import ActivityQueueException


class FullQueueException(ActivityQueueException):
    """
    Exception raised when an entry is added to a full queue
    """
    pass
