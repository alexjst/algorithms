"""
Problem 6: Merge Intervals (Medium)

**High Frequency - Interval/Array Manipulation**

Given an array of intervals where intervals[i] = [start_i, end_i], merge all
overlapping intervals, and return an array of the non-overlapping intervals that
cover all the intervals in the input.

Example 1:
Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].

Example 2:
Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.

Example 3:
Input: intervals = [[1,4],[0,4]]
Output: [[0,4]]

Constraints:
- 1 <= intervals.length <= 10^4
- intervals[i].length == 2
- 0 <= start_i <= end_i <= 10^4

Approach:
1. Sort intervals by start time
2. Iterate through sorted intervals
3. If current interval overlaps with last merged interval, merge them
4. Otherwise, add current interval to result

Time Complexity: O(n log n) due to sorting
Space Complexity: O(n) for output

Implement your solution in 06_merge_intervals_solution.py
"""

from typing import List

# Import the solution
try:
    from importlib import import_module
    solution = import_module('06_merge_intervals_solution')
    merge = solution.merge
except (ImportError, AttributeError):
    def merge(intervals: List[List[int]]) -> List[List[int]]:
        raise NotImplementedError("Implement merge in 06_merge_intervals_solution.py")


def test_merge_intervals():
    print("Testing Merge Intervals...\n")

    # Test 1: Basic merge
    print("Test 1: Basic overlapping intervals")
    intervals1 = [[1,3],[2,6],[8,10],[15,18]]
    result1 = merge(intervals1)
    expected1 = [[1,6],[8,10],[15,18]]
    assert result1 == expected1, f"Test 1 failed: expected {expected1}, got {result1}"
    print(f"✓ Test 1 passed: {result1}\n")

    # Test 2: Adjacent intervals (edge touch)
    print("Test 2: Adjacent intervals [1,4] and [4,5]")
    intervals2 = [[1,4],[4,5]]
    result2 = merge(intervals2)
    expected2 = [[1,5]]
    assert result2 == expected2, f"Test 2 failed: expected {expected2}, got {result2}"
    print(f"✓ Test 2 passed: {result2}\n")

    # Test 3: Unsorted input
    print("Test 3: Unsorted intervals")
    intervals3 = [[1,4],[0,4]]
    result3 = merge(intervals3)
    expected3 = [[0,4]]
    assert result3 == expected3, f"Test 3 failed: expected {expected3}, got {result3}"
    print(f"✓ Test 3 passed: {result3}\n")

    # Test 4: No overlap
    print("Test 4: No overlapping intervals")
    intervals4 = [[1,2],[3,4],[5,6]]
    result4 = merge(intervals4)
    expected4 = [[1,2],[3,4],[5,6]]
    assert result4 == expected4, f"Test 4 failed: expected {expected4}, got {result4}"
    print(f"✓ Test 4 passed: {result4}\n")

    # Test 5: All merge into one
    print("Test 5: All intervals merge into one")
    intervals5 = [[1,4],[2,5],[3,6],[4,7]]
    result5 = merge(intervals5)
    expected5 = [[1,7]]
    assert result5 == expected5, f"Test 5 failed: expected {expected5}, got {result5}"
    print(f"✓ Test 5 passed: {result5}\n")

    # Test 6: Single interval
    print("Test 6: Single interval")
    intervals6 = [[1,5]]
    result6 = merge(intervals6)
    expected6 = [[1,5]]
    assert result6 == expected6, f"Test 6 failed: expected {expected6}, got {result6}"
    print(f"✓ Test 6 passed: {result6}\n")

    # Test 7: Interval contains another
    print("Test 7: One interval contains another")
    intervals7 = [[1,10],[2,6],[8,9]]
    result7 = merge(intervals7)
    expected7 = [[1,10]]
    assert result7 == expected7, f"Test 7 failed: expected {expected7}, got {result7}"
    print(f"✓ Test 7 passed: {result7}\n")

    print("All tests passed! ✓")


if __name__ == "__main__":
    test_merge_intervals()
