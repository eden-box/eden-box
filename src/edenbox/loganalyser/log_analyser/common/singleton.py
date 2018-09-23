#!/usr/bin/env python3.7

from threading import Lock


class Singleton(type):
    """
    Thread-safe singleton metaclass
    """

    __instance = None
    __singleton_lock = Lock()

    def __call__(cls, *args, **kwargs):
        if cls.__instance is None:
            with cls.__singleton_lock:
                if cls.__instance is None:  # recheck to assure thread safety
                    cls.__instance = super(Singleton, cls).__call__(*args, **kwargs)

        return cls.__instance
