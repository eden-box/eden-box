#!/usr/bin/env python3.7

from .activity_creator import _ActivityCreator
from .activity_types import FileRestoredActivity


class FileRestoredActivityCreator(_ActivityCreator):
    """
    Creates objects representing File Restoration
    """

    _identifier = "file_restored"

    def _return_activity(self, activity_id, timestamp, file, xml_dict):
        return FileRestoredActivity(activity_id, timestamp, file, xml_dict)
