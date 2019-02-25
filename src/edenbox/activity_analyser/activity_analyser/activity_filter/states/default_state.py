#!/usr/bin/env python3.7

import logging
from .activity_filter_state import _ActivityFilterState
from ..exceptions import FullActivityQueueException

logger = logging.getLogger(__name__)


class DefaultState(_ActivityFilterState):
    """
    Defines activity filter behavior
    Temporal coherency of the events is assured
    """

    identifier = "default"

    def add_activity(self, activity):
        """
        Add activity
        :param activity: activity to add
        """
        try:
            self._activity_filter.activities.add(activity)
        except FullActivityQueueException:
            logger.warning("Unable to add activity to queue.")

    def process(self):
        """
        Process activity queue
        """

        old_queue = self._activity_filter.activities.reset()

        logger.debug("Process Queue")
        self._dispatch_queue(old_queue)
