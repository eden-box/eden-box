#!/usr/bin/env python3.7

from log_analyser.log_filter import _Filter as Filter


class NameChangeFilter(Filter):

    def filter(self, log_entry):

        if log_entry:
            return  # TODO prepare way to inform db about name change
