#!/usr/bin/env python3.7

from pkg_resources import resource_filename
from log_analyser.common.configuration.config import Config


class __LogFilterConfig(Config):
    """
    Log filter configuration wrapper
    """

    _identifier = __name__

    _file_path = resource_filename(__name__, "config.yaml")

    def max_default_priority_queue_size(self) -> int:
        return self.get_property("max_default_priority_queue_size")

    def max_high_priority_queue_size(self) -> int:
        return self.get_property("max_high_priority_queue_size")

    def process_interval(self) -> float:
        return self.get_property("process_interval")


LogFilterConfig = __LogFilterConfig()
