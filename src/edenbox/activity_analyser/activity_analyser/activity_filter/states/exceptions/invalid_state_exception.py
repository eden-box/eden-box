#!/usr/bin/env python3.7

from .state_factory_exception import StateFactoryException


class InvalidStateException(StateFactoryException):
    """
    Exception raised when an invalid type is request to the State Factory
    """
    pass
