#!/usr/bin/env python3
"""
Solution for Problem 1: API Rate Limiter with Priority Queues

TODO: Implement the PriorityRateLimiter class below.
"""

import time
from collections import deque

class PriorityRateLimiter:
    """
    Rate limiter with priority queue support for healthcare API requests.

    Args:
        max_requests: Maximum number of requests allowed in the time window
        time_window: Time window in seconds
    """

    def __init__(self, max_requests: int, time_window: float):
        """Initialize the rate limiter."""
        # TODO: Implement initialization
        pass

    def allow_request(self, priority: int) -> bool:
        """
        Check if a request with given priority should be allowed.

        Args:
            priority: Priority level (lower number = higher priority)

        Returns:
            True if request is allowed, False if rate limited
        """
        # TODO: Implement request handling
        # Hints:
        # 1. Remove requests outside the time window
        # 2. Check if we're under the max_requests limit
        # 3. If allowed, add the request with timestamp and priority
        # 4. Return True/False based on whether request was allowed
        pass
