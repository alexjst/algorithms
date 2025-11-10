"""
Solution for Merge Intervals

Implement your solution below.
"""

from typing import List

def merge(intervals: List[List[int]]) -> List[List[int]]:
    """
    Merge all overlapping intervals.

    Args:
        intervals: List of intervals [start, end]

    Returns:
        List of merged non-overlapping intervals

    Approach:
        1. Sort intervals by start time
        2. Initialize result with first interval
        3. For each subsequent interval:
           - If it overlaps with last interval in result, merge them
           - Otherwise, add it to result

    Overlap condition: current_start <= last_end

    Time: O(n log n) for sorting
    Space: O(n) for output
    """
    # TODO: Implement your solution

    # Hints:
    # 1. Sort intervals by start time: intervals.sort(key=lambda x: x[0])
    # 2. Initialize merged = [intervals[0]]
    # 3. For each interval in intervals[1:]:
    #    - Get last merged interval
    #    - If current[0] <= last[1]:  # Overlapping
    #        - Merge: last[1] = max(last[1], current[1])
    #    - Else:  # Not overlapping
    #        - Add current to merged
    # 4. Return merged

    # Edge cases:
    # - Empty input: return []
    # - Single interval: return as is
    # - All merge into one: keep extending the end

    raise NotImplementedError("Implement this function")
