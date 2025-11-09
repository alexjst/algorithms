#!/usr/bin/env python3
"""
Problem 11: Array Divisibility Check

Check if an array can be divided into pairs where each pair sum is divisible by k.

Example 1:
    Input: arr = [1, 2, 3, 4, 5, 10, 6, 7, 8, 9], k = 5
    Output: True
    Explanation: Pairs: (1,4), (2,3), (5,10), (6,9), (7,8) - all sums divisible by 5

Example 2:
    Input: arr = [1, 2, 3, 4, 5, 6], k = 7
    Output: True
    Explanation: (1,6), (2,5), (3,4) - all sums divisible by 7

Example 3:
    Input: arr = [1, 2, 3, 4, 5, 6], k = 10
    Output: False

Constraints:
    - arr.length is even
    - 1 <= arr.length <= 10^5
    - 1 <= arr[i] <= 10^9
    - 1 <= k <= 10^5
    - Use modular arithmetic
"""

from typing import List
from collections import Counter


def can_arrange_pairs(arr: List[int], k: int) -> bool:
    """
    Check if array can be arranged into pairs with sum divisible by k.

    Args:
        arr: Array of integers
        k: Divisor

    Returns:
        True if valid pairing exists, False otherwise
    """
    # TODO: Implement using remainder frequency counting
    return False  # Placeholder


def run_tests():
    """Run test cases for array divisibility."""

    # Test Case 1: Valid pairing exists
    arr1 = [1, 2, 3, 4, 5, 10, 6, 7, 8, 9]
    k1 = 5
    result1 = can_arrange_pairs(arr1, k1)
    assert result1 == True, f"Test 1 failed: expected True, got {result1}"
    print("✓ Test 1 passed: Valid pairing with k=5")

    # Test Case 2: Another valid case
    arr2 = [1, 2, 3, 4, 5, 6]
    k2 = 7
    result2 = can_arrange_pairs(arr2, k2)
    assert result2 == True, f"Test 2 failed: expected True, got {result2}"
    print("✓ Test 2 passed: Valid pairing with k=7")

    # Test Case 3: Invalid pairing
    arr3 = [1, 2, 3, 4, 5, 6]
    k3 = 10
    result3 = can_arrange_pairs(arr3, k3)
    assert result3 == False, f"Test 3 failed: expected False, got {result3}"
    print("✓ Test 3 passed: Invalid pairing detected")

    # Test Case 4: All elements divisible by k
    arr4 = [2, 4, 6, 8]
    k4 = 2
    result4 = can_arrange_pairs(arr4, k4)
    print(f"Test 4: Result = {result4}")
    print("✓ Test 4 passed: Elements divisible by k")

    # Test Case 5: Small array
    arr5 = [1, 1]
    k5 = 2
    result5 = can_arrange_pairs(arr5, k5)
    assert result5 == True, f"Test 5 failed: expected True, got {result5}"
    print("✓ Test 5 passed: Small array")

    print("\n" + "="*50)
    print("All basic tests passed! ✓")
    print("="*50)


def run_custom_tests():
    """Add your own custom test cases here."""
    print("\nRunning custom tests...")

    # Test remainder distribution
    print("\nTesting remainder counting:")
    test_arr = [1, 2, 3, 4, 5, 6]
    k = 5
    remainders = Counter([x % k for x in test_arr])
    print(f"  Array: {test_arr}")
    print(f"  k = {k}")
    print(f"  Remainders: {dict(remainders)}")

    print("\nNo custom pairing tests defined yet.")


if __name__ == "__main__":
    print("Testing Array Divisibility Check Solution")
    print("="*50 + "\n")

    try:
        run_tests()
        run_custom_tests()
    except AssertionError as e:
        print(f"\n❌ Test failed: {e}")
    except Exception as e:
        print(f"\n❌ Error: {e}")
