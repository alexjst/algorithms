#!/usr/bin/env python3
"""
Solution for Problem 7: Course Schedule with Minimum Time

Asked 2+ times at Faire

Problem: Find minimum time to complete all courses with prerequisites.
Courses can be taken in parallel if prerequisites are met.

Similar to: LeetCode "Parallel Courses" problem

TODO: Implement the function below.

Approach:
- Use topological sort (BFS/DFS)
- Track earliest completion time for each course
- Courses can run in parallel if no dependencies
"""

from typing import List


def min_time_to_complete_courses(n: int, prerequisites: List[List[int]], time: List[int]) -> int:
    """
    Find minimum time to complete all courses.

    Args:
        n: Number of courses (0 to n-1)
        prerequisites: List of [course, prerequisite] pairs
                      [a, b] means course b must be completed before course a
        time: List where time[i] is duration of course i

    Returns:
        Minimum time to complete all courses (can take multiple in parallel)

    Examples:
        >>> min_time_to_complete_courses(3, [[1,0], [2,0]], [1, 2, 3])
        4  # Course 0 (1 day), then courses 1 and 2 in parallel (max 3 days) = 4 total
    """
    # TODO: Implement using topological sort + dynamic programming
    # Hint:
    #   1. Build adjacency list from prerequisites
    #   2. Track in-degree for each course
    #   3. Use BFS starting from courses with no prerequisites
    #   4. Track earliest start time for each course
    #   5. For each course, earliest_start = max(end_time of all prerequisites)
    #   6. Return max end time across all courses
    pass
