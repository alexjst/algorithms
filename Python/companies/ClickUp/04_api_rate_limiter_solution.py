#!/usr/bin/env python3
"""
Solution for Problem 04: API Rate Limiter

TODO: Implement the RateLimiter class below.
"""

from collections import defaultdict, deque
from typing import Dict


class RateLimiter:
    """
    Rate limiter using sliding window algorithm.
    """

    def __init__(self, max_requests: int, window_seconds: int):
        """
        Initialize rate limiter.

        Args:
            max_requests: Maximum requests allowed in window
            window_seconds: Time window in seconds
        """
        # TODO: Implement initialization
        pass

    def is_allowed(self, user_id: str, timestamp: int) -> bool:
        """
        Check if request is allowed for user at given timestamp.

        Args:
            user_id: User identifier
            timestamp: Current timestamp in seconds

        Returns:
            True if request is allowed, False otherwise
        """
        # TODO: Implement your solution here
        return False  # Placeholder
