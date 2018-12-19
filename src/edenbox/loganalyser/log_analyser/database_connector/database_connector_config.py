#!/usr/bin/env python3.7

from pkg_resources import resource_filename
from log_analyser.common.configuration.config import Config


class DatabaseConnectorConfig(Config):
    """
    Database connector configuration wrapper
    """

    _file_path = resource_filename(__name__, "config.yaml")

    @property
    def max_workers(self):
        return self.get_property("max_workers")

    @property
    def min_connections(self):
        return self.get_property("min_connections")

    @property
    def max_connections(self):
        return self.get_property("max_connections")

    @property
    def host(self):
        return self.get_property("host")

    @property
    def port(self):
        return self.get_property("port")

    @property
    def database(self):
        return self.get_property("database")

    @property
    def user(self):
        return self.get_property("user")

    @property
    def ssl_mode(self):
        return self.get_property("ssl_mode")

    @property
    def timeout(self):
        return self.get_property("timeout")
