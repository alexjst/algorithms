#!/usr/bin/env python3
"""Solution for Problem 4: Binary Tree Serialization and Deserialization"""

from typing import Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def serialize(root: Optional[TreeNode]) -> str:
    """
    Serialize binary tree to string.

    TODO: Implement serialization
    Hints:
    1. Use level-order traversal (BFS with queue)
    2. Or use pre-order traversal (DFS)
    3. Represent null nodes with special marker (e.g., "null")
    4. Join values with delimiter (e.g., comma)

    Level-Order Approach (BFS):
    if not root:
        return ""

    result = []
    queue = deque([root])

    while queue:
        node = queue.popleft()
        if node:
            result.append(str(node.val))
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append("null")

    # Remove trailing nulls
    while result and result[-1] == "null":
        result.pop()

    return ",".join(result)

    Pre-Order Approach (DFS):
    def dfs(node):
        if not node:
            return ["null"]
        return [str(node.val)] + dfs(node.left) + dfs(node.right)

    return ",".join(dfs(root))

    Args:
        root: Root of binary tree

    Returns:
        String representation of tree
    """
    pass

def deserialize(data: str) -> Optional[TreeNode]:
    """
    Deserialize string to binary tree.

    TODO: Implement deserialization
    Hints:
    1. Split string by delimiter
    2. Use queue to track parent nodes
    3. For each value, create node and attach to parent
    4. Handle "null" markers appropriately

    Level-Order Approach (BFS):
    if not data:
        return None

    values = data.split(",")
    root = TreeNode(int(values[0]))
    queue = deque([root])
    i = 1

    while queue and i < len(values):
        node = queue.popleft()

        # Left child
        if i < len(values) and values[i] != "null":
            node.left = TreeNode(int(values[i]))
            queue.append(node.left)
        i += 1

        # Right child
        if i < len(values) and values[i] != "null":
            node.right = TreeNode(int(values[i]))
            queue.append(node.right)
        i += 1

    return root

    Pre-Order Approach (DFS):
    def dfs(values):
        val = values.pop(0)
        if val == "null":
            return None
        node = TreeNode(int(val))
        node.left = dfs(values)
        node.right = dfs(values)
        return node

    if not data:
        return None
    values = data.split(",")
    return dfs(values)

    Args:
        data: String representation of tree

    Returns:
        Root of reconstructed binary tree
    """
    pass
