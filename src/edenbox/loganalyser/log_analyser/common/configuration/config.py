#!/usr/bin/env python3.7

import abc
from .loader import get_config
from .config_manager import ConfigManager


class Config:
    """
    Configuration wrapper
    """

    """ initially defined by ConfigManager """
    __config_type = None

    __config = None

    def __init__(self):

        self.raw_config = self.load_config(self._file_path)

        ConfigManager().register(self._identifier, self)

    @property
    @abc.abstractmethod
    def _identifier(self):
        pass

    @property
    @abc.abstractmethod
    def _file_path(self):
        pass

    @staticmethod
    def load_config(file_path):
        return get_config(file_path)

    def set_config_type(self, config_type):
        self.__config_type = config_type
        self.__config = self.raw_config.get(config_type)

    def get_property(self, property_name):
        return self.__config.get(property_name)  # if key does not exist, return None
