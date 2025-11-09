#!/usr/bin/env python3
"""
Problem 6: Course Schedule with Minimum Time

Find minimum time to complete all courses given prerequisites and course durations.

Each course has:
- Prerequisites (courses that must be completed first)
- Duration (time to complete the course)

Return the minimum total time to complete all courses.

Example 1:
    Input:
        courses = 4
        prerequisites = [[1, 0], [2, 0], [3, 1], [3, 2]]
        durations = [1, 2, 3, 4]
    Output: 7
    Explanation:
        Course 0: time 1 (no prereqs)
        Course 1: time 2 (after course 0) -> earliest = 1 + 2 = 3
        Course 2: time 3 (after course 0) -> earliest = 1 + 3 = 4
        Course 3: time 4 (after courses 1, 2) -> earliest = max(3, 4) + 4 = 8
        But we can take 0, 1, 2 in parallel, so minimum is 7

Constraints:
    - 1 <= courses <= 2000
    - 0 <= prerequisites.length <= 5000
    - prerequisites[i] = [a, b] means course b must be taken before course a
    - No cycles in prerequisites
    - All courses can be completed - TEST SCAFFOLDING (DO NOT EDIT)

================================================================================
INSTRUCTIONS:
- Implement your solution in: 06_course_schedule_min_time_solution.py
- Run this file to test: python 06_course_schedule_min_time.py
- To reset and practice again: just delete/reset the solution file
================================================================================
"""

# Import the solution
try:
    import importlib.util
    spec = importlib.util.spec_from_file_location(
        "solution_module",
        "07_course_schedule_min_time_solution.py"
    )
    solution_module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(solution_module)
    min_time_to_complete_courses = solution_module.min_time_to_complete_courses
except Exception as e:
    print(f"❌ Error importing solution: {e}")
    print(f"   Make sure 07_course_schedule_min_time_solution.py exists.")
    exit(1)

def run_tests():
    """Run test cases for course scheduling."""

    # Test Case 1: Basic example with parallel courses
    courses1 = 4
    prereqs1 = [[1, 0], [2, 0], [3, 1], [3, 2]]
    durations1 = [1, 2, 3, 4]
    result1 = min_time_to_complete_courses(courses1, prereqs1, durations1)
    # Course 0: 1, Course 1: 1+2=3, Course 2: 1+3=4, Course 3: 4+4=8
    # Minimum time is 8
    assert result1 == 8, f"Test 1 failed: expected 8, got {result1}"
    print("✓ Test 1 passed: Basic parallel courses")

    # Test Case 2: Sequential courses
    courses2 = 3
    prereqs2 = [[1, 0], [2, 1]]
    durations2 = [1, 2, 3]
    result2 = min_time_to_complete_courses(courses2, prereqs2, durations2)
    # 0 -> 1 -> 2: total = 1 + 2 + 3 = 6
    assert result2 == 6, f"Test 2 failed: expected 6, got {result2}"
    print("✓ Test 2 passed: Sequential courses")

    # Test Case 3: No prerequisites
    courses3 = 3
    prereqs3 = []
    durations3 = [2, 3, 4]
    result3 = min_time_to_complete_courses(courses3, prereqs3, durations3)
    # All can be taken in parallel, max duration is 4
    print(f"Test 3: Minimum time = {result3} (expected 4)")
    print("✓ Test 3 passed: No prerequisites")

    print("\n" + "="*50)
    print("All basic tests passed! ✓")
    print("="*50)



def run_custom_tests():
    """Add your own custom test cases here."""
    print("\nRunning custom tests...")

    # Add your custom test cases here

    print("No custom tests defined yet.")



if __name__ == "__main__":
    print("Testing Course Schedule with Minimum Time Solution")
    print("="*50 + "\n")

    try:
        run_tests()
        run_custom_tests()
    except AssertionError as e:
        print(f"\n❌ Test failed: {e}")
    except Exception as e:
        print(f"\n❌ Error: {e}")
