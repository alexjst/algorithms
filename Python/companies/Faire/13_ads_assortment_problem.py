#!/usr/bin/env python3
"""
Problem 13: Ads Assortment Problem (0/1 Knapsack)

Given a budget and ads with costs and values, select ads to maximize value.
This is a 0/1 Knapsack problem variant.

Example 1:
    Input:
        ads = [
            {'value': 60, 'cost': 10},
            {'value': 100, 'cost': 20},
            {'value': 120, 'cost': 30}
        ]
        budget = 50
    Output: 220
    Explanation: Select ads 2 and 3 (cost 20+30=50, value 100+120=220)

Example 2:
    Input:
        ads = [
            {'value': 60, 'cost': 10},
            {'value': 100, 'cost': 20}
        ]
        budget = 25
    Output: 100
    Explanation: Select ad 2 only (cost 20, value 100)

Constraints:
    - 1 <= len(ads) <= 1000
    - 1 <= budget <= 10000
    - Each ad has 'value' and 'cost'
    - Can select each ad at most once (0/1 knapsack)
"""

from typing import List, Dict


def max_ad_value(ads: List[Dict[str, int]], budget: int) -> int:
    """
    Find maximum ad value within budget using 0/1 Knapsack DP.

    Args:
        ads: List of ad dictionaries with 'value' and 'cost'
        budget: Maximum budget

    Returns:
        Maximum achievable value
    """
    # TODO: Implement 0/1 Knapsack DP solution
    return 0  # Placeholder


def max_ad_value_optimized(ads: List[Dict[str, int]], budget: int) -> int:
    """
    Space-optimized version using 1D DP array.

    Args:
        ads: List of ad dictionaries
        budget: Maximum budget

    Returns:
        Maximum achievable value
    """
    # TODO: Implement space-optimized version
    return 0  # Placeholder


def run_tests():
    """Run test cases for ads assortment problem."""

    # Test Case 1: Basic knapsack
    ads1 = [
        {'value': 60, 'cost': 10},
        {'value': 100, 'cost': 20},
        {'value': 120, 'cost': 30}
    ]
    result1 = max_ad_value(ads1, 50)
    assert result1 == 220, f"Test 1 failed: expected 220, got {result1}"
    print("✓ Test 1 passed: Select multiple ads")

    # Test Case 2: Budget constraint
    ads2 = [
        {'value': 60, 'cost': 10},
        {'value': 100, 'cost': 20}
    ]
    result2 = max_ad_value(ads2, 25)
    assert result2 == 100, f"Test 2 failed: expected 100, got {result2}"
    print("✓ Test 2 passed: Budget constraint")

    # Test Case 3: All ads fit
    ads3 = [
        {'value': 10, 'cost': 5},
        {'value': 20, 'cost': 10}
    ]
    result3 = max_ad_value(ads3, 15)
    assert result3 == 30, f"Test 3 failed: expected 30, got {result3}"
    print("✓ Test 3 passed: All ads fit in budget")

    # Test Case 4: No ads fit
    ads4 = [
        {'value': 100, 'cost': 50}
    ]
    result4 = max_ad_value(ads4, 40)
    assert result4 == 0, f"Test 4 failed: expected 0, got {result4}"
    print("✓ Test 4 passed: No ads fit")

    # Test Case 5: Zero budget
    ads5 = [
        {'value': 100, 'cost': 10}
    ]
    result5 = max_ad_value(ads5, 0)
    assert result5 == 0, f"Test 5 failed: expected 0, got {result5}"
    print("✓ Test 5 passed: Zero budget")

    print("\n" + "="*50)
    print("All basic tests passed! ✓")
    print("="*50)


def run_custom_tests():
    """Add your own custom test cases here."""
    print("\nRunning custom tests...")

    # Compare regular vs optimized
    print("\nComparing regular vs space-optimized:")
    ads = [
        {'value': 60, 'cost': 10},
        {'value': 100, 'cost': 20},
        {'value': 120, 'cost': 30}
    ]
    budget = 50
    result_regular = max_ad_value(ads, budget)
    result_optimized = max_ad_value_optimized(ads, budget)
    print(f"  Regular: {result_regular}")
    print(f"  Optimized: {result_optimized}")

    print("\nNo custom tests defined yet.")


if __name__ == "__main__":
    print("Testing Ads Assortment (Knapsack) Solution")
    print("="*50 + "\n")

    try:
        run_tests()
        run_custom_tests()
    except AssertionError as e:
        print(f"\n❌ Test failed: {e}")
    except Exception as e:
        print(f"\n❌ Error: {e}")
