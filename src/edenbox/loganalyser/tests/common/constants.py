#!/usr/bin/env python3.7

from log_analyser.log_filter.log_filter_config import LogFilterConfig


class Constants:

    def max_default_entries(self):
        """
        Returns the number of default priority entries required to trigger contingency
        """
        return LogFilterConfig.max_default_priority_queue_size()

    def max_high_entries(self):
        """
        Returns the number of high priority entries required to trigger contingency
        """
        return LogFilterConfig.max_high_priority_queue_size()
