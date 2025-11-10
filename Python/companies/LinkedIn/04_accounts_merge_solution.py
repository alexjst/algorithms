"""
Solution for Accounts Merge

Implement your solution below.
"""

from typing import List
from collections import defaultdict

def accountsMerge(accounts: List[List[str]]) -> List[List[str]]:
    """
    Merge accounts that share common emails.

    Args:
        accounts: List of accounts, each account is [name, email1, email2, ...]

    Returns:
        List of merged accounts with emails sorted

    Approach 1 (DFS):
    1. Build a graph where emails are nodes and edges connect emails in same account
    2. Use DFS to find connected components
    3. For each component, collect all emails and assign the name

    Approach 2 (Union-Find):
    1. Use Union-Find to group emails that belong together
    2. Union emails within the same account
    3. Collect emails by their root parent

    Time: O(N * K * log(N * K)) where N = accounts, K = max emails
    Space: O(N * K)
    """
    # TODO: Implement your solution

    # Hints for DFS Approach:
    # 1. Create email_to_name mapping: {email: name}
    # 2. Create graph: {email: [list of connected emails]}
    # 3. For each account, connect all emails to first email
    # 4. DFS to find connected components:
    #    - Use visited set to track processed emails
    #    - For each unvisited email, DFS to collect all connected emails
    #    - Create merged account: [name] + sorted(emails)

    # Hints for Union-Find Approach:
    # 1. Create parent dictionary for Union-Find
    # 2. Implement find() with path compression
    # 3. Implement union() to connect emails
    # 4. Union all emails within each account
    # 5. Group emails by their root parent
    # 6. Format output with names and sorted emails

    raise NotImplementedError("Implement this function")
