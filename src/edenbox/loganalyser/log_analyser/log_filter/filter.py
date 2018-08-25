#!/usr/bin/env python3.7

import abc


class _Filter(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def filter(self, entry):
        pass
