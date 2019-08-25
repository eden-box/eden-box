#!/usr/bin/env python3.7

from activity_analyser.common.configuration.config import Config


class LoggerConfig(Config):
    """
    Logger configuration wrapper
    """

    _identifier = __name__

    _config_section = "log_config"

    def logging_config(self) -> str:
        return self.get_property("log_config")
