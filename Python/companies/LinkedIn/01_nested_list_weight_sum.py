"""
Problem 1: Nested List Weight Sum (Easy)

**LinkedIn Signature Problem - Very High Frequency**

You are given a nested list of integers nestedList. Each element is either an integer
or a list whose elements may also be integers or other lists.

The depth of an integer is the number of lists that it is inside of. For example,
the nested list [1,[2,2],[[3],2],1] has each integer's value set to its depth.

Return the sum of each integer in nestedList multiplied by its depth.

Example 1:
Input: nestedList = [[1,1],2,[1,1]]
Output: 10
Explanation: Four 1's at depth 2, one 2 at depth 1. 1*2 + 1*2 + 2*1 + 1*2 + 1*2 = 10.

Example 2:
Input: nestedList = [1,[4,[6]]]
Output: 27
Explanation: One 1 at depth 1, one 4 at depth 2, and one 6 at depth 3.
1*1 + 4*2 + 6*3 = 27.

Example 3:
Input: nestedList = [0]
Output: 0

Constraints:
- 1 <= nestedList.length <= 50
- The values of the integers in the nested list is in the range [-100, 100]
- The maximum depth of any integer is less than or equal to 50

Approach:
- Use DFS/Recursion to traverse the nested structure
- Keep track of current depth
- Add integer * depth to sum when you encounter an integer

Time Complexity: O(n) where n is total number of integers
Space Complexity: O(d) where d is maximum depth (recursion stack)

Implement your solution in 01_nested_list_weight_sum_solution.py
"""

from typing import List

# This is the interface that allows for creating nested lists.
class NestedInteger:
    def __init__(self, value=None):
        """
        If value is not specified, initializes an empty list.
        Otherwise initializes a single integer equal to value.
        """
        self._value = value
        self._list = [] if value is None else None

    def isInteger(self) -> bool:
        """
        @return True if this NestedInteger holds a single integer, rather than a nested list.
        """
        return self._list is None

    def getInteger(self) -> int:
        """
        @return the single integer that this NestedInteger holds, if it holds a single integer
        Return None if this NestedInteger holds a nested list
        """
        return self._value

    def getList(self) -> List['NestedInteger']:
        """
        @return the nested list that this NestedInteger holds, if it holds a nested list
        Return None if this NestedInteger holds a single integer
        """
        return self._list

    def add(self, elem: 'NestedInteger'):
        """
        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
        """
        if self._list is None:
            self._list = []
        self._list.append(elem)


# Import the solution
try:
    from importlib import import_module
    solution = import_module('01_nested_list_weight_sum_solution')
    depthSum = solution.depthSum
except (ImportError, AttributeError):
    # Fallback if solution file doesn't exist
    def depthSum(nestedList: List[NestedInteger]) -> int:
        raise NotImplementedError("Implement depthSum in 01_nested_list_weight_sum_solution.py")


def create_nested_list(data) -> List[NestedInteger]:
    """
    Helper function to create NestedInteger structure from Python list
    """
    result = []
    for item in data:
        if isinstance(item, list):
            nested = NestedInteger()
            for sub_item in create_nested_list(item):
                nested.add(sub_item)
            result.append(nested)
        else:
            result.append(NestedInteger(item))
    return result


def test_nested_list_weight_sum():
    print("Testing Nested List Weight Sum...\n")

    # Test 1: [[1,1],2,[1,1]]
    print("Test 1: [[1,1],2,[1,1]]")
    nestedList1 = create_nested_list([[1,1],2,[1,1]])
    result1 = depthSum(nestedList1)
    expected1 = 10  # (1*2 + 1*2) + 2*1 + (1*2 + 1*2) = 10
    assert result1 == expected1, f"Test 1 failed: expected {expected1}, got {result1}"
    print(f"✓ Test 1 passed: {result1}\n")

    # Test 2: [1,[4,[6]]]
    print("Test 2: [1,[4,[6]]]")
    nestedList2 = create_nested_list([1,[4,[6]]])
    result2 = depthSum(nestedList2)
    expected2 = 27  # 1*1 + 4*2 + 6*3 = 27
    assert result2 == expected2, f"Test 2 failed: expected {expected2}, got {result2}"
    print(f"✓ Test 2 passed: {result2}\n")

    # Test 3: [0]
    print("Test 3: [0]")
    nestedList3 = create_nested_list([0])
    result3 = depthSum(nestedList3)
    expected3 = 0
    assert result3 == expected3, f"Test 3 failed: expected {expected3}, got {result3}"
    print(f"✓ Test 3 passed: {result3}\n")

    # Test 4: Deep nesting [[[[[1]]]]]
    print("Test 4: [[[[[1]]]]]")
    nestedList4 = create_nested_list([[[[[1]]]]])
    result4 = depthSum(nestedList4)
    expected4 = 5  # 1*5 = 5
    assert result4 == expected4, f"Test 4 failed: expected {expected4}, got {result4}"
    print(f"✓ Test 4 passed: {result4}\n")

    # Test 5: Mix of integers and lists [[1,2],[3,4]]
    print("Test 5: [[1,2],[3,4]]")
    nestedList5 = create_nested_list([[1,2],[3,4]])
    result5 = depthSum(nestedList5)
    expected5 = 20  # (1*2 + 2*2) + (3*2 + 4*2) = 20
    assert result5 == expected5, f"Test 5 failed: expected {expected5}, got {result5}"
    print(f"✓ Test 5 passed: {result5}\n")

    # Test 6: Empty nested list [[]]
    print("Test 6: [[]]")
    nestedList6 = create_nested_list([[]])
    result6 = depthSum(nestedList6)
    expected6 = 0
    assert result6 == expected6, f"Test 6 failed: expected {expected6}, got {result6}"
    print(f"✓ Test 6 passed: {result6}\n")

    print("All tests passed! ✓")


if __name__ == "__main__":
    test_nested_list_weight_sum()
