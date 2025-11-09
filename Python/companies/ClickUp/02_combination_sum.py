#!/usr/bin/env python3
"""
Problem 02: Combination Sum

Find all unique combinations where chosen numbers sum to target. Numbers can be used unlimited times.

Example:
    Input: candidates = [2, 3, 6, 7], target = 7
Output: [[2, 2, 3], [7]]

Constraints:
    - 1 <= candidates.length <= 30
    - 1 <= target <= 500

================================================================================
INSTRUCTIONS:
- Implement your solution in: 02_combination_sum_solution.py
- Run this file to test: python 02_combination_sum.py
- To reset and practice again: just delete/reset the solution file
================================================================================
"""

# Import the solution
try:
    import importlib.util
    spec = importlib.util.spec_from_file_location(
        "solution_module",
        "02_combination_sum_solution.py"
    )
    solution_module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(solution_module)
    combination_sum = solution_module.combination_sum
except Exception as e:
    print(f"❌ Error importing solution: {e}")
    print(f"   Make sure 02_combination_sum_solution.py exists.")
    exit(1)

def run_tests():
    """Run test cases for combination sum."""

    # Test Case 1: [[2, 2, 3], [7]]
    result1 = combination_sum([2, 3, 6, 7], 7)
    assert sorted(result1) == sorted([[2, 2, 3], [7]]), f"Test 1 failed: {result1}"
    print("✓ Test 1 passed: [[2, 2, 3], [7]]")

    # Test Case 2: 3 combinations
    result2 = combination_sum([2, 3, 5], 8)
    assert len(result2) == 3, f"Test 2 failed: expected 3, got {len(result2)}"
    print("✓ Test 2 passed: 3 combinations")

    # Test Case 3: []
    result3 = combination_sum([2, 4], 7)
    assert result3 == [], f"Test 3 failed: {result3}"
    print("✓ Test 3 passed: []")

    print("\n" + "="*50)
    print("All basic tests passed! ✓")
    print("="*50)


def run_custom_tests():
    """Add your own custom test cases here."""
    print("\nRunning custom tests...")
    print("No custom tests defined yet.")


if __name__ == "__main__":
    print("Testing Combination Sum Solution")
    print("="*50 + "\n")

    try:
        run_tests()
        run_custom_tests()
    except AssertionError as e:
        print(f"\n❌ Test failed: {e}")
    except Exception as e:
        print(f"\n❌ Error: {e}")
