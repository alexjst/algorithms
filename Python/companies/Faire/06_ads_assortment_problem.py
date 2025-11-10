#!/usr/bin/env python3
"""
Problem 6: Ad Blocking System

🚨 CONFIRMED FAIRE INTERVIEW PROBLEM (Asked 2022)

Given a list of ads that were already sent, determine which customers should
be blocked from receiving a new advertisement.

A customer should be BLOCKED from receiving a new ad if:
1. They already received the SAME ad in the same week, OR
2. They already received 3 or more ads in the same week

Input:
- sent_ads: List of tuples (ad_name, customer, day_number)
  - ad_name: string identifier for the ad
  - customer: string identifier for the customer
  - day_number: integer day number (days 1-7 are week 1, 8-14 are week 2, etc.)

- new_ad: Tuple (ad_name, customer, day_number) representing the ad to send

Output:
- List of customer IDs who should be BLOCKED from receiving the new ad

Example 1:
    Input:
        sent_ads = [
            ('ad1', 'alice', 1),
            ('ad2', 'alice', 2),
            ('ad3', 'alice', 3),
            ('ad1', 'bob', 1)
        ]
        new_ad = ('ad4', 'alice', 4)
    Output: ['alice']
    Explanation: Alice already received 3 ads in week 1 (days 1-7)

Example 2:
    Input:
        sent_ads = [
            ('ad1', 'alice', 1),
            ('ad2', 'bob', 2)
        ]
        new_ad = ('ad1', 'alice', 5)
    Output: ['alice']
    Explanation: Alice already received 'ad1' in week 1

Example 3:
    Input:
        sent_ads = [
            ('ad1', 'alice', 1),
            ('ad2', 'alice', 8)
        ]
        new_ad = ('ad3', 'alice', 10)
    Output: []
    Explanation: Alice has 1 ad in week 1, 1 ad in week 2.
                 New ad is in week 2, so only 2 total ads in week 2. Not blocked.

Constraints:
    - 1 <= len(sent_ads) <= 10000
    - 1 <= day_number <= 365
    - Weeks are defined as: days 1-7 = week 1, days 8-14 = week 2, etc.
    - Week number = (day_number - 1) // 7 + 1

================================================================================
INSTRUCTIONS:
- Implement your solution in: 06_ads_assortment_problem_solution.py
- Run this file to test: python 06_ads_assortment_problem.py
- To reset and practice again: just delete/reset the solution file
================================================================================
"""

# Import the solution
try:
    import importlib.util
    spec = importlib.util.spec_from_file_location(
        "solution_module",
        "06_ads_assortment_problem_solution.py"
    )
    solution_module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(solution_module)
    get_blocked_customers = solution_module.get_blocked_customers
except Exception as e:
    print(f"❌ Error importing solution: {e}")
    print(f"   Make sure 06_ads_assortment_problem_solution.py exists.")
    exit(1)

def run_tests():
    """Run test cases for ad blocking system."""

    # Test Case 1: Customer reached 3 ads limit in the week
    sent_ads1 = [
        ('ad1', 'alice', 1),
        ('ad2', 'alice', 2),
        ('ad3', 'alice', 3),
        ('ad1', 'bob', 1)
    ]
    new_ad1 = ('ad4', 'alice', 4)
    result1 = get_blocked_customers(sent_ads1, new_ad1)
    assert result1 == ['alice'], f"Test 1 failed: expected ['alice'], got {result1}"
    print("✓ Test 1 passed: Customer blocked - 3 ads limit reached")

    # Test Case 2: Customer already received same ad in the week
    sent_ads2 = [
        ('ad1', 'alice', 1),
        ('ad2', 'bob', 2)
    ]
    new_ad2 = ('ad1', 'alice', 5)
    result2 = get_blocked_customers(sent_ads2, new_ad2)
    assert result2 == ['alice'], f"Test 2 failed: expected ['alice'], got {result2}"
    print("✓ Test 2 passed: Customer blocked - same ad in week")

    # Test Case 3: Customer not blocked (different week)
    sent_ads3 = [
        ('ad1', 'alice', 1),
        ('ad2', 'alice', 8)
    ]
    new_ad3 = ('ad3', 'alice', 10)
    result3 = get_blocked_customers(sent_ads3, new_ad3)
    assert result3 == [], f"Test 3 failed: expected [], got {result3}"
    print("✓ Test 3 passed: Customer not blocked - different week")

    # Test Case 4: Customer not blocked (only 2 ads in week)
    sent_ads4 = [
        ('ad1', 'alice', 1),
        ('ad2', 'alice', 2),
        ('ad3', 'bob', 1)
    ]
    new_ad4 = ('ad4', 'alice', 3)
    result4 = get_blocked_customers(sent_ads4, new_ad4)
    assert result4 == [], f"Test 4 failed: expected [], got {result4}"
    print("✓ Test 4 passed: Customer not blocked - only 2 ads in week")

    # Test Case 5: Multiple customers, some blocked
    sent_ads5 = [
        ('ad1', 'alice', 1),
        ('ad2', 'alice', 2),
        ('ad3', 'alice', 3),
        ('ad1', 'bob', 1),
        ('ad2', 'bob', 2)
    ]
    new_ad5 = ('ad4', 'charlie', 4)
    result5 = get_blocked_customers(sent_ads5, new_ad5)
    assert result5 == [], f"Test 5 failed: expected [], got {result5}"
    print("✓ Test 5 passed: New customer not blocked")

    # Test Case 6: Edge case - exactly at week boundary
    sent_ads6 = [
        ('ad1', 'alice', 7),  # Last day of week 1
        ('ad2', 'alice', 8)   # First day of week 2
    ]
    new_ad6 = ('ad3', 'alice', 9)  # Week 2
    result6 = get_blocked_customers(sent_ads6, new_ad6)
    assert result6 == [], f"Test 6 failed: expected [], got {result6}"
    print("✓ Test 6 passed: Week boundary handling")

    # Test Case 7: Same ad different week - not blocked
    sent_ads7 = [
        ('ad1', 'alice', 1)
    ]
    new_ad7 = ('ad1', 'alice', 8)  # Same ad but week 2
    result7 = get_blocked_customers(sent_ads7, new_ad7)
    assert result7 == [], f"Test 7 failed: expected [], got {result7}"
    print("✓ Test 7 passed: Same ad different week - allowed")

    # Test Case 8: Complex scenario with multiple weeks
    sent_ads8 = [
        ('ad1', 'alice', 1),
        ('ad2', 'alice', 2),
        ('ad3', 'alice', 8),
        ('ad4', 'alice', 9),
        ('ad5', 'alice', 10)
    ]
    new_ad8 = ('ad6', 'alice', 11)  # Week 2, already has 3 ads
    result8 = get_blocked_customers(sent_ads8, new_ad8)
    assert result8 == ['alice'], f"Test 8 failed: expected ['alice'], got {result8}"
    print("✓ Test 8 passed: 3 ads limit in week 2")

    print("\n" + "="*50)
    print("All basic tests passed! ✓")
    print("="*50)



def run_custom_tests():
    """Add your own custom test cases here."""
    print("\nRunning custom tests...")

    # Add your custom test cases here

    print("No custom tests defined yet.")



if __name__ == "__main__":
    print("Testing Ad Blocking System Solution")
    print("="*50 + "\n")

    try:
        run_tests()
        run_custom_tests()
    except AssertionError as e:
        print(f"\n❌ Test failed: {e}")
    except Exception as e:
        print(f"\n❌ Error: {e}")
