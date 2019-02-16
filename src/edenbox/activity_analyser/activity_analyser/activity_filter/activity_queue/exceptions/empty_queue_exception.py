#!/usr/bin/env python3.7

from .entry_queue_exception import ActivityQueueException


class EmptyQueueException(ActivityQueueException):
    """
    Exception raised upon attempt to retrieve entry from an empty queue
    """
    pass
