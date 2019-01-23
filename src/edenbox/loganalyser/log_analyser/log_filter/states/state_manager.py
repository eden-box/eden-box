#!/usr/bin/env python3.7

from .state_type import StateType
from .default_state import DefaultState
from .contingency_state import ContingencyState
from .exceptions import InvalidStateException


class StateManager:
    """
    State Manager
    Registers the requested state type
    """

    @staticmethod
    def register_state(state_type, log_filter):
        """
        Registers the requested state type in the provided log_filter

        :param state_type: type of state to register
        :param log_filter: log_filter to which the state belongs to
        :return: registered state type
        """
        if state_type is StateType.DEFAULT:
            return DefaultState(log_filter)
        elif state_type is StateType.CONTINGENCY:
            return ContingencyState(log_filter)
        else:  # only reached in case of method usage error, exception is not handled by default
            raise InvalidStateException(state_type, "Unable to register state, state type is invalid")
