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
        """
        - Create a map of "funnel_name : dictionary(step_name, distinct_users_set)" -> this will turn into the result
        - Create a map of "funnel_name : dictionary(step_name: step_idx)"
        - Create a map of "funnel_name : dictionary(step_idx: step_name) -> or a list"
        - Create a map of "funnel_name : dictionary(user_name: step_idx)"
        - Scan funnel definitions to get map from step_name : set of funnels.

        Now scan events:
            - user, timestamp, event/step
                - from step, find list of funnels.
                    - for each funnel, find idx of that step, find idx of that user too
                        - if idx of user is not found:
                            - add user to step
                        - if idx is found:
                            if idx is last upper limit, skip
                            if idx is not the last, move user from idx to idx+1

        build final result.
        """
        funnel_step_user = defaultdict(lambda: defaultdict(set))
        funnel_step = defaultdict(lambda: defaultdict(int))
        funnel_steps = defaultdict(list)
        funnel_user = defaultdict(lambda: defaultdict(int))
        step_funnel = defaultdict(set)

        # build funnel_step, step_funnel
        for funnel_row in funnels:
            parts = funnel_row.split(",")
            funnel = parts[0]
            steps = parts[1:]
            funnel_steps[funnel] = steps
            for i, step in enumerate(steps):
                funnel_step[funnel][step] = i
                step_funnel[step].add(funnel)

        for event in events:
            user, timestamp, step = event.split(",")
            funnels = step_funnel[step]
            for funnel in funnels:
                if user not in funnel_user[funnel]:
                    funnel_user[funnel][user] = 0
                    funnel_step_user[funnel][step].add(user)
                else:
                    step_idx = funnel_user[funnel]
                    if step_idx >= len(funnel_step[funnel]):
                        continue
                    else:
                        funnel_user[funnel][user] += 1
                        funnel_step_user[funnel][step].add(user)

        result = []
        for funnel_row in funnels:
            parts = funnel_row.split(",")
            funnel = parts[0]
            steps = parts[1:]
            step_count = []
            for i, step in enumerate(steps):
                user_count = len(funnel_step_user[funnel][step])
                step_count.append(step + "(" + str(user_count) + "|")
            step_count_str =  ",".join(step_count)
            result.append(",".join[funnel, step_count_str])

        return result 

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
