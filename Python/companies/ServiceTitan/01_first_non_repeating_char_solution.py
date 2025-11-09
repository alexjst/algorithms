#!/usr/bin/env python3
"""Solution for Problem 1: First Non-Repeating Character"""

def firstUniqChar(s: str) -> int:
    """
    Find the first non-repeating character in a string.

    TODO: Implement solution
    Hints:
    1. Use hash map to count character frequencies
    2. Two-pass approach:
       - First pass: count all characters
       - Second pass: find first character with count 1
    3. Return index of first unique character, or -1 if none

    Algorithm:
    char_count = {}
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1

    for i, char in enumerate(s):
        if char_count[char] == 1:
            return i

    return -1

    Args:
        s: Input string

    Returns:
        Index of first non-repeating character, or -1 if none exists
    """
    pass
