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
        # Your code here
        pass


# Write your test cases here
if __name__ == "__main__":
    # Example test case
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

    # Expected output:
    # ["checkout_process,view_product(2),add_to_cart(2),enter_payment_info(2),complete_order(1)",
    #  "three_clicks_then_add,click_product(2),click_product(2),click_product(1),add_to_cart(1)"]
