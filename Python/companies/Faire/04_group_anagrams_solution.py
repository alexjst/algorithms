#!/usr/bin/env python3
"""
Solution for Problem 4: Group Anagrams

Standard LeetCode problem (LC 49) - Asked 3+ times at Faire

Problem: Group strings that are anagrams of each other.

TODO: Implement the function below.

Approaches:
1. Sort each string as key: O(n * k log k) where n = # strings, k = avg length
2. Character count as key: O(n * k)

Edge Cases:
- Empty strings
- Single character strings
- All anagrams vs no anagrams
"""

from typing import List
from collections import defaultdict


def group_anagrams(strs: List[str]) -> List[List[str]]:
    """
    Group strings that are anagrams of each other.

    Args:
        strs: List of strings (lowercase letters only)
              Example: ["eat", "tea", "tan", "ate", "nat", "bat"]

    Returns:
        List of groups (order doesn't matter)
        Example: [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]

    Time Complexity: O(n * k log k) using sorted string, or O(n * k) using count
    Space Complexity: O(n * k) for the output

    Examples:
        >>> group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
        # Returns groups of anagrams (order may vary)
        >>> group_anagrams([""])
        [[""]]
        >>> group_anagrams(["a"])
        [["a"]]
    """
    # TODO: Implement your solution here
    # Hint: Use a dictionary with sorted string as key
    #   Example: "eat" → key = "aet", "tea" → key = "aet" (same group!)
    # Alternative: Use character count tuple as key

    pass
