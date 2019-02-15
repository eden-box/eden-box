#!/usr/bin/env python3.7

from pkg_resources import resource_filename
from activity_analyser.common.configuration.config import Config


class __ActivityAnalyserConfig(Config):
    """
    Log Analyser configuration wrapper
    """

    _identifier = __name__

    _file_path = resource_filename(__name__, "config.yaml")

    def log_file(self):
        return self.get_property("log_file")


ActivityAnalyserConfig = __ActivityAnalyserConfig()
