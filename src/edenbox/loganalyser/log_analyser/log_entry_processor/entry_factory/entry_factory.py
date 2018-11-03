#!/usr/bin/env python3.7

import re
from .entry_creators import *
from log_analyser.common import Singleton


class EntryFactory(metaclass=Singleton):
    """
    Transforms log lines to the correspondent object type

    Converts json log entries to usable objects, depending on the available set of entry creators
    """

    def __init__(self):

        self.__matcher = re.compile(r'(.*?): (.*)')

        self._entry_creators = {}

        # Initialize available entry creators

        self.__default_entry_creator = DefaultEntryCreator()  # used if no matching creator is found

        for creator in (
                FileAddedEntryCreator(),
                FileRemovedEntryCreator(),
                FileRenamedEntryCreator(),
                FileModifiedEntryCreator(),
                FileAccessEntryCreator()
        ):
            creator.register(self)

    def register(self, entry_creator_id, entry_creator):
        """
        Register an entry creator to the factory
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
        json_line = json_line.message.replace('\\', '')  # remove all backslashes
        json_line = json_line.replace('"', '', 2)  # remove first 2 "
        args = self.__matcher.match(json_line, re.M)

        if args is None:  # if no match was found
            return None

        # action = args.group(1)
        # operation = args.group(2)

        return self._entry_creators.get(args.group(1), self.__default_entry_creator).create(args.group(2), json_line)
