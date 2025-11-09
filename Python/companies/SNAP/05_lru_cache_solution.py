#!/usr/bin/env python3
"""Solution for Problem 5: LRU Cache"""

class ListNode:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        """
        TODO: Initialize LRU cache
        Hints:
        1. Use hash map for O(1) lookup
        2. Use doubly linked list for O(1) removal/addition
        3. Keep head and tail dummy nodes
        """
        pass

    def get(self, key: int) -> int:
        """
        TODO: Get value and update access order
        Return -1 if key doesn't exist
        """
        pass

    def put(self, key: int, value: int) -> None:
        """
        TODO: Put key-value pair
        Evict LRU item if capacity exceeded
        """
        pass
