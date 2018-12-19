#!/usr/bin/env python3.7

from pkg_resources import resource_filename
from log_analyser.common.configuration.config import Config


class LogAnalyserConfig(Config):
    """
    Log Analyser configuration wrapper
    """

    _file_path = resource_filename(__name__, "config.yaml")

    @property
    def logging_file(self):
        return self.get_property("logging_file")
