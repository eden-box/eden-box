#!/usr/bin/env python3.7

import logging
from .log_filter_state import _LogFilterState
from .state_type import StateType
from ..exceptions import FullDefaultException, FullHighException

logger = logging.getLogger(__name__)


class DefaultState(_LogFilterState):
    """
    Defines default log filter behavior

    Default entries are added to default filter queue,
    while high priority entries are also added to high priority queue.

    Temporal coherency of the events is assured, even if contingency measures are enforced.
    """

    identifier = "Default"

    def add_default_entry(self, entry):
        """
        Add default priority entry
        :param entry: default priority entry
        """
        try:
            logger.debug("Add default priority entry")
            self._log_filter.add_to_default_queue(entry)
        except FullDefaultException:
            logger.info("Enter Contingency state")
            self._change_state(StateType.CONTINGENCY)           # enter contingency state
            self._log_filter.log_entries.reset()                # discard default priority queue
            self.unbind()

    def add_high_priority_entry(self, entry):
        """
        Add high priority entry
        :param entry: high priority entry
        """
        try:
            logger.debug("Add high priority entry")
            self._log_filter.add_to_default_queue(entry)
            self._log_filter.add_to_high_priority_queue(entry)
        except (FullDefaultException, FullHighException):
            logger.info("Enter Contingency state")
            self._change_state(StateType.CONTINGENCY)           # enter contingency state
            self._log_filter.log_entries.reset()                # discard default priority queue
            self._log_filter.filter_high_priority_entry(entry)  # delegate choice to log filter
            self.unbind()

    def process(self):
        """
        Process entry queues

        Reset default high priority queue and process default priority queue only
        """

        self._log_filter.high_priority_log_entries.reset()

        old_queue = self._log_filter.log_entries.reset()

        logger.debug("Process Queue")
        self._dispatch_queue(old_queue)
