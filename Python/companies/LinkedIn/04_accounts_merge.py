"""
Problem 4: Accounts Merge (Medium)

**LinkedIn Signature Problem - VERY High Frequency**
**Directly Related to LinkedIn's Social Graph**

Given a list of accounts where each element accounts[i] is a list of strings, where
the first element accounts[i][0] is a name, and the rest of the elements are emails
representing emails of the account.

Now, we would like to merge these accounts. Two accounts definitely belong to the
same person if there is some common email to both accounts. Note that even if two
accounts have the same name, they may belong to different people as people could have
the same name. A person can have any number of accounts initially, but all of their
accounts definitely have the same name.

After merging the accounts, return the accounts in the following format: the first
element of each account is the name, and the rest of the elements are emails in sorted
order. The accounts themselves can be returned in any order.

Example 1:
Input: accounts = [
  ["John","johnsmith@mail.com","john_newyork@mail.com"],
  ["John","johnsmith@mail.com","john00@mail.com"],
  ["Mary","mary@mail.com"],
  ["John","johnnybravo@mail.com"]
]
Output: [
  ["John","john00@mail.com","john_newyork@mail.com","johnsmith@mail.com"],
  ["Mary","mary@mail.com"],
  ["John","johnnybravo@mail.com"]
]
Explanation:
The first and second John are the same person (common email johnsmith@mail.com).
The third John and Mary are different people as none of their emails are shared.

Example 2:
Input: accounts = [
  ["Gabe","Gabe0@m.co","Gabe3@m.co","Gabe1@m.co"],
  ["Kevin","Kevin3@m.co","Kevin5@m.co","Kevin0@m.co"],
  ["Ethan","Ethan5@m.co","Ethan4@m.co","Ethan0@m.co"],
  ["Hanzo","Hanzo3@m.co","Hanzo1@m.co","Hanzo0@m.co"],
  ["Fern","Fern5@m.co","Fern1@m.co","Fern0@m.co"]
]
Output: [
  ["Ethan","Ethan0@m.co","Ethan4@m.co","Ethan5@m.co"],
  ["Gabe","Gabe0@m.co","Gabe1@m.co","Gabe3@m.co"],
  ["Hanzo","Hanzo0@m.co","Hanzo1@m.co","Hanzo3@m.co"],
  ["Kevin","Kevin0@m.co","Kevin3@m.co","Kevin5@m.co"],
  ["Fern","Fern0@m.co","Fern1@m.co","Fern5@m.co"]
]

Constraints:
- 1 <= accounts.length <= 1000
- 2 <= accounts[i].length <= 10
- 1 <= accounts[i][j].length <= 30
- accounts[i][0] consists of English letters
- accounts[i][j] (for j > 0) is a valid email

Approaches:
1. DFS/BFS: Build graph of connected emails, then traverse
2. Union-Find (Disjoint Set Union): More efficient for merging

Time Complexity: O(N * K * log(N * K)) where N is accounts, K is max emails
Space Complexity: O(N * K)

Implement your solution in 04_accounts_merge_solution.py
"""

from typing import List

# Import the solution
try:
    from importlib import import_module
    solution = import_module('04_accounts_merge_solution')
    accountsMerge = solution.accountsMerge
except (ImportError, AttributeError):
    def accountsMerge(accounts: List[List[str]]) -> List[List[str]]:
        raise NotImplementedError("Implement accountsMerge in 04_accounts_merge_solution.py")


def test_accounts_merge():
    print("Testing Accounts Merge...\n")

    # Test 1: Example 1 from problem
    print("Test 1: Basic merge with common emails")
    accounts1 = [
        ["John", "johnsmith@mail.com", "john_newyork@mail.com"],
        ["John", "johnsmith@mail.com", "john00@mail.com"],
        ["Mary", "mary@mail.com"],
        ["John", "johnnybravo@mail.com"]
    ]
    result1 = accountsMerge(accounts1)
    # Sort for comparison
    result1_sorted = sorted([sorted(acc) for acc in result1])
    expected1_sorted = sorted([
        sorted(["John", "john00@mail.com", "john_newyork@mail.com", "johnsmith@mail.com"]),
        sorted(["Mary", "mary@mail.com"]),
        sorted(["John", "johnnybravo@mail.com"])
    ])
    assert result1_sorted == expected1_sorted, f"Test 1 failed: {result1_sorted} != {expected1_sorted}"
    print(f"✓ Test 1 passed\n")

    # Test 2: All accounts belong to same person
    print("Test 2: All accounts merge into one")
    accounts2 = [
        ["John", "a@mail.com", "b@mail.com"],
        ["John", "b@mail.com", "c@mail.com"],
        ["John", "c@mail.com", "d@mail.com"]
    ]
    result2 = accountsMerge(accounts2)
    assert len(result2) == 1, f"Test 2a failed: should have 1 account, got {len(result2)}"
    assert len(result2[0]) == 5, f"Test 2b failed: should have 5 elements (name + 4 emails)"  # John + 4 emails
    print(f"✓ Test 2 passed\n")

    # Test 3: No merge needed
    print("Test 3: No common emails - no merge")
    accounts3 = [
        ["John", "a@mail.com"],
        ["Mary", "b@mail.com"],
        ["Jane", "c@mail.com"]
    ]
    result3 = accountsMerge(accounts3)
    assert len(result3) == 3, f"Test 3 failed: should have 3 accounts, got {len(result3)}"
    print(f"✓ Test 3 passed\n")

    # Test 4: Same name, different people
    print("Test 4: Same name but different people")
    accounts4 = [
        ["John", "john1@mail.com"],
        ["John", "john2@mail.com"],
        ["John", "john3@mail.com"]
    ]
    result4 = accountsMerge(accounts4)
    assert len(result4) == 3, f"Test 4 failed: should have 3 accounts, got {len(result4)}"
    print(f"✓ Test 4 passed\n")

    # Test 5: Chain of connections
    print("Test 5: Chain merging (A-B, B-C, C-D)")
    accounts5 = [
        ["John", "a@mail.com", "b@mail.com"],
        ["John", "c@mail.com"],
        ["John", "b@mail.com", "c@mail.com"],
        ["John", "d@mail.com", "c@mail.com"]
    ]
    result5 = accountsMerge(accounts5)
    assert len(result5) == 1, f"Test 5 failed: should merge into 1 account, got {len(result5)}"
    print(f"✓ Test 5 passed\n")

    # Test 6: Single account
    print("Test 6: Single account")
    accounts6 = [["David", "david@mail.com", "david2@mail.com"]]
    result6 = accountsMerge(accounts6)
    assert len(result6) == 1, "Test 6 failed"
    assert result6[0][0] == "David", "Test 6 failed: name should be David"
    print(f"✓ Test 6 passed\n")

    print("All tests passed! ✓")


if __name__ == "__main__":
    test_accounts_merge()
