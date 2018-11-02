#!/usr/bin/env python3.7

from .entry_creator import _EntryCreator as EntryCreator
from .entry_types import FileRemovedEntry


class FileRemovedEntryCreator(EntryCreator):
    """
    Creates objects representing File Removals
    """

    _identifier = "File deleted"

    def _return_entry(self, operation, json_line):
        return FileRemovedEntry(operation, json_line)
