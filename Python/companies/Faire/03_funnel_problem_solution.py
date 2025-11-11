#!/usr/bin/env python3
"""
Solution for Problem 3: Funnel Analysis

🚨 ACTUAL FAIRE INTERVIEW PROBLEM - Reconstructed from interview

TODO: Implement the Solution class with compute_funnel_counts method

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
    # Example test
    funnels = ["checkout,view,add,purchase"]
    events = [
        "1,100,view",
        "1,200,add",
        "1,300,purchase",
        "2,100,view",
        "2,200,add"
    ]

    sol = Solution()
    result = sol.compute_funnel_counts(funnels, events)
    print(f"Result: {result}")
    # Expected: ["checkout,view(2),add(2),purchase(1)"]
