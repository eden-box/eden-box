#!/usr/bin/env python3.7

from activity_analyser.common.configuration.config import Config


class DatabaseConnectorConfig(Config):
    """
    Database connector configuration wrapper
    """

    _identifier = __name__

    _config_section = "database_connector"

    def max_workers(self) -> int:
        return self.get_property("max_workers")

    def min_connections(self) -> int:
        return self.get_property("min_connections")

    def max_connections(self) -> int:
        return self.get_property("max_connections")

    def host(self) -> str:
        return self.get_property("host")

    def host_addr(self) -> str:
        return self.get_property("host_addr")

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
