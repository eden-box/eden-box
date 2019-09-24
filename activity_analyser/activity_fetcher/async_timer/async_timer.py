#!/usr/bin/env python3.7

import asyncio


class AsyncTimer:
    """
    Async Timer, able to schedule awaitable function calls
    An initial delay may be set before the first callback function call
    """

    def __init__(self, interval, initial_delay, timer_name, callback):
        """
        If initial_delay is True, the job run for the first time only after the time value defined by interval argument
        :param interval: interval between method calls, in seconds
        :param initial_delay:
        :param timer_name: timer name
        :param callback: callback method to call
        """
        self._interval = interval
        self._initial_delay = initial_delay
        self._name = timer_name
        self._callback = callback
        self._active = True
        self._task = None

    def start(self):
        """
        Initialize the timer
        """
        self._task = asyncio.create_task(self._job())

    def await_termination(self):
        """
        Await timer termination
        Behaviour similar to a similar to a thread join
        """
        await self._task

    async def _job(self):
        """
        Job loop
        Responsible for periodically calling the callback function
        """
        if self._initial_delay:
            await asyncio.sleep(self._interval)
        while self._active:
            await self._callback()
            await asyncio.sleep(self._interval)

    def cancel(self):
        """
        Cancel the timer and stops the scheduled task
        """
        self._active = False
        self._task.cancel()
