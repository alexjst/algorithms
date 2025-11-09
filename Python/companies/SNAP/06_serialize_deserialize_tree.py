#!/usr/bin/env python3
"""
Problem 6: Serialize and Deserialize Binary Tree

SNAP asks this for data persistence and caching.
Encode a binary tree to a string and decode it back.

Requirements:
- Serialize tree to string format
- Deserialize string back to tree
- Handle null nodes
- Preserve tree structure

Example:
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(5)
    
    codec = Codec()
    serialized = codec.serialize(root)   # "1,2,null,null,3,4,null,null,5,null,null"
    deserialized = codec.deserialize(serialized)  # Original tree restored

Time Complexity: O(n)
Space Complexity: O(n)
"""

try:
    import importlib.util
    spec = importlib.util.spec_from_file_location("solution_module",
                                                   "06_serialize_deserialize_tree_solution.py")
    solution_module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(solution_module)
    TreeNode = solution_module.TreeNode
    Codec = solution_module.Codec
except Exception as e:
    print(f"❌ Error importing solution: {e}")
    exit(1)

def test_codec():
    print("Testing Serialize and Deserialize Binary Tree...")
    print()

    codec = Codec()

    # Test 1: Simple tree
    print("Test 1: Simple tree")
    root1 = TreeNode(1)
    root1.left = TreeNode(2)
    root1.right = TreeNode(3)
    serialized1 = codec.serialize(root1)
    deserialized1 = codec.deserialize(serialized1)
    assert deserialized1.val == 1, "Test 1 failed: wrong root value"
    assert deserialized1.left.val == 2, "Test 1 failed: wrong left value"
    assert deserialized1.right.val == 3, "Test 1 failed: wrong right value"
    print("✓ Test 1 passed")
    print()

    # Test 2: Empty tree
    print("Test 2: Empty tree")
    serialized2 = codec.serialize(None)
    deserialized2 = codec.deserialize(serialized2)
    assert deserialized2 is None, "Test 2 failed"
    print("✓ Test 2 passed")
    print()

    # Test 3: Complex tree
    print("Test 3: Complex tree with nulls")
    root3 = TreeNode(1)
    root3.left = TreeNode(2)
    root3.right = TreeNode(3)
    root3.right.left = TreeNode(4)
    root3.right.right = TreeNode(5)
    serialized3 = codec.serialize(root3)
    deserialized3 = codec.deserialize(serialized3)
    assert deserialized3.right.left.val == 4, "Test 3 failed"
    print("✓ Test 3 passed")
    print()

    print("All tests passed! ✓")

if __name__ == "__main__":
    test_codec()
