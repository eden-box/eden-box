#!/usr/bin/env python3.7

from .activity_creator import _ActivityCreator
from .activity_types import FileAccessActivity


class FileAccessActivityCreator(_ActivityCreator):
    """
    Creates objects representing File Accesses
    """

    _identifier = "public_links"

    def _return_activity(self, activity_id, timestamp, file, xml_dict):
        return FileAccessActivity(activity_id, timestamp, file, xml_dict)
