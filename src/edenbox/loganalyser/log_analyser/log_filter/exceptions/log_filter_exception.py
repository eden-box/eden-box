#!/usr/bin/env python3.7


class LogFilterException(Exception):
    """
    Exception raised by Log Filter
    """

    def __init__(self, error, message=None):
        # Call the base class constructor with the needed parameters
        super().__init__(message)

        self.error = error
