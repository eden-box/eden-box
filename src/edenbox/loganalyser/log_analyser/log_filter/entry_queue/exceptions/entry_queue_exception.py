#!/usr/bin/env python3.7


class EntryQueueException(Exception):
    """
    Exception raised by Entry Queue
    """

    def __init__(self, error, message=None):
        # Call the base class constructor with the needed parameters
        super().__init__(message)

        self.error = error
