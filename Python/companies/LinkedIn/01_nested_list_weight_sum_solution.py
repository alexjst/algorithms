"""
Solution for Nested List Weight Sum

Implement your solution below.
"""

from typing import List

# This is the interface that allows for creating nested lists.
class NestedInteger:
    def isInteger(self) -> bool:
        """
        @return True if this NestedInteger holds a single integer, rather than a nested list.
        """
        pass

    def getInteger(self) -> int:
        """
        @return the single integer that this NestedInteger holds, if it holds a single integer
        Return None if this NestedInteger holds a nested list
        """
        pass

    def getList(self) -> List['NestedInteger']:
        """
        @return the nested list that this NestedInteger holds, if it holds a nested list
        Return None if this NestedInteger holds a single integer
        """
        pass


def depthSum(nestedList: List[NestedInteger]) -> int:
    """
    Calculate the depth sum of a nested list of integers.

    Args:
        nestedList: List of NestedInteger objects

    Returns:
        Sum of each integer multiplied by its depth

    Approach:
        Use DFS/recursion to traverse the nested structure.
        Keep track of the current depth and add integer * depth to the sum.

    Time: O(n) where n is total number of integers
    Space: O(d) where d is max depth (recursion stack)
    """
    # TODO: Implement your solution
    # Hint: Use a helper function dfs(nested, depth) that returns the sum
    # For each item in nested:
    #   - If it's an integer: add item.getInteger() * depth
    #   - If it's a list: recursively call dfs(item.getList(), depth + 1)

    raise NotImplementedError("Implement this function")
