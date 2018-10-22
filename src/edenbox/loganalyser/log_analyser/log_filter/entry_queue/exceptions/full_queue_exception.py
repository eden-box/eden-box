#!/usr/bin/env python3.7

from .entry_queue_exception import EntryQueueException


class FullQueueException(EntryQueueException):
    """
    Exception raised when an entry is added to a full queue
    """
    pass
