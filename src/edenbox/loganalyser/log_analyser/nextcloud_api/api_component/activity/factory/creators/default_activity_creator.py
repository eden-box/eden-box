#!/usr/bin/env python3.7

from .activity_creator import _ActivityCreator
from .activity_types import NullActivity


class DefaultActivityCreator(_ActivityCreator):
    """
    Default Entry Creator
    Returns no object, used for xml objects which do not match with other creators
    """

    _identifier = "default"

    def _return_activity(self, activity_id, timestamp, file, xml_dict):
        return NullActivity(activity_id, timestamp, file, xml_dict)
