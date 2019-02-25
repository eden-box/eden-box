#!/usr/bin/env python3.7

import abc
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

    def __init__(self):

        self.raw_config = self.load_config(self._file_path)

        ConfigManager().register(self._identifier, self)

    @property
    @abc.abstractmethod
    def _identifier(self):
        """
        Configuration identifier
        """
        pass

    @property
    @abc.abstractmethod
    def _file_path(self):
        """
        Path of the configuration file
        """
        pass

    @staticmethod
    def load_config(file_path):
        """
        Load configuration from a file
        :param file_path: path of the file to load
        :return: configuration dict
        """
        return get_config(file_path)

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
