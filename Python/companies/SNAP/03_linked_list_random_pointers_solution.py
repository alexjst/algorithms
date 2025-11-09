#!/usr/bin/env python3
"""Solution for Problem 3: Copy List with Random Pointers"""

from typing import Optional

class Node:
    def __init__(self, val: int = 0, next: 'Node' = None, random: 'Node' = None):
        self.val = val
        self.next = next
        self.random = random

class LinkedListCopier:
    def copy_with_random(self, head: Optional[Node]) -> Optional[Node]:
        """
        Create deep copy of linked list with random pointers.
        
        TODO: Implement using hash map or three-pass approach
        Hints:
        1. First pass: Create all nodes and store in hash map
        2. Second pass: Link next and random pointers
        3. Return copied head
        """
        pass
