#!/usr/bin/env python3
"""
Problem 3: Funnel Analysis (ACTUAL FAIRE INTERVIEW PROBLEM)

🚨 CONFIRMED FAIRE INTERVIEW PROBLEM - Reconstructed from actual interview

Given multiple funnels (sequences of steps) and user events, determine how many
distinct users reached each step of each funnel IN ORDER.

Input 1 - Funnels (CSV format):
    funnel_name,step_1,step_2,...,step_n

    Examples:
    - checkout_process,view_product,add_to_cart,enter_payment_info,complete_order
    - three_clicks_then_add,click_product,click_product,click_product,add_to_cart

    Note: Funnels may contain REPEATED steps (same step name multiple times)

Input 2 - User Events (CSV format):
    user_id,timestamp,event_name

    - user_id: integer user identifier
    - timestamp: integer (guaranteed to be sorted in chronological order)
    - event_name: step name or irrelevant event

    Note: Events are already sorted by timestamp globally

Goal:
    For each funnel, count how many distinct users reached each step IN ORDER.

    Rules:
    - Events are processed in timestamp order for each user
    - User advances to next step only when event matches current required step
    - Repeated steps require separate matching events
    - Each funnel is evaluated independently

Output format:
    funnel_name,step_1(count_1),step_2(count_2),...,step_n(count_n)

Example:
    Funnels:
        checkout_process,view_product,add_to_cart,enter_payment_info,complete_order
        three_clicks_then_add,click_product,click_product,click_product,add_to_cart

    Events:
        4,1200,view_product
        4,1210,add_to_cart
        4,1300,enter_payment_info
        5,1250,view_product
        5,1260,add_to_cart
        5,1270,enter_payment_info
        5,1280,complete_order
        6,2000,click_product
        6,2005,click_product
        6,2010,click_product
        6,2015,add_to_cart
        7,3000,click_product
        7,3005,click_product

    Output:
        checkout_process,view_product(2),add_to_cart(2),enter_payment_info(2),complete_order(1)
        three_clicks_then_add,click_product(2),click_product(2),click_product(1),add_to_cart(1)

    Explanation:
        - checkout_process: Users 4 and 5 both reach view_product, add_to_cart, enter_payment_info
                           Only user 5 completes entire funnel
        - three_clicks_then_add: User 6 does 3 click_product events then add_to_cart
                                Users counted: step1(2), step2(2), step3(1), step4(1)
                                User 6 reaches all 4 steps, User 7 only reaches first 2 clicks

Constraints:
    - 1 <= funnels <= 100
    - 1 <= events <= 10^5
    - Funnel steps may repeat
    - Events not globally sorted (must sort per user)

================================================================================
INSTRUCTIONS:
- Implement your solution in: 03_funnel_problem_solution.py
- Run this file to test: python 03_funnel_problem.py
- To reset and practice again: just delete/reset the solution file
================================================================================
"""

import pytest
from typing import List

# Import the solution
try:
    import importlib.util
    spec = importlib.util.spec_from_file_location(
        "solution_module",
        "03_funnel_problem_solution.py"
    )
    solution_module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(solution_module)
    Solution = solution_module.Solution
except Exception as e:
    print(f"❌ Error importing solution: {e}")
    print(f"   Make sure 03_funnel_problem_solution.py exists.")
    exit(1)


def test_example():
    """Test the example from problem description."""
    funnels = [
        "checkout_process,view_product,add_to_cart,enter_payment_info,complete_order",
        "new_user_signup,visit_landing_page,click_signup,complete_profile,first_purchase",
        "three_clicks_then_add,click_product,click_product,click_product,add_to_cart",
    ]

    events = [
        "1,1000,visit_landing_page",
        "1,1005,click_signup",
        "1,1030,complete_profile",
        "2,1001,visit_landing_page",
        "2,1010,click_signup",
        "2,1020,complete_profile",
        "3,1002,visit_landing_page",
        "3,1100,click_signup",
        "4,1200,view_product",
        "4,1210,add_to_cart",
        "4,1300,enter_payment_info",
        "5,1250,view_product",
        "5,1260,add_to_cart",
        "5,1270,enter_payment_info",
        "5,1280,complete_order",
        "6,2000,click_product",
        "6,2005,click_product",
        "6,2010,click_product",
        "6,2015,add_to_cart",
        "7,3000,click_product",
        "7,3005,click_product",
    ]

    sol = Solution()
    result = sol.compute_funnel_counts(funnels, events)

    expected = [
        "checkout_process,view_product(2),add_to_cart(2),enter_payment_info(2),complete_order(1)",
        "new_user_signup,visit_landing_page(3),click_signup(3),complete_profile(2),first_purchase(0)",
        "three_clicks_then_add,click_product(2),click_product(2),click_product(1),add_to_cart(1)",
    ]

    assert set(result) == set(expected), f"Expected {expected}, got {result}"
    print("✓ Test 1 passed: Main example")


def test_single_user_complete():
    """Test single user completing entire funnel."""
    funnels = ["simple,a,b,c"]
    events = [
        "1,100,a",
        "1,200,b",
        "1,300,c"
    ]

    sol = Solution()
    result = sol.compute_funnel_counts(funnels, events)
    expected = ["simple,a(1),b(1),c(1)"]

    assert set(result) == set(expected)
    print("✓ Test 2 passed: Single user complete funnel")


def test_user_drops_off():
    """Test user dropping off at middle step."""
    funnels = ["dropout,step1,step2,step3"]
    events = [
        "1,100,step1",
        "1,200,step2",
        # User 1 stops here
        "2,100,step1",
        # User 2 stops after step1
    ]

    sol = Solution()
    result = sol.compute_funnel_counts(funnels, events)
    expected = ["dropout,step1(2),step2(1),step3(0)"]

    assert set(result) == set(expected)
    print("✓ Test 3 passed: User drop-off")


def test_out_of_order_events():
    """Test events not matching funnel order are ignored."""
    funnels = ["ordered,first,second,third"]
    events = [
        "1,100,second",  # Out of order - should be ignored
        "1,200,first",
        "1,300,second",  # Now in order
        "1,400,third"
    ]

    sol = Solution()
    result = sol.compute_funnel_counts(funnels, events)
    expected = ["ordered,first(1),second(1),third(1)"]

    assert set(result) == set(expected)
    print("✓ Test 4 passed: Out of order events ignored")


def test_repeated_steps():
    """Test funnel with repeated step names."""
    funnels = ["double_click,click,click,purchase"]
    events = [
        "1,100,click",
        "1,200,click",
        "1,300,purchase",
        "2,100,click",  # Only one click
        "2,200,purchase"  # Doesn't count - missing second click
    ]

    sol = Solution()
    result = sol.compute_funnel_counts(funnels, events)
    expected = ["double_click,click(2),click(1),purchase(1)"]

    assert set(result) == set(expected)
    print("✓ Test 5 passed: Repeated steps")


def test_multiple_users():
    """Test multiple users progressing through funnel at different rates."""
    funnels = ["test,a,b,c"]
    events = [
        "1,100,a",  # User 1 event
        "1,200,b",
        "1,300,c",
        "2,500,a",  # User 2 event (later timestamp)
        "2,600,b"   # User 2 stops at b
    ]

    sol = Solution()
    result = sol.compute_funnel_counts(funnels, events)
    # Both users reach a and b, only user 1 reaches c
    expected = ["test,a(2),b(2),c(1)"]

    assert set(result) == set(expected)
    print("✓ Test 6 passed: Multiple users with different progress")


def run_all_tests():
    """Run all test cases."""
    print("Testing Funnel Analysis Solution")
    print("="*50 + "\n")

    try:
        test_example()
        test_single_user_complete()
        test_user_drops_off()
        test_out_of_order_events()
        test_repeated_steps()
        test_multiple_users()

        print("\n" + "="*50)
        print("All tests passed! ✓")
        print("="*50)
    except AssertionError as e:
        print(f"\n❌ Test failed: {e}")
    except Exception as e:
        print(f"\n❌ Error: {e}")


if __name__ == "__main__":
    run_all_tests()


# ==============================================================================
# REFERENCE SOLUTION (for your reference after attempting the problem)
# ==============================================================================
"""
class SolutionReference:
    def compute_funnel_counts(self, funnels: List[str], events: List[str]) -> List[str]:
        # Parse funnels
        parsed_funnels = []
        for funnel_str in funnels:
            parts = funnel_str.split(',')
            funnel_name = parts[0]
            steps = parts[1:]  # May contain duplicates
            parsed_funnels.append((funnel_name, steps))

        # Parse and group events by user
        user_events = defaultdict(list)  # user_id -> [(timestamp, event_name), ...]
        for event_str in events:
            parts = event_str.split(',')
            user_id = int(parts[0])
            timestamp = int(parts[1])
            event_name = parts[2]
            user_events[user_id].append((timestamp, event_name))

        # Note: Events are already sorted by timestamp globally (guaranteed by problem)

        # Process each funnel
        results = []
        for funnel_name, steps in parsed_funnels:
            # Track which users reached each step index
            step_users = [set() for _ in range(len(steps))]

            # For each user, track their current position in this funnel
            for user_id, events_list in user_events.items():
                current_step_idx = 0  # User starts before step 0

                # Process user's events in timestamp order
                for timestamp, event_name in events_list:
                    # Check if this event matches the next required step
                    if current_step_idx < len(steps) and event_name == steps[current_step_idx]:
                        # User reached this step
                        step_users[current_step_idx].add(user_id)
                        current_step_idx += 1

            # Format output for this funnel
            output_parts = [funnel_name]
            for i, step_name in enumerate(steps):
                count = len(step_users[i])
                output_parts.append(f"{step_name}({count})")

            results.append(','.join(output_parts))

        return results
"""
