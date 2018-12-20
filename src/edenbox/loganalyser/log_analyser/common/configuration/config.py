#!/usr/bin/env python3.7

import abc
from .loader import get_config


class Config:
    """
    Configuration wrapper
    """

    def __init__(self, test=False):

        config = self.load_config(self._file_path)

        if test:
            self._config = config.get("test")
        else:
            self._config = config.get("app")

    @property
    @abc.abstractmethod
    def _file_path(self):
        pass

    @staticmethod
    def load_config(file_path):
        return get_config(file_path)

    def get_property(self, property_name):
        return self._config.get(property_name)  # if key does not exist, return None
