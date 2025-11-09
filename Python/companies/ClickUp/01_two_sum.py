#!/usr/bin/env python3
"""
Problem 1: Two Sum (Array Pairs)

Given an array of integers nums and an integer target,
return indices of the two numbers that add up to target.
You may not use the same element twice.

Example 1:
    Input: nums = [2, 7, 11, 15], target = 9
    Output: [0, 1]
    Explanation: nums[0] + nums[1] = 2 + 7 = 9

Example 2:
    Input: nums = [3, 2, 4], target = 6
    Output: [1, 2]

Constraints:
    - 2 <= len(nums) <= 10^4
    - -10^9 <= nums[i] <= 10^9
    - Exactly one solution exists
    - Cannot use same index twice

================================================================================
INSTRUCTIONS:
- Implement your solution in: 01_two_sum_solution.py
- Run this file to test: python 01_two_sum.py
- To reset and practice again: just delete/reset the solution file
================================================================================
"""

# Import the solution
try:
    import importlib.util
    spec = importlib.util.spec_from_file_location(
        "solution_module",
        "01_two_sum_solution.py"
    )
    solution_module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(solution_module)
    two_sum = solution_module.two_sum
except Exception as e:
    print(f"❌ Error importing solution: {e}")
    print(f"   Make sure 01_two_sum_solution.py exists.")
    exit(1)

def run_tests():
    """Run test cases for two sum problem."""

    # Test Case 1: Basic case
    result1 = two_sum([2, 7, 11, 15], 9)
    assert result1 == [0, 1], f"Test 1 failed: expected [0, 1], got {result1}"
    print("✓ Test 1 passed: Basic case")

    # Test Case 2: Numbers not in order
    result2 = two_sum([3, 2, 4], 6)
    assert result2 == [1, 2], f"Test 2 failed: expected [1, 2], got {result2}"
    print("✓ Test 2 passed: Numbers not in order")

    # Test Case 3: Negative numbers
    result3 = two_sum([-1, -2, -3, -4, -5], -8)
    assert result3 == [2, 4], f"Test 3 failed: expected [2, 4], got {result3}"
    print("✓ Test 3 passed: Negative numbers")

    # Test Case 4: Same number appears twice
    result4 = two_sum([3, 3], 6)
    assert result4 == [0, 1], f"Test 4 failed: expected [0, 1], got {result4}"
    print("✓ Test 4 passed: Duplicate numbers")

    # Test Case 5: Larger array
    result5 = two_sum([1, 5, 3, 7, 9, 2], 10)
    assert result5 == [1, 3], f"Test 5 failed: expected [1, 3], got {result5}"
    print("✓ Test 5 passed: Larger array")

    print("\n" + "="*50)
    print("All basic tests passed! ✓")
    print("="*50)


def run_custom_tests():
    """Add your own custom test cases here."""
    print("\nRunning custom tests...")
    print("No custom tests defined yet.")


if __name__ == "__main__":
    print("Testing Two Sum Solution")
    print("="*50 + "\n")

    try:
        run_tests()
        run_custom_tests()
    except AssertionError as e:
        print(f"\n❌ Test failed: {e}")
    except Exception as e:
        print(f"\n❌ Error: {e}")
