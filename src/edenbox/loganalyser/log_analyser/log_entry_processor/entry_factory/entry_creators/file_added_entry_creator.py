#!/usr/bin/env python3.7

from .entry_creator import _EntryCreator as EntryCreator
from .entry_types import FileAddedEntry


class FileAddedEntryCreator(EntryCreator):
    """
    Creates objects representing Added Files
    """

    _identifier = "File created"

    def _return_entry(self, file, json_line):
        return FileAddedEntry(file, json_line)
