#!/usr/bin/env python3
"""Solution for Problem 8: Find the Spy"""

from typing import List

class Solution:
    def findSpy(self, n: int, trust: List[List[int]]) -> int:
        """
        Find the spy who is accused by everyone else.

        TODO: Implement spy detection
        Hints:
        1. Count in-degree (accusations) and out-degree (accusing) for each person
        2. Spy has in-degree n-1 (everyone accuses them) and out-degree 0 (they accuse no one)
        3. Use two arrays or dictionary to track degrees
        4. Iterate through trust relationships once
        5. Check which person meets spy criteria

        Args:
            n: Number of people
            trust: List of [a, b] where a accuses b

        Returns:
            Person number (1-indexed) who is the spy, or -1 if none exists
        """
        pass
