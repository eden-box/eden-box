#!/usr/bin/env python3.7

from pkg_resources import resource_filename
from log_analyser.common.configuration.config import Config


class __LoggerConfig(Config):
    """
    Logger configuration wrapper
    """

    _identifier = __name__

    _file_path = resource_filename(__name__, "config.yaml")

    def logging_config(self) -> str:
        return self.get_property("log_config")


LoggerConfig = __LoggerConfig()
