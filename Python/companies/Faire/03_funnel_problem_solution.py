#!/usr/bin/env python3
"""
Solution for Problem 3: Funnel Analysis

🚨 ACTUAL FAIRE INTERVIEW PROBLEM - Reconstructed from interview

TODO: Implement the Solution class with compute_funnel_counts method

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

Algorithm hints:
1. Parse funnels: split by comma to get funnel_name and list of steps
2. Parse events: split by comma to get (user_id, timestamp, event_name)
3. Group events by user_id (timestamps already sorted globally)
4. For each funnel, track user progress through steps
5. Format output as CSV

Key insights:
- Repeated steps in funnel require separate matching events
- Events not in order are ignored (state machine doesn't advance)
- Each funnel is evaluated independently
"""

import pytest
from typing import List
from collections import defaultdict


class Solution:
    def compute_funnel_counts(
        self,
        funnels: List[str],
        events: List[str]
    ) -> List[str]:
        """
        Compute, for each funnel, how many distinct users reach each step in order.

        :param funnels: List of strings, each formatted:
                        "funnel_name,step_1,step_2,...,step_n"
        :param events:  List of strings, each formatted:
                        "user_id,timestamp,event_name"
        :return: List of strings, one per funnel, formatted:
                 "funnel_name,step_1(count_1),step_2(count_2),...,step_n(count_n)"
        """
        # TODO: Implement your solution here
        pass


# Optional: Write your own test cases here
if __name__ == "__main__":
    # Example from problem description
    funnels = [
        "checkout_process,view_product,add_to_cart,enter_payment_info,complete_order",
        "three_clicks_then_add,click_product,click_product,click_product,add_to_cart"
    ]

    events = [
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
        "7,3005,click_product"
    ]

    sol = Solution()
    result = sol.compute_funnel_counts(funnels, events)
    print(f"Result: {result}")

    # Expected:
    # ["checkout_process,view_product(2),add_to_cart(2),enter_payment_info(2),complete_order(1)",
    #  "three_clicks_then_add,click_product(2),click_product(2),click_product(1),add_to_cart(1)"]
