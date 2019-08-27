#! usr/bin/env python3.7

from typing import List
from .creators.activity_types import Activity


class Activities:

    """Most recent activity received"""
    first = None

    """Oldest activity received"""
    last = None

    """List of activities"""
    activities = List[Activity]

    def __init__(self, activities, last, first=None):

        self.first = first

        self.last = last

        self.activities = activities

    def filter(self, id_limit):
        """
        Keep activities with id superior to id_limit
        :param id_limit: filtering parameter
        :return: object after activities have been filtered
        """

        self.activities = [activity for activity in self.activities if activity.id > id_limit]

        return self

    def merge_activities(self, activities_list):
        """
        Merge several Activities
        :param activities_list: list of Activities
        :return: concatenation of all Activities
        """

        if activities_list:

            self.last = activities_list[-1].last

            for activity in activities_list:
                self.activities.extend(activity.activities)
