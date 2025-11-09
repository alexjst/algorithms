#!/usr/bin/env python3
"""
Problem 4: Binary Tree Serialization and Deserialization

Actual ServiceTitan interview question - implement methods to serialize
and deserialize a binary tree.

Requirements:
- serialize(root): Convert binary tree to string representation
- deserialize(data): Reconstruct binary tree from string
- Handle empty trees and single nodes
- Format is flexible (can use level-order, pre-order, etc.)

Example:
    Input tree:
        1
       / \
      2   3
         / \
        4   5

    serialize(root) -> "1,2,null,null,3,4,null,null,5,null,null"
    deserialize(data) -> reconstructed tree

Approach:
1. Serialization: Use level-order (BFS) or pre-order (DFS) traversal
2. Deserialization: Parse string and reconstruct tree
3. Use "null" or "None" to represent missing nodes
4. Handle edge cases (empty tree, single node)

Time Complexity: O(n) for both operations
Space Complexity: O(n) for both operations
"""

try:
    import importlib.util
    spec = importlib.util.spec_from_file_location("solution_module",
                                                   "04_binary_tree_serialization_solution.py")
    solution_module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(solution_module)
    TreeNode = solution_module.TreeNode
    serialize = solution_module.serialize
    deserialize = solution_module.deserialize
except Exception as e:
    print(f"❌ Error importing solution: {e}")
    exit(1)

def test_binary_tree_serialization():
    print("Testing Binary Tree Serialization...")
    print()

    # Test 1: Single node
    print("Test 1: Single node")
    root1 = TreeNode(1)
    data1 = serialize(root1)
    result1 = deserialize(data1)
    assert result1.val == 1, "Test 1a failed"
    assert result1.left is None, "Test 1b failed"
    assert result1.right is None, "Test 1c failed"
    print("✓ Test 1 passed")
    print()

    # Test 2: Complete binary tree
    print("Test 2: Complete binary tree")
    root2 = TreeNode(1)
    root2.left = TreeNode(2)
    root2.right = TreeNode(3)
    root2.left.left = TreeNode(4)
    root2.left.right = TreeNode(5)

    data2 = serialize(root2)
    result2 = deserialize(data2)
    assert result2.val == 1, "Test 2a failed"
    assert result2.left.val == 2, "Test 2b failed"
    assert result2.right.val == 3, "Test 2c failed"
    assert result2.left.left.val == 4, "Test 2d failed"
    assert result2.left.right.val == 5, "Test 2e failed"
    print("✓ Test 2 passed")
    print()

    # Test 3: Unbalanced tree
    print("Test 3: Unbalanced tree")
    root3 = TreeNode(1)
    root3.left = TreeNode(2)
    root3.left.left = TreeNode(3)
    root3.left.left.left = TreeNode(4)

    data3 = serialize(root3)
    result3 = deserialize(data3)
    assert result3.val == 1, "Test 3a failed"
    assert result3.left.val == 2, "Test 3b failed"
    assert result3.left.left.val == 3, "Test 3c failed"
    assert result3.left.left.left.val == 4, "Test 3d failed"
    assert result3.right is None, "Test 3e failed"
    print("✓ Test 3 passed")
    print()

    # Test 4: Empty tree
    print("Test 4: Empty tree")
    data4 = serialize(None)
    result4 = deserialize(data4)
    assert result4 is None, "Test 4 failed"
    print("✓ Test 4 passed")
    print()

    # Test 5: Right-skewed tree
    print("Test 5: Right-skewed tree")
    root5 = TreeNode(1)
    root5.right = TreeNode(2)
    root5.right.right = TreeNode(3)

    data5 = serialize(root5)
    result5 = deserialize(data5)
    assert result5.val == 1, "Test 5a failed"
    assert result5.left is None, "Test 5b failed"
    assert result5.right.val == 2, "Test 5c failed"
    assert result5.right.right.val == 3, "Test 5d failed"
    print("✓ Test 5 passed")
    print()

    # Test 6: Tree with gaps
    print("Test 6: Tree with gaps")
    root6 = TreeNode(1)
    root6.left = TreeNode(2)
    root6.right = TreeNode(3)
    root6.right.left = TreeNode(4)
    root6.right.right = TreeNode(5)

    data6 = serialize(root6)
    result6 = deserialize(data6)
    assert result6.val == 1, "Test 6a failed"
    assert result6.left.val == 2, "Test 6b failed"
    assert result6.left.left is None, "Test 6c failed"
    assert result6.left.right is None, "Test 6d failed"
    assert result6.right.val == 3, "Test 6e failed"
    assert result6.right.left.val == 4, "Test 6f failed"
    assert result6.right.right.val == 5, "Test 6g failed"
    print("✓ Test 6 passed")
    print()

    # Test 7: Roundtrip multiple times
    print("Test 7: Roundtrip serialization")
    root7 = TreeNode(10)
    root7.left = TreeNode(5)
    root7.right = TreeNode(15)
    root7.left.left = TreeNode(3)
    root7.left.right = TreeNode(7)
    root7.right.right = TreeNode(18)

    data7_1 = serialize(root7)
    result7_1 = deserialize(data7_1)
    data7_2 = serialize(result7_1)
    result7_2 = deserialize(data7_2)

    # Check values match after double roundtrip
    assert result7_2.val == 10, "Test 7a failed"
    assert result7_2.left.val == 5, "Test 7b failed"
    assert result7_2.right.val == 15, "Test 7c failed"
    assert result7_2.left.left.val == 3, "Test 7d failed"
    assert result7_2.left.right.val == 7, "Test 7e failed"
    assert result7_2.right.right.val == 18, "Test 7f failed"
    print("✓ Test 7 passed")
    print()

    # Test 8: Large values
    print("Test 8: Large values")
    root8 = TreeNode(1000000)
    root8.left = TreeNode(-1000000)
    root8.right = TreeNode(999999)

    data8 = serialize(root8)
    result8 = deserialize(data8)
    assert result8.val == 1000000, "Test 8a failed"
    assert result8.left.val == -1000000, "Test 8b failed"
    assert result8.right.val == 999999, "Test 8c failed"
    print("✓ Test 8 passed")
    print()

    print("All tests passed! ✓")

if __name__ == "__main__":
    test_binary_tree_serialization()
