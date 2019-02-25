#!/usr/bin/env python3.7

from pkg_resources import resource_filename
from activity_analyser.common.configuration.config import Config


class __ActivityFilterConfig(Config):
    """
    Activity filter configuration wrapper
    """

    _identifier = __name__

    _file_path = resource_filename(__name__, "config.yaml")

    def max_queue_size(self) -> int:
        return self.get_property("max_queue_size")

    def process_interval(self) -> float:
        return self.get_property("process_interval")


ActivityFilterConfig = __ActivityFilterConfig()
