#!/usr/bin/env python3
"""
Problem 7: Max Consecutive Ones

Given a binary array, return the maximum number of consecutive 1's.

Example 1:
    Input: [1, 1, 0, 1, 1, 1]
    Output: 3
    Explanation: Maximum consecutive 1's is 3 (last three elements)

Example 2:
    Input: [1, 0, 1, 1, 0, 1]
    Output: 2

Example 3:
    Input: [0, 0, 0]
    Output: 0

Constraints:
    - 1 <= nums.length <= 10^5
    - nums[i] is either 0 or 1
"""

from typing import List


def find_max_consecutive_ones(nums: List[int]) -> int:
    """
    Find maximum number of consecutive 1's in binary array.

    Args:
        nums: Binary array containing 0s and 1s

    Returns:
        Maximum count of consecutive 1's
    """
    # TODO: Implement your solution here
    return 0  # Placeholder


def run_tests():
    """Run test cases for max consecutive ones."""

    # Test Case 1: Basic example
    input1 = [1, 1, 0, 1, 1, 1]
    result1 = find_max_consecutive_ones(input1)
    assert result1 == 3, f"Test 1 failed: expected 3, got {result1}"
    print("✓ Test 1 passed: Basic example")

    # Test Case 2: Multiple sequences
    input2 = [1, 0, 1, 1, 0, 1]
    result2 = find_max_consecutive_ones(input2)
    assert result2 == 2, f"Test 2 failed: expected 2, got {result2}"
    print("✓ Test 2 passed: Multiple sequences")

    # Test Case 3: All zeros
    input3 = [0, 0, 0]
    result3 = find_max_consecutive_ones(input3)
    assert result3 == 0, f"Test 3 failed: expected 0, got {result3}"
    print("✓ Test 3 passed: All zeros")

    # Test Case 4: All ones
    input4 = [1, 1, 1, 1]
    result4 = find_max_consecutive_ones(input4)
    assert result4 == 4, f"Test 4 failed: expected 4, got {result4}"
    print("✓ Test 4 passed: All ones")

    # Test Case 5: Single element
    input5 = [1]
    result5 = find_max_consecutive_ones(input5)
    assert result5 == 1, f"Test 5 failed: expected 1, got {result5}"
    print("✓ Test 5 passed: Single element")

    print("\n" + "="*50)
    print("All basic tests passed! ✓")
    print("="*50)


def run_custom_tests():
    """Add your own custom test cases here."""
    print("\nRunning custom tests...")

    # Add your custom test cases here

    print("No custom tests defined yet.")


if __name__ == "__main__":
    print("Testing Max Consecutive Ones Solution")
    print("="*50 + "\n")

    try:
        run_tests()
        run_custom_tests()
    except AssertionError as e:
        print(f"\n❌ Test failed: {e}")
    except Exception as e:
        print(f"\n❌ Error: {e}")
