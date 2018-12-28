#!/usr/bin/env python3.7

from pkg_resources import resource_filename
from log_analyser.common.configuration.config import Config


class __LogParserConfig(Config):
    """
    Log parser configuration wrapper
    """

    _identifier = __name__

    _file_path = resource_filename(__name__, "config.yaml")

    def file_access_mode(self) -> str:
        return self.get_property("file_access_mode")

    def default_sleep(self) -> float:
        return self.get_property("default_sleep")

    def max_sleep(self) -> float:
        return self.get_property("max_sleep")

    def processes(self) -> int:
        return self.get_property("processes")


LogParserConfig = __LogParserConfig()
