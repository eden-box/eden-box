#!/usr/bin/env python3.7

import abc
from pkgutil import get_data
from pkg_resources import resource_filename
from .loader import get_config


class Config:
    """
    Configuration wrapper
    """

    """configuration contents"""
    _config = None

    """default config file name"""
    __default_config = "config.yaml"

    """application custom config file name"""
    __app_config = "app_config.yaml"

    def __init__(self, config=None):
        self._config = self.load_config(config)

    @property
    @abc.abstractmethod
    def _identifier(self):
        """
        Configuration identifier
        """
        pass

    @property
    @abc.abstractmethod
    def _config_section(self):
        """
        Configuration file section name
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
        resource = get_data(path, file_name) or {}  # get_data returns None if file is not reachable

        if resource:
            return get_config(resource)

        return {}

    def load_config(self, custom_config=None):
        """
        Load configuration
        Loads the default configuration from a file and tries to
        merge it with custom application configuration
        :return: configuration dict
        """
        config = self.__load_config_from_file(self._identifier, self.__default_config)

        if custom_config:
            config[self._config_section].update(custom_config)

        return config

    def get_property(self, property_name):
        """
        Get a configuration property
        :param property_name:
        :return: requested property or None, if it does not exist
        """
        return self._config.get(self._config_section).get(property_name)  # returns None if entry does not exist
