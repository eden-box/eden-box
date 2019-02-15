#!/usr/bin/env python3.7

from .activity_creator import _ActivityCreator
from .activity_types import FileRemovedActivity


class FileRemovedActivityCreator(_ActivityCreator):
    """
    Creates objects representing File Removals
    """

    _identifier = "file_deleted"

    def _return_activity(self, activity_id, timestamp, file, xml_dict):
        return FileRemovedActivity(activity_id, timestamp, file, xml_dict)
