#!/usr/bin/env python3.7

import abc
from pkg_resources import resource_filename
from .loader import get_config
from .config_manager import ConfigManager


class Config:
    """
    Configuration wrapper
    """

    """current type of configuration, defined by ConfigManager"""
    __config_type = None

    """configuration contents"""
    __config = None

    """default config file name"""
    __default_config = "config.yaml"

    """application custom config file name"""
    __app_config = "app_config.yaml"

    def __init__(self):

        self.raw_config = self.load_config()

        ConfigManager().register(self._identifier, self)

    @property
    @abc.abstractmethod
    def _identifier(self):
        """
        Configuration identifier
        """
        pass

    @staticmethod
    def __load_config_from_file(path, file_name):
        """
        Load configuration from a file
        :param path: path to the file directory
        :param file_name: file name
        :return: configuration dict
        """
        try:
            file_path = resource_filename(path, file_name)
        except ImportError:
            return {}

        return get_config(file_path)

    def load_config(self):
        """
        Load configuration
        Loads the default configuration from a file and tries to
        merge it with custom application configuration
        :return: configuration dict
        """
        config = self.__load_config_from_file(self._identifier, self.__default_config)

        app_config = self.__load_config_from_file(self._identifier, self.__app_config)

        if app_config:
            config.update(app_config)

        return config

    def set_config_type(self, config_type):
        """
        Set type of configuration
        :param config_type: type of configuration to set
        """
        self.__config_type = config_type
        self.__config = self.raw_config.get(config_type)

    def get_property(self, property_name):
        """
        Get a configuration property
        :param property_name:
        :return: requested property or None, if it does not exist
        """
        return self.__config.get(property_name)  # returns None if entry does not exist
