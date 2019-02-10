#!/usr/bin/env python3.7

from .activity_creator import _ActivityCreator
from .activity_types import FileModifiedActivity, FileRenamedActivity, NullActivity


class FileModifiedActivityCreator(_ActivityCreator):
    """
    Creates objects representing File Modifications
    """

    _identifier = "file_changed"

    def _return_activity(self, activity_id, timestamp, file, xml_dict):
        action = xml_dict["subject_rich"]["element"][0]
        if "changed" in action:
            return FileModifiedActivity(activity_id, timestamp, file, xml_dict)
        elif ("renamed" in action) or ("moved" in action):
            return FileRenamedActivity(activity_id, timestamp, file, xml_dict)
        else:
            return NullActivity(activity_id, timestamp, file, xml_dict)
