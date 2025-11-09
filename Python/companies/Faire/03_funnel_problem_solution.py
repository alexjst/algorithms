#!/usr/bin/env python3
"""
Solution for Problem 3: Funnel Problem

🚨 ACTUAL FAIRE INTERVIEW PROBLEM - Asked 4+ times

Problem: Analyze user conversion funnel through multiple stages.
Track users' progression through: Browse → View → Cart → Checkout → Purchase

TODO: Implement the FunnelAnalyzer class below.

Key Methods:
- get_funnel_metrics(): Return conversion stats for each stage
- get_user_journey(user_id): Return list of stages user went through
- find_dropoff_stage(): Find stage with highest drop-off rate

Edge Cases:
- Users can skip stages (Browse → Purchase)
- Users can repeat same stage (count only once)
- Empty events list
- Division by zero when no users at a stage
"""

from typing import List, Tuple, Dict, Set
from collections import defaultdict


class FunnelAnalyzer:
    """
    Analyze user conversion funnel.

    Funnel stages (in order):
    1. Browse
    2. View
    3. Cart
    4. Checkout
    5. Purchase
    """

    def __init__(self, events: List[Tuple[str, str, int]]):
        """
        Initialize analyzer with user events.

        Args:
            events: List of (user_id, stage, timestamp) tuples
                   Example: [('u1', 'Browse', 1), ('u1', 'View', 2), ('u2', 'Browse', 1)]
        """
        # TODO: Implement initialization
        # Hint: Store events and build data structures for:
        #   - Which users reached each stage
        #   - User journeys (ordered list of stages per user)
        #   - Stage order for conversion calculation
        pass

    def get_funnel_metrics(self) -> Dict[str, Dict]:
        """
        Get metrics for each funnel stage.

        Returns:
            Dictionary with stage names as keys, metrics as values:
            {
                'Browse': {
                    'total_users': 100,
                    'conversion_from_previous': 100.0  # Always 100% for first stage
                },
                'View': {
                    'total_users': 50,
                    'conversion_from_previous': 50.0   # 50 out of 100
                },
                ...
            }
        """
        # TODO: Implement metrics calculation
        pass

    def get_user_journey(self, user_id: str) -> List[str]:
        """
        Get the ordered list of stages a user went through.

        Args:
            user_id: User identifier

        Returns:
            List of stage names in chronological order
            Example: ['Browse', 'View', 'Cart', 'Purchase']
        """
        # TODO: Implement user journey retrieval
        pass

    def find_dropoff_stage(self) -> Tuple[str, float]:
        """
        Find the stage with the highest drop-off rate.

        Returns:
            Tuple of (stage_name, dropoff_percentage)
            Example: ('View -> Cart', 66.7)
        """
        # TODO: Implement drop-off calculation
        # Hint: Compare users at consecutive stages
        pass
