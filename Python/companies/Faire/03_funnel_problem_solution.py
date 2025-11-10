#!/usr/bin/env python3
"""
Solution for Problem 3: Funnel Problem

🚨 ACTUAL FAIRE INTERVIEW PROBLEM - Asked 4+ times

Problem: Analyze user conversion funnel through multiple stages.
Track users' progression through: Browse → View → Cart → Checkout → Purchase

Key Approach:
- Use hash map: stage → set of users who reached that stage
- Calculate conversion rates between consecutive stages
- Find biggest drop-off between stages
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

    STAGE_ORDER = ['Browse', 'View', 'Cart', 'Checkout', 'Purchase']

    def __init__(self, events: List[Tuple[str, str, int]]):
        """
        Initialize analyzer with user events.

        Args:
            events: List of (user_id, stage, timestamp) tuples
                   Example: [('u1', 'Browse', 1), ('u1', 'View', 2), ('u2', 'Browse', 1)]

        Time: O(n) where n = number of events
        Space: O(n) to store user sets per stage
        """
        # Track which users reached each stage (users can skip stages!)
        self.stage_users = defaultdict(set)  # {stage: set of user_ids}

        # Track user journeys in chronological order
        self.user_journeys = defaultdict(list)  # {user_id: [(stage, timestamp)]}

        # Process events
        for user_id, stage, timestamp in events:
            # Add user to this stage (set handles duplicates automatically)
            self.stage_users[stage].add(user_id)

            # Track journey
            self.user_journeys[user_id].append((stage, timestamp))

        # Sort each user's journey by timestamp
        for user_id in self.user_journeys:
            self.user_journeys[user_id].sort(key=lambda x: x[1])

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

        Time: O(s) where s = number of stages (constant = 5)
        """
        metrics = {}

        for i, stage in enumerate(self.STAGE_ORDER):
            current_users = len(self.stage_users[stage])

            # Calculate conversion from previous stage
            if i == 0:
                # First stage: always 100% (no previous stage)
                conversion = 100.0
            else:
                # Find previous non-empty stage
                prev_users = 0
                for j in range(i - 1, -1, -1):
                    prev_stage = self.STAGE_ORDER[j]
                    prev_users = len(self.stage_users[prev_stage])
                    if prev_users > 0:
                        break

                # Calculate conversion
                if prev_users > 0:
                    conversion = (current_users / prev_users) * 100
                else:
                    conversion = 0.0 if current_users == 0 else 100.0

            metrics[stage] = {
                'total_users': current_users,
                'conversion_from_previous': round(conversion, 2)
            }

        return metrics

    def get_user_journey(self, user_id: str) -> List[str]:
        """
        Get the ordered list of stages a user went through.

        Args:
            user_id: User identifier

        Returns:
            List of stage names in chronological order
            Example: ['Browse', 'View', 'Cart', 'Purchase']

        Time: O(1) - already pre-sorted
        """
        if user_id not in self.user_journeys:
            return []

        # Return just the stage names (without timestamps)
        return [stage for stage, timestamp in self.user_journeys[user_id]]

    def find_dropoff_stage(self) -> Tuple[str, float]:
        """
        Find the stage-to-stage transition with the highest drop-off rate.

        Returns:
            Tuple of (transition_name, dropoff_percentage)
            Example: ('View -> Cart', 66.7)
            Returns ('', 0.0) if no drop-offs

        Key Insight:
        - Drop-off is calculated between consecutive stages
        - If user skips from Browse to Purchase, they "dropped off" from View, Cart, Checkout
        - Even though they eventually converted!

        Time: O(s) where s = number of stages (constant = 5)
        """
        max_dropoff_rate = 0.0
        max_dropoff_stage = ""

        # Check each consecutive pair of stages
        for i in range(len(self.STAGE_ORDER) - 1):
            current_stage = self.STAGE_ORDER[i]
            next_stage = self.STAGE_ORDER[i + 1]

            current_users = len(self.stage_users[current_stage])
            next_users = len(self.stage_users[next_stage])

            # Calculate drop-off rate
            if current_users > 0:
                dropoff_rate = ((current_users - next_users) / current_users) * 100

                if dropoff_rate > max_dropoff_rate:
                    max_dropoff_rate = dropoff_rate
                    max_dropoff_stage = f"{current_stage} -> {next_stage}"

        return (max_dropoff_stage, round(max_dropoff_rate, 2))


if __name__ == "__main__":
    # Example usage
    events = [
        ('u1', 'Browse', 1),
        ('u1', 'View', 2),
        ('u1', 'Cart', 3),
        ('u1', 'Purchase', 5),  # u1 skips Checkout!
        ('u2', 'Browse', 1),
        ('u2', 'View', 2),
        ('u3', 'Browse', 1),
    ]

    analyzer = FunnelAnalyzer(events)

    print("=== Funnel Metrics ===")
    metrics = analyzer.get_funnel_metrics()
    for stage, data in metrics.items():
        print(f"{stage}: {data['total_users']} users ({data['conversion_from_previous']}% conversion)")

    print("\n=== User Journeys ===")
    for user in ['u1', 'u2', 'u3']:
        journey = analyzer.get_user_journey(user)
        print(f"{user}: {' -> '.join(journey)}")

    print("\n=== Biggest Drop-off ===")
    dropoff_stage, dropoff_rate = analyzer.find_dropoff_stage()
    print(f"{dropoff_stage}: {dropoff_rate}% drop-off")
