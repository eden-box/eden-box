#!/usr/bin/env python3.7

from .entry_creator import _EntryCreator as EntryCreator
from .entry_types import FileModifiedEntry


class FileModifiedEntryCreator(EntryCreator):
    """
    Creates objects representing File Modifications
    """

    _identifier = "File updated"

    def _return_entry(self, operation, json_line):
        return FileModifiedEntry(operation, json_line)
