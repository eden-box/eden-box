#!/usr/bin/env python3.7

from .entry_creator import _EntryCreator as EntryCreator
from .entry_types import FileRenamedEntry


class FileRenamedEntryCreator(EntryCreator):
    """
    Creates objects representing File Renames
    """

    _identifier = "File renamed"

    def _return_entry(self, file, json_line):
        return FileRenamedEntry(file, json_line)
