#!/usr/bin/env python3.7

from pkg_resources import resource_filename
from log_analyser.common.configuration.config import Config


class __DatabaseConnectorConfig(Config):
    """
    Database connector configuration wrapper
    """

    _identifier = __name__

    _file_path = resource_filename(__name__, "config.yaml")

    def max_workers(self) -> int:
        return self.get_property("max_workers")

    def min_connections(self) -> int:
        return self.get_property("min_connections")

    def max_connections(self) -> int:
        return self.get_property("max_connections")

    def host(self) -> str:
        return self.get_property("host")

    def port(self) -> int:
        return self.get_property("port")

    def database(self) -> str:
        return self.get_property("database")

    def user(self) -> str:
        return self.get_property("user")

    def ssl_mode(self) -> str:
        return self.get_property("ssl_mode")

    def timeout(self) -> int:
        return self.get_property("timeout")


DatabaseConnectorConfig = __DatabaseConnectorConfig()
