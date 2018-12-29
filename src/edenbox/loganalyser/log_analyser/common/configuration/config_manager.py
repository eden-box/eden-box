#!/usr/bin/env python3.7

from log_analyser.common import Singleton


class ConfigManager(metaclass=Singleton):
    """
    Defines the type of configuration to be used by all configuration objects
    """

    __config_type = None

    __configurations = {}

    def __init__(self):
        self.set_app()

    def __set_config_type(self, config):
        config.set_config_type(self.__config_type)

    def __update_config_type(self, config_type):
        self.__config_type = config_type

        # propagate to all configurations
        for config in self.__configurations.values():
            self.__set_config_type(config)

    def set_app(self):
        self.__update_config_type("app")

    def set_test(self):
        self.__update_config_type("test")

    def register(self, identifier, config):
        self.__configurations[identifier] = config
        self.__set_config_type(config)
