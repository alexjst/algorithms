#!/usr/bin/env python3
"""
Solution for Problem 6: Ad Blocking System

🚨 CONFIRMED FAIRE INTERVIEW PROBLEM (Asked 2022)

Problem: Given a list of ads that were already sent, determine which customers
should be blocked from receiving a new advertisement.

Block Rules:
1. Customer already received the SAME ad in the same week
2. Customer already received 3 or more ads in the same week

Key Approach:
- Calculate week number from day number: week = (day - 1) // 7 + 1
- Group sent ads by customer and week
- Check blocking conditions for the new ad

Time Complexity: O(n) where n is number of sent ads
Space Complexity: O(n) for tracking customer ad history
"""

from typing import List, Tuple
from collections import defaultdict


def get_blocked_customers(sent_ads: List[Tuple[str, str, int]], new_ad: Tuple[str, str, int]) -> List[str]:
    """
    Determine which customers should be blocked from receiving the new ad.

    Args:
        sent_ads: List of (ad_name, customer, day_number) tuples
        new_ad: Tuple (ad_name, customer, day_number) for the new ad to send

    Returns:
        List of customer IDs who should be BLOCKED from receiving the new ad

    Examples:
        >>> sent_ads = [('ad1', 'alice', 1), ('ad2', 'alice', 2), ('ad3', 'alice', 3)]
        >>> new_ad = ('ad4', 'alice', 4)
        >>> get_blocked_customers(sent_ads, new_ad)
        ['alice']  # Alice already has 3 ads in week 1

        >>> sent_ads = [('ad1', 'alice', 1)]
        >>> new_ad = ('ad1', 'alice', 5)
        >>> get_blocked_customers(sent_ads, new_ad)
        ['alice']  # Alice already received 'ad1' in week 1
    """
    # Extract new ad information
    new_ad_name, new_customer, new_day = new_ad
    new_week = (new_day - 1) // 7 + 1

    # TODO: Build data structure to track:
    # 1. Which ads each customer received in each week
    # 2. How many ads each customer received in each week

    # Hint: Use nested dictionaries
    # customer_ads[customer][week] = set of ad names
    # customer_counts[customer][week] = count of ads

    customer_ads = defaultdict(lambda: defaultdict(set))
    customer_counts = defaultdict(lambda: defaultdict(int))

    # TODO: Process all sent ads
    for ad_name, customer, day in sent_ads:
        week = (day - 1) // 7 + 1
        customer_ads[customer][week].add(ad_name)
        customer_counts[customer][week] += 1

    # TODO: Check blocking conditions for the new customer
    blocked = []

    # Check if customer should be blocked
    # Condition 1: Same ad already received in the same week
    if new_ad_name in customer_ads[new_customer][new_week]:
        blocked.append(new_customer)
    # Condition 2: Customer already has 3 ads in the week
    elif customer_counts[new_customer][new_week] >= 3:
        blocked.append(new_customer)

    return blocked


# Alternative implementation with more explicit logic
def get_blocked_customers_verbose(sent_ads: List[Tuple[str, str, int]], new_ad: Tuple[str, str, int]) -> List[str]:
    """
    More verbose implementation with explicit checks.
    Same functionality as get_blocked_customers but easier to understand.
    """
    new_ad_name, new_customer, new_day = new_ad
    new_week = get_week_number(new_day)

    # Track customer activity by week
    customer_weekly_ads = {}  # {customer: {week: [ad_names]}}

    for ad_name, customer, day in sent_ads:
        week = get_week_number(day)

        if customer not in customer_weekly_ads:
            customer_weekly_ads[customer] = {}

        if week not in customer_weekly_ads[customer]:
            customer_weekly_ads[customer][week] = []

        customer_weekly_ads[customer][week].append(ad_name)

    # Check if customer should be blocked
    blocked = []

    # Check if this customer has any history
    if new_customer in customer_weekly_ads:
        # Check if customer has ads in the new ad's week
        if new_week in customer_weekly_ads[new_customer]:
            ads_in_week = customer_weekly_ads[new_customer][new_week]

            # Condition 1: Same ad already received
            if new_ad_name in ads_in_week:
                blocked.append(new_customer)
            # Condition 2: Already 3 ads in the week
            elif len(ads_in_week) >= 3:
                blocked.append(new_customer)

    return blocked


def get_week_number(day: int) -> int:
    """
    Convert day number to week number.
    Days 1-7 = week 1, days 8-14 = week 2, etc.

    Formula: week = (day - 1) // 7 + 1

    Examples:
        >>> get_week_number(1)
        1
        >>> get_week_number(7)
        1
        >>> get_week_number(8)
        2
        >>> get_week_number(14)
        2
    """
    return (day - 1) // 7 + 1


if __name__ == "__main__":
    print("=== Ad Blocking System Examples ===\n")

    # Example 1: Customer reached 3 ads limit
    print("Example 1: 3 ads limit reached")
    sent_ads1 = [
        ('ad1', 'alice', 1),
        ('ad2', 'alice', 2),
        ('ad3', 'alice', 3)
    ]
    new_ad1 = ('ad4', 'alice', 4)
    result1 = get_blocked_customers(sent_ads1, new_ad1)
    print(f"Sent ads: {sent_ads1}")
    print(f"New ad: {new_ad1}")
    print(f"Blocked: {result1}")
    print(f"Reason: Alice already has 3 ads in week 1\n")

    # Example 2: Same ad in same week
    print("Example 2: Same ad already received")
    sent_ads2 = [
        ('ad1', 'alice', 1),
        ('ad2', 'bob', 2)
    ]
    new_ad2 = ('ad1', 'alice', 5)
    result2 = get_blocked_customers(sent_ads2, new_ad2)
    print(f"Sent ads: {sent_ads2}")
    print(f"New ad: {new_ad2}")
    print(f"Blocked: {result2}")
    print(f"Reason: Alice already received 'ad1' in week 1\n")

    # Example 3: Not blocked - different week
    print("Example 3: Not blocked - different week")
    sent_ads3 = [
        ('ad1', 'alice', 1),
        ('ad2', 'alice', 8)
    ]
    new_ad3 = ('ad3', 'alice', 10)
    result3 = get_blocked_customers(sent_ads3, new_ad3)
    print(f"Sent ads: {sent_ads3}")
    print(f"New ad: {new_ad3}")
    print(f"Blocked: {result3}")
    print(f"Reason: Only 1 ad in week 1, only 1 ad in week 2. New ad is in week 2.\n")

    # Example 4: Week boundary test
    print("Example 4: Week boundary")
    sent_ads4 = [
        ('ad1', 'alice', 7),  # Last day of week 1
        ('ad2', 'alice', 8)   # First day of week 2
    ]
    new_ad4 = ('ad3', 'alice', 9)  # Week 2
    result4 = get_blocked_customers(sent_ads4, new_ad4)
    print(f"Sent ads: {sent_ads4}")
    print(f"New ad: {new_ad4}")
    print(f"Blocked: {result4}")
    print(f"Weeks: day 7 = week {get_week_number(7)}, day 8 = week {get_week_number(8)}")
    print(f"Reason: Day 7 is in week 1, days 8-9 are in week 2. Only 2 ads in week 2.\n")

    # Example 5: Complex scenario
    print("Example 5: Complex scenario - multiple weeks")
    sent_ads5 = [
        ('ad1', 'alice', 1),   # Week 1
        ('ad2', 'alice', 2),   # Week 1
        ('ad3', 'alice', 8),   # Week 2
        ('ad4', 'alice', 9),   # Week 2
        ('ad5', 'alice', 10)   # Week 2
    ]
    new_ad5 = ('ad6', 'alice', 11)  # Week 2
    result5 = get_blocked_customers(sent_ads5, new_ad5)
    print(f"Sent ads: {sent_ads5}")
    print(f"New ad: {new_ad5}")
    print(f"Blocked: {result5}")
    print(f"Reason: Alice has 2 ads in week 1, 3 ads in week 2. Limit reached in week 2.\n")
