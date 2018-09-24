#!/usr/bin/env python3.7

import abc


class _EntryCreator(metaclass=abc.ABCMeta):
    """
    Creates entry objects depending on the provided json entry
    """

    @property
    @abc.abstractmethod
    def _identifier(self):
        """
        Identifies the create objects, correspondent to json entry representation
        """
        raise NotImplementedError

    def register(self, entry_factory):
        """
        Register this creator in a given factory
        :param entry_factory: entry factory
        """
        entry_factory.register(self._identifier, self)

    def create(self, file, json_line):
        """
        Create entry object
        :param file: file to which the action refers to
        :param json_line: json entry from the log file
        :return: entry object
        """
        return self._return_entry(file, json_line)

    @abc.abstractmethod
    def _return_entry(self, file, json_line):
        """
        Returns entry object of a specific type
        :param file: file to which the action refers to
        :param json_line: json entry from the log file
        :return: entry object
        """
        pass
