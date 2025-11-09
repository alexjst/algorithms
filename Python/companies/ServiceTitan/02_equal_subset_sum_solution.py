#!/usr/bin/env python3
"""Solution for Problem 2: Equal Subset Sum Partition"""

from typing import List

def canPartition(nums: List[int]) -> bool:
    """
    Determine if array can be partitioned into two subsets with equal sum.

    TODO: Implement solution
    Hints:
    1. Calculate total sum of array
    2. If sum is odd, return False (can't split evenly)
    3. If sum is even, target = sum // 2
    4. Problem becomes: can we find subset with sum = target?
    5. Use dynamic programming (subset sum problem)
       - dp[i] = True if we can achieve sum i
       - For each number, update dp in reverse order
    6. Return dp[target]

    Dynamic Programming Approach:
    total = sum(nums)
    if total % 2 != 0:
        return False

    target = total // 2
    dp = [False] * (target + 1)
    dp[0] = True  # Can always achieve sum 0 (empty subset)

    for num in nums:
        # Iterate backwards to avoid using same element twice
        for i in range(target, num - 1, -1):
            dp[i] = dp[i] or dp[i - num]

    return dp[target]

    Alternative: Recursion with Memoization
    - Try including/excluding each element
    - Memoize (index, current_sum) states

    Args:
        nums: Array of positive integers

    Returns:
        True if array can be partitioned into two equal sum subsets
    """
    pass
