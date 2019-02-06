#!/usr/bin/env python3.7

from .default_activity import _DefaultActivity


class FileDefaultActivity(_DefaultActivity):
    """
    Generated when no file entry is identified
    """

    def dispatch(self, db_cursor):
        return
