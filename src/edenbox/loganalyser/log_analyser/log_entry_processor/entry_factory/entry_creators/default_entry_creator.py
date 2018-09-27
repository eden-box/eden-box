#!/usr/bin/env python3.7

from .entry_creator import _EntryCreator as EntryCreator


class DefaultEntryCreator(EntryCreator):
    """
    Default Entry Creator
    Returns no object, used for json entries which do not match with other creators
    """

    _identifier = "Default"

    def _return_entry(self, file, json_line):
        pass
