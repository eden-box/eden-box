#!/usr/bin/env python3.7

from pkg_resources import resource_filename
from log_analyser.common.configuration.config import Config


class LogFilterConfig(Config):
    """
    Log filter configuration wrapper
    """

    _file_path = resource_filename(__name__, "config.yaml")

    @property
    def max_default_priority_queue_size(self):
        return self.get_property("max_default_priority_queue_size")

    @property
    def max_high_priority_queue_size(self):
        return self.get_property("max_high_priority_queue_size")

    @property
    def process_interval(self):
        return self.get_property("process_interval")
