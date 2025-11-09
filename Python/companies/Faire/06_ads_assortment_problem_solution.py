#!/usr/bin/env python3
"""
Solution for Problem 6: Ads Assortment Problem

Asked 3+ times at Faire

Problem: Maximize ad value while respecting weekly limits per brand and per user.

Constraints:
- Each brand can show max N ads per week
- Each user can see max M ads per week
- Maximize total ad value

TODO: Implement the functions below.
"""

from typing import List, Tuple


def max_ad_value(ads: List[Tuple[str, str, int]], brand_limit: int, user_limit: int) -> int:
    """
    Calculate maximum ad value respecting brand and user limits.

    Args:
        ads: List of (user_id, brand_id, value) tuples
             Example: [('u1', 'Nike', 100), ('u1', 'Adidas', 90), ('u2', 'Nike', 80)]
        brand_limit: Max ads per brand per week
        user_limit: Max ads per user per week

    Returns:
        Maximum total ad value

    Examples:
        >>> ads = [('u1', 'Nike', 100), ('u1', 'Adidas', 90), ('u2', 'Nike', 80)]
        >>> max_ad_value(ads, brand_limit=1, user_limit=1)
        # Should return optimal selection respecting limits
    """
    # TODO: Implement ad selection algorithm
    # Hint: Greedy approach - sort by value descending
    # Track counts per brand and per user
    pass


def max_ad_value_optimized(ads: List[Tuple[str, str, int]], brand_limit: int, user_limit: int) -> int:
    """
    Optimized version using more efficient data structures.

    Same interface as max_ad_value but potentially faster.
    """
    # TODO: Implement optimized version
    # Hint: Use dictionaries to track brand/user counts
    pass
