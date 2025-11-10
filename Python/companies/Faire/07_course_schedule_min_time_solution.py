#!/usr/bin/env python3
"""
Solution for Problem 7: Course Schedule with Minimum Time

🚨 Asked 2+ times at Faire

Problem: Find minimum time to complete all courses with prerequisites.
Courses can be taken in parallel if prerequisites are met.

Similar to: LeetCode "Parallel Courses" problem

Key Approach:
- Topological sort (BFS with Kahn's algorithm)
- Track earliest possible start time for each course
- Course can start when ALL its prerequisites are done
- Time = max(all prerequisite end times)
"""

from typing import List
from collections import defaultdict, deque


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

        >>> min_time_to_complete_courses(4, [[1,0], [2,1], [3,2]], [1, 1, 1, 1])
        4  # Must be sequential: 0->1->2->3 = 4 days

    Key Insight:
    - Courses can run in PARALLEL if no dependency
    - Course i can start at: max(end_time of all prerequisites)
    - Total time = max(end_time of all courses)

    Time: O(V + E) where V = courses, E = prerequisites
    Space: O(V + E) for adjacency list and in-degree tracking
    """
    # Build adjacency list (prerequisite -> courses that depend on it)
    graph = defaultdict(list)  # prereq -> [courses that need it]
    in_degree = [0] * n  # Count of prerequisites for each course

    for course, prereq in prerequisites:
        graph[prereq].append(course)
        in_degree[course] += 1

    # Track earliest start time for each course
    earliest_start = [0] * n  # When course can start
    earliest_end = [0] * n    # When course will end

    # BFS: Start with courses that have no prerequisites
    queue = deque()
    for i in range(n):
        if in_degree[i] == 0:
            queue.append(i)
            earliest_end[i] = time[i]  # Can start immediately, ends at time[i]

    # Process courses in topological order
    while queue:
        prereq = queue.popleft()

        # For each course that depends on this prerequisite
        for course in graph[prereq]:
            # Course can start when this prerequisite finishes
            earliest_start[course] = max(earliest_start[course], earliest_end[prereq])

            # Decrease in-degree
            in_degree[course] -= 1

            # If all prerequisites done, this course can now start
            if in_degree[course] == 0:
                earliest_end[course] = earliest_start[course] + time[course]
                queue.append(course)

    # Total time = when the last course finishes
    return max(earliest_end)


if __name__ == "__main__":
    print("=== Course Schedule Min Time Examples ===\n")

    # Example 1: Parallel courses
    print("Example 1: Parallel execution")
    n1 = 3
    prerequisites1 = [[1, 0], [2, 0]]  # Both 1 and 2 depend on 0
    time1 = [1, 2, 3]
    result1 = min_time_to_complete_courses(n1, prerequisites1, time1)
    print(f"Courses: {n1}")
    print(f"Prerequisites: {prerequisites1}")
    print(f"Time: {time1}")
    print(f"Min time: {result1}")
    print(f"Explanation:")
    print(f"  Day 0-1: Course 0 (1 day)")
    print(f"  Day 1-3: Courses 1 and 2 in PARALLEL")
    print(f"           Course 1: 2 days (ends day 3)")
    print(f"           Course 2: 3 days (ends day 4)")
    print(f"  Total: 4 days\n")

    # Example 2: Sequential courses
    print("Example 2: Sequential execution")
    n2 = 4
    prerequisites2 = [[1, 0], [2, 1], [3, 2]]  # 0->1->2->3 chain
    time2 = [1, 1, 1, 1]
    result2 = min_time_to_complete_courses(n2, prerequisites2, time2)
    print(f"Courses: {n2}")
    print(f"Prerequisites: {prerequisites2}")
    print(f"Time: {time2}")
    print(f"Min time: {result2}")
    print(f"Explanation:")
    print(f"  Must be sequential: 0->1->2->3")
    print(f"  Total: 1+1+1+1 = 4 days\n")

    # Example 3: Complex dependency
    print("Example 3: Complex dependencies")
    n3 = 5
    prerequisites3 = [[1, 0], [2, 0], [3, 1], [3, 2], [4, 3]]
    time3 = [1, 2, 3, 1, 2]
    result3 = min_time_to_complete_courses(n3, prerequisites3, time3)
    print(f"Courses: {n3}")
    print(f"Prerequisites: {prerequisites3}")
    print(f"Time: {time3}")
    print(f"Min time: {result3}")
    print(f"Explanation:")
    print(f"  Day 0-1: Course 0 (1 day)")
    print(f"  Day 1-3: Course 1 (2 days, ends day 3)")
    print(f"  Day 1-4: Course 2 (3 days, ends day 4) - parallel with 1!")
    print(f"  Day 4-5: Course 3 (1 day, waits for both 1 and 2)")
    print(f"  Day 5-7: Course 4 (2 days)")
    print(f"  Total: 7 days\n")

    # Example 4: No prerequisites (all parallel)
    print("Example 4: No dependencies (all parallel)")
    n4 = 3
    prerequisites4 = []
    time4 = [5, 3, 4]
    result4 = min_time_to_complete_courses(n4, prerequisites4, time4)
    print(f"Courses: {n4}")
    print(f"Prerequisites: {prerequisites4}")
    print(f"Time: {time4}")
    print(f"Min time: {result4}")
    print(f"Explanation:")
    print(f"  All courses can run in parallel")
    print(f"  Total: max(5, 3, 4) = 5 days\n")
