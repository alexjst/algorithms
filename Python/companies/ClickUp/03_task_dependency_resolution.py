#!/usr/bin/env python3
"""
Problem 03: Task Dependency Resolution

Given tasks and their dependencies, determine if all tasks can be completed and return valid execution order.

Example:
    Input: num_tasks = 4, dependencies = [[1,0], [2,0], [3,1], [3,2]]
Output: [0, 1, 2, 3] or [0, 2, 1, 3]

Constraints:
    - Return empty list if circular dependency exists
    - Tasks labeled 0 to n-1

================================================================================
INSTRUCTIONS:
- Implement your solution in: 03_task_dependency_resolution_solution.py
- Run this file to test: python 03_task_dependency_resolution.py
- To reset and practice again: just delete/reset the solution file
================================================================================
"""

# Import the solution
try:
    import importlib.util
    spec = importlib.util.spec_from_file_location(
        "solution_module",
        "03_task_dependency_resolution_solution.py"
    )
    solution_module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(solution_module)
    find_task_order = solution_module.find_task_order
except Exception as e:
    print(f"❌ Error importing solution: {e}")
    print(f"   Make sure 03_task_dependency_resolution_solution.py exists.")
    exit(1)

def run_tests():
    """Run test cases for task dependency resolution."""

    # Test Case 1: [0,1,2,3] or [0,2,1,3]
    result1 = find_task_order(4, [[1,0], [2,0], [3,1], [3,2]])
    assert result1 in [[0,1,2,3], [0,2,1,3]], f"Test 1 failed: {result1}"
    print("✓ Test 1 passed: [0,1,2,3] or [0,2,1,3]")

    # Test Case 2: []
    result2 = find_task_order(2, [[1,0], [0,1]])
    assert result2 == [], f"Test 2 failed: {result2}"
    print("✓ Test 2 passed: []")

    # Test Case 3: 3 tasks
    result3 = find_task_order(3, [])
    assert len(result3) == 3, f"Test 3 failed: {result3}"
    print("✓ Test 3 passed: 3 tasks")

    print("\n" + "="*50)
    print("All basic tests passed! ✓")
    print("="*50)


def run_custom_tests():
    """Add your own custom test cases here."""
    print("\nRunning custom tests...")
    print("No custom tests defined yet.")


if __name__ == "__main__":
    print("Testing Task Dependency Resolution Solution")
    print("="*50 + "\n")

    try:
        run_tests()
        run_custom_tests()
    except AssertionError as e:
        print(f"\n❌ Test failed: {e}")
    except Exception as e:
        print(f"\n❌ Error: {e}")
