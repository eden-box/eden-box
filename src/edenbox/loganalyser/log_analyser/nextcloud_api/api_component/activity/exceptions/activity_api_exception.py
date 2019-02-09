#!/usr/bin/env python3.7


class ActivityApiException(Exception):
    """
    Exception raised by Activity Api
    """

    def __init__(self, error, message=None):
        # Call the base class constructor with the needed parameters
        super().__init__(message)

        self.error = error
