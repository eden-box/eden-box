#!/usr/bin/env python3.7

from .activity_creator import _ActivityCreator
from .activity_types import FileAddedActivity


class FileAddedActivityCreator(_ActivityCreator):
    """
    Creates objects representing Added Files
    """

    _identifier = "file_created"

    def _return_activity(self, activity_id, timestamp, file, xml_dict):
        return FileAddedActivity(activity_id, timestamp, file, xml_dict)
