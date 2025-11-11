#!/usr/bin/env python3
"""
Solution for Problem 3: Funnel Analysis

🚨 ACTUAL FAIRE INTERVIEW PROBLEM - Reconstructed from interview

Algorithm:
1. Parse funnels: split by comma to get funnel_name and list of steps
2. Parse events: split by comma to get (user_id, timestamp, event_name)
3. Group events by user_id (timestamps already sorted globally)
4. For each funnel, track user progress through steps:
   - Maintain state: which step each user is currently on
   - Process events in timestamp order for each user
   - When event matches next required step, advance user's position
   - Count distinct users who reached each step
5. Format output as CSV

Key insights:
- Repeated steps in funnel require separate matching events
- Events not in order are ignored (state machine doesn't advance)
- Each funnel is evaluated independently

Time Complexity: O(F * E) where F = funnels, E = events
Space Complexity: O(U * F) where U = unique users, F = funnels (track state per user per funnel)
"""

from typing import List, Dict, Tuple
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
            # step_users[i] = set of users who reached step i
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


# Alternative implementation with more detailed comments
class SolutionVerbose:
    def compute_funnel_counts(self, funnels: List[str], events: List[str]) -> List[str]:
        """
        More verbose implementation with detailed comments.
        """
        # Step 1: Parse funnel definitions
        funnel_definitions = []
        for funnel_csv in funnels:
            parts = funnel_csv.split(',')
            name = parts[0]
            steps = parts[1:]
            funnel_definitions.append({
                'name': name,
                'steps': steps
            })

        # Step 2: Parse user events and organize by user
        events_by_user = defaultdict(list)
        for event_csv in events:
            parts = event_csv.split(',')
            user_id = int(parts[0])
            timestamp = int(parts[1])
            event_name = parts[2]

            events_by_user[user_id].append({
                'timestamp': timestamp,
                'event_name': event_name
            })

        # Step 3: Events already sorted by timestamp (guaranteed by problem)

        # Step 4: Process each funnel
        output_lines = []

        for funnel_def in funnel_definitions:
            funnel_name = funnel_def['name']
            funnel_steps = funnel_def['steps']
            num_steps = len(funnel_steps)

            # Track users who reached each step
            users_at_step = [set() for _ in range(num_steps)]

            # Step 5: Simulate each user's journey through this funnel
            for user_id, user_event_list in events_by_user.items():
                # User's current position in the funnel (step index)
                position = 0  # Starts before first step

                # Process user's events in chronological order
                for event in user_event_list:
                    event_name = event['event_name']

                    # Check if this event advances the user in the funnel
                    if position < num_steps and event_name == funnel_steps[position]:
                        # User reached this step
                        users_at_step[position].add(user_id)
                        position += 1

                        # Early termination if user completed entire funnel
                        if position >= num_steps:
                            break

            # Step 6: Format output for this funnel
            output_parts = [funnel_name]
            for step_idx, step_name in enumerate(funnel_steps):
                user_count = len(users_at_step[step_idx])
                output_parts.append(f"{step_name}({user_count})")

            output_line = ','.join(output_parts)
            output_lines.append(output_line)

        return output_lines


if __name__ == "__main__":
    print("=== Funnel Analysis Solution Examples ===\n")

    # Example 1: Basic funnel
    print("Example 1: Basic checkout funnel")
    funnels1 = ["checkout,view,add,purchase"]
    events1 = [
        "1,100,view",
        "1,200,add",
        "1,300,purchase",
        "2,100,view",
        "2,200,add"
    ]

    sol = Solution()
    result1 = sol.compute_funnel_counts(funnels1, events1)
    print(f"Funnels: {funnels1}")
    print(f"Events: {events1}")
    print(f"Result: {result1}")
    print("Explanation: User 1 completes all steps, User 2 stops at 'add'\n")

    # Example 2: Repeated steps
    print("Example 2: Funnel with repeated steps")
    funnels2 = ["triple_click,click,click,click,buy"]
    events2 = [
        "1,100,click",
        "1,200,click",
        "1,300,click",
        "1,400,buy",
        "2,100,click",
        "2,200,click"
    ]

    result2 = sol.compute_funnel_counts(funnels2, events2)
    print(f"Funnels: {funnels2}")
    print(f"Events: {events2}")
    print(f"Result: {result2}")
    print("Explanation: User 1 does 3 clicks then buy. User 2 only does 2 clicks.\n")

    # Example 3: Out of order events
    print("Example 3: Events not in funnel order")
    funnels3 = ["ordered,a,b,c"]
    events3 = [
        "1,100,b",  # Wrong order - ignored
        "1,200,a",  # Correct - matches step 1
        "1,300,c",  # Wrong - skips step 2 (b)
        "1,400,b",  # Correct - matches step 2
        "1,500,c"   # Correct - matches step 3
    ]

    result3 = sol.compute_funnel_counts(funnels3, events3)
    print(f"Funnels: {funnels3}")
    print(f"Events: {events3}")
    print(f"Result: {result3}")
    print("Explanation: Only events matching current step advance the funnel\n")
