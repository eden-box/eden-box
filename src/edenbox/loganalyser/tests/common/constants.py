#!/usr/bin/env python3.7

from log_analyser.log_filter.log_filter_config import LogFilterConfig


class Constants:

    def max_default_entries(self):
        """
        TODO
        """
        return LogFilterConfig.max_default_priority_queue_size()

    def max_high_entries(self):
        """
        TODO
        """
        return LogFilterConfig.max_high_priority_queue_size()
