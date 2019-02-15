#!/usr/bin/env python3.7

import logging
from .activity_filter_state import _ActivityFilterState
from ..exceptions import FullActivityQueueException

logger = logging.getLogger(__name__)


class DefaultState(_ActivityFilterState):
    """
    Defines default log filter behavior

    Default entries are added to default filter queue,
    while high priority entries are also added to high priority queue.

    Temporal coherency of the events is assured, even if contingency measures are enforced.
    """

    identifier = "default"

    def add_activity(self, activity):
        """
        Add default priority entry
        :param activity: activity to add
        """
        try:
            self._log_filter.activities.add(activity)
        except FullActivityQueueException:
            logger.warning("Unable to add activity to queue")

    def process(self):
        """
        Process entry queues

        Reset default high priority queue and process default priority queue only
        """

        old_queue = self._log_filter.activities.reset()

        logger.debug("Process Queue")
        self._dispatch_queue(old_queue)
