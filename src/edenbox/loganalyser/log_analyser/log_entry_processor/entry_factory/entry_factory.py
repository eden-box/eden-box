#!/usr/bin/env python3.7

import re
from log_analyser.common import Singleton


class EntryFactory(metaclass=Singleton):
    """
    Transforms log lines to the correspondent object type

    Converts json log entries to usable objects, depending on the available set of entry creators
    """

    def __init__(self):

        self._entry_creators = {}

        # Initialize available entry creators
        for creator in (
            # TODO add creators
        ):
            creator.register(self)

        # self.__default_entry_creator = DefaultEntryCreator()  # used if no matching creator is found

    def register(self, entry_creator_id, entry_creator):
        """
        Register a entry creator to the factory
        :param entry_creator_id: id of the added creator
        :param entry_creator: creator to add
        """
        self._entry_creators[entry_creator_id] = entry_creator

    def get_entry(self, json_line):
        """
        Convert json line to correspondent object
        :param json_line: json object of the log entry
        :return: created entry object
        """
        args = re.match(r'(.*): "(.*)" .*', json_line.message, re.M)  # TODO parse it in another way, maybe

        # action = args.group(1)
        # file = args.group(2)

        return self._entry_creators.get(args.group(1), self.__default_entry_creator).create(args.group(2), json_line)
