#!/usr/bin/env python3.7

import logging
from .log_filter_state import _LogFilterState
from .state_type import StateType
from ..exceptions import FullHighException

logger = logging.getLogger(__name__)


class ContingencyState(_LogFilterState):
    """
    Defines contingency log filter behavior

    During contingency, only high priority entries are added, while default ones are ignored.
    Only high priority entries are processed.
    """

    identifier = "Contingency"

    def add_default_entry(self, entry):
        """
        Add default priority entry
        :param entry: default priority entry
        """
        return

    def add_high_priority_entry(self, entry):
        """
        Add high priority entry
        :param entry: high priority entry
        """
        try:
            logger.debug("Add high priority entry")
            self._log_filter.add_to_high_priority_queue(entry)
        except FullHighException:  # if queue is full, dispatch it
            old_p_queue = self._log_filter.high_priority_log_entries.reset()
            self._log_filter.filter_high_priority_entry(entry)
            logger.debug("Processing Contingency state queue")
            self._dispatch_queue(old_p_queue)

    def process(self):
        """
        Process entry queues

        Reset default priority queue and process high priority queue only
        Revert state back to default
        The state is set to Default before processing the queue to ensure that new entries
        are correctly processed accordingly to Default state and not to Contingency state
        """

        self._log_filter.log_entries.reset()

        old_p_queue = self._log_filter.high_priority_log_entries.reset()

        logger.info("Entering Default state")
        self._change_state(StateType.DEFAULT)  # return to default state

        logger.debug("Processing Contingency state queue")
        self._dispatch_queue(old_p_queue)
        self.unbind()
