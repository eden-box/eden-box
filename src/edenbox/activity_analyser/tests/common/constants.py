#!/usr/bin/env python3.7

from activity_analyser.activity_filter.activity_filter_config import ActivityFilterConfig


class Constants:

    def max_activities(self):
        """
        Returns the number of default priority entries required to trigger contingency
        """
        return ActivityFilterConfig.max_queue_size()
