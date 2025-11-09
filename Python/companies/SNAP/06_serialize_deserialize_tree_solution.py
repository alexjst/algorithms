#!/usr/bin/env python3
"""Solution for Problem 6: Serialize and Deserialize Binary Tree"""

from typing import Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Codec:
    def serialize(self, root: Optional[TreeNode]) -> str:
        """
        Encode tree to string.
        
        TODO: Implement using BFS or DFS
        Hints:
        1. Use BFS with queue for level-order traversal
        2. Append node values to list, use "null" for None nodes
        3. Join with delimiter (e.g., comma)
        """
        pass

    def deserialize(self, data: str) -> Optional[TreeNode]:
        """
        Decode string to tree.
        
        TODO: Implement reverse of serialize
        Hints:
        1. Split string by delimiter
        2. Use queue to track nodes to process
        3. Connect children to parents
        """
        pass
