#!/usr/bin/env python3
"""Solution for Problem 10: TV Remote Keyboard Navigation"""

from typing import List
from collections import deque

class Solution:
    def typePath(self, text: str, keyboard: List[List[str]]) -> List[str]:
        """
        Find shortest button sequence to type text on TV keyboard.

        TODO: Implement BFS pathfinding
        Hints:
        1. Build char -> position map first for O(1) lookup
        2. For each character in text:
           a. BFS from current position to target character
           b. Track path taken (UP/DOWN/LEFT/RIGHT)
           c. Add "OK" after reaching target
           d. Update current position
        3. Return concatenated paths for all characters

        BFS Implementation:
        1. Queue stores (row, col, path_so_far)
        2. Visit each cell once (use visited set)
        3. Try 4 directions with corresponding commands
        4. Stop when target character reached

        Args:
            text: String to type
            keyboard: 2D grid of characters

        Returns:
            List of button commands
        """
        pass
