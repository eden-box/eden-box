#!/usr/bin/env python3.7

from .entry_creator import _EntryCreator as EntryCreator
from .entry_types import FileAccessEntry


class FileAccessEntryCreator(EntryCreator):
    """
    Creates objects representing File Accesses
    """

    _identifier = "File accessed"

    def _return_entry(self, operation, json_line):
        return FileAccessEntry(operation, json_line)
