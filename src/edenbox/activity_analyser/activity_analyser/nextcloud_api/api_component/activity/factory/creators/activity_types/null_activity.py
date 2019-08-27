#!/usr/bin/env python3.7

from .activity import Activity


class NullActivity(Activity):
    """
    Generated when an activity should not be processed
    """

    __procedure = "null_activity"

    def dispatch(self, db_cursor):
        return
