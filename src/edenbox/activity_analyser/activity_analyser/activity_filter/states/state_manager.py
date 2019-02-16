#!/usr/bin/env python3.7

from .state_type import StateType
from .default_state import DefaultState
from .exceptions import InvalidStateException


class StateManager:
    """
    State Manager
    Registers the requested state type
    """

    @staticmethod
    def register_state(state_type, activity_filter):
        """
        Registers the requested state type in the provided activity_filter

        :param state_type: type of state to register
        :param activity_filter: activity_filter to which the state belongs to
        :return: registered state type
        """
        if state_type is StateType.DEFAULT:
            return DefaultState(activity_filter)
        else:  # only reached in case of method usage error, exception is not handled by default
            raise InvalidStateException(state_type, "Unable to register state, state type is invalid.")
