#!/usr/bin/env python3.7

import re
from .prioritary_entry import _PrioritaryEntry as PrioritaryEntry


class FileRenamedEntry(PrioritaryEntry):
    """
    Generated when a file is renamed
    """

    __procedure = "file_renamed"

    def _process_operation(self, operation):
        args = re.match(r'(.*) to "(.*)"', operation, re.M)
        self.old_file = args.group(1)
        self.new_file = args.group(2)

    def dispatch(self, db_cursor):
        db_cursor.callproc(self.__procedure, (self.old_file, self.new_file, self.time))
