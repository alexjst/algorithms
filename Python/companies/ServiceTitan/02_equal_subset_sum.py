#!/usr/bin/env python3
"""
Problem 2: Equal Subset Sum Partition

Actual ServiceTitan interview question - determine if an array can be partitioned
into two subsets with equal sum.

Requirements:
- Given array of positive integers with unique values
- Determine if can split into two subsets with equal sums
- Each element must be used exactly once
- Return True if possible, False otherwise

Example:
    canPartition([1, 5, 11, 5])     # True  ([1, 5, 5] and [11])
    canPartition([1, 2, 3, 5])      # False (no valid partition)
    canPartition([1, 2, 5])         # False (sum is odd, can't split)
    canPartition([2, 2, 2, 2])      # True  ([2, 2] and [2, 2])

Approach:
1. If total sum is odd, return False
2. If total sum is even, find if subset exists with sum = total_sum / 2
3. Use dynamic programming (subset sum problem)

Time Complexity: O(n * sum) where sum is total sum of array
Space Complexity: O(sum)
"""

try:
    import importlib.util
    spec = importlib.util.spec_from_file_location("solution_module",
                                                   "02_equal_subset_sum_solution.py")
    solution_module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(solution_module)
    canPartition = solution_module.canPartition
except Exception as e:
    print(f"❌ Error importing solution: {e}")
    exit(1)

def test_equal_subset_sum():
    print("Testing Equal Subset Sum Partition...")
    print()

    # Test 1: Basic valid partition
    print("Test 1: Basic valid partition")
    assert canPartition([1, 5, 11, 5]) == True, "Test 1 failed"
    print("✓ Test 1 passed")
    print()

    # Test 2: No valid partition
    print("Test 2: No valid partition")
    assert canPartition([1, 2, 3, 5]) == False, "Test 2 failed"
    print("✓ Test 2 passed")
    print()

    # Test 3: Odd sum (impossible)
    print("Test 3: Odd sum")
    assert canPartition([1, 2, 5]) == False, "Test 3 failed"
    print("✓ Test 3 passed")
    print()

    # Test 4: All equal elements
    print("Test 4: All equal elements")
    assert canPartition([2, 2, 2, 2]) == True, "Test 4 failed"
    print("✓ Test 4 passed")
    print()

    # Test 5: Single element
    print("Test 5: Single element")
    assert canPartition([10]) == False, "Test 5 failed"
    print("✓ Test 5 passed")
    print()

    # Test 6: Two elements - valid
    print("Test 6: Two equal elements")
    assert canPartition([5, 5]) == True, "Test 6 failed"
    print("✓ Test 6 passed")
    print()

    # Test 7: Two elements - invalid
    print("Test 7: Two different elements")
    assert canPartition([3, 7]) == False, "Test 7 failed"
    print("✓ Test 7 passed")
    print()

    # Test 8: Larger example - valid
    print("Test 8: Larger valid partition")
    assert canPartition([1, 2, 3, 4, 5, 6, 7]) == True, "Test 8 failed"
    # Total = 28, can split: [1,2,4,7] = 14 and [3,5,6] = 14
    print("✓ Test 8 passed")
    print()

    # Test 9: Larger example - invalid
    print("Test 9: Larger invalid partition")
    assert canPartition([1, 2, 3, 4, 5, 6, 8]) == False, "Test 9 failed"
    # Total = 29 (odd)
    print("✓ Test 9 passed")
    print()

    # Test 10: Edge case - empty array
    print("Test 10: Empty array")
    assert canPartition([]) == True, "Test 10 failed: empty splits into two empty subsets"
    print("✓ Test 10 passed")
    print()

    # Test 11: Large numbers
    print("Test 11: Large numbers")
    assert canPartition([100, 100, 100, 100]) == True, "Test 11 failed"
    print("✓ Test 11 passed")
    print()

    print("All tests passed! ✓")

if __name__ == "__main__":
    test_equal_subset_sum()
