#!/usr/bin/env python3.7

from .default_activity import _DefaultActivity


class NullActivity(_DefaultActivity):
    """
    Generated when an activity should not be processed
    """

    __procedure = "null_activity"

    def dispatch(self, db_cursor):
        return
