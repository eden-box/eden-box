#!/usr/bin/env python3.7

from pkg_resources import resource_filename
from log_analyser.common.configuration.config import Config


class LogParserConfig(Config):
    """
    Log parser configuration wrapper
    """

    _file_path = resource_filename(__name__, "config.yaml")

    @property
    def file_access_mode(self):
        return self.get_property("file_access_mode")

    @property
    def default_sleep(self):
        return self.get_property("default_sleep")

    @property
    def max_sleep(self):
        return self.get_property("max_sleep")

    @property
    def processes(self):
        return self.get_property("processes")
