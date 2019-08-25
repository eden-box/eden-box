#!/usr/bin/env python3.7

from activity_analyser.activity_filter.activity_filter_config import ActivityFilterConfig


class Constants:

    @staticmethod
    def dummy_process_interval():
        """
        Returns a dummy value for
        """
        return 5

    @staticmethod
    def max_activities():
        """
        Returns the number of default priority entries required to trigger contingency
        """
        return ActivityFilterConfig().max_queue_size()
