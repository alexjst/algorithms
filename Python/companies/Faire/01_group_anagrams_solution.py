#!/usr/bin/env python3
"""
Solution for Problem 1: Group Anagrams

TODO: Implement the group_anagrams function below.
"""

from typing import List
from collections import defaultdict

def group_anagrams(strs: List[str]) -> List[List[str]]:
    """
    Group anagrams together from a list of strings.

    Args:
        strs: List of strings to group

    Returns:
        List of lists, where each inner list contains anagrams
    """
    anagrams = defaultdict(list)

    for s in strs:
        key = ''.join(sorted(s))
        anagrams[key].append(s)

    return list(anagrams.values())
