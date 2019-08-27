#!/usr/bin/env python3.7

from activity_analyser.common.configuration.config import Config


class ActivityFilterConfig(Config):
    """
    Activity filter configuration wrapper
    """

    _identifier = __name__

    _config_section = "activity_filter"

    def max_queue_size(self) -> int:
        return self.get_property("max_queue_size")

    def process_interval(self) -> float:
        return self.get_property("process_interval")
