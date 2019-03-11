#!/usr/bin/env python3.7

from activity_analyser.common.configuration.config import Config


class __LoggerConfig(Config):
    """
    Logger configuration wrapper
    """

    _identifier = __name__

    def logging_config(self) -> str:
        return self.get_property("log_config")


LoggerConfig = __LoggerConfig()
