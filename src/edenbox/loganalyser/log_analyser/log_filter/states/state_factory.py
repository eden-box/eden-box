#!/usr/bin/env python3.7

from enum import Enum
from .default_state import DefaultState
from .contingency_state import ContingencyState
from .exceptions import InvalidStateException


class StateType(Enum):
    DEFAULT = 0
    CONTINGENCY = 1


class StateFactory:
    """
    State Factory
    Provides the requested state type
    """

    @staticmethod
    def get_state(state_type, log_filter):
        """
        Provides the request state type, belonging to the provided log_filter

        :param state_type: type of state to provide
        :param log_filter: log_filter to which the state belongs to
        :return: requested state type
        """
        if state_type is StateType.DEFAULT:
            return DefaultState(log_filter)
        elif state_type is StateType.CONTINGENCY:
            return ContingencyState(log_filter)
        else:  # only reached in case of method usage error, exception is not handled by default
            raise InvalidStateException(state_type, "Unable to return state, state type is invalid")
