#!/usr/bin/env python3
"""Solution for Problem 1: LRU Cache"""

class Node:
    """
    Doubly linked list node.

    TODO: Implement node structure
    Hints:
    1. Store key, value, prev, next
    2. Key is needed for eviction (to delete from hash map)
    """
    def __init__(self, key: int = 0, value: int = 0):
        pass

class LRUCache:
    def __init__(self, capacity: int):
        """
        Initialize LRU cache with given capacity.

        TODO: Implement initialization
        Hints:
        1. Create hash map: key -> Node
        2. Create dummy head and tail nodes
        3. Connect head.next = tail, tail.prev = head
        4. Store capacity
        """
        pass

    def get(self, key: int) -> int:
        """
        Get value for key, return -1 if not exists.

        TODO: Implement get operation
        Hints:
        1. Check if key in hash map
        2. If exists: move node to head (most recently used)
        3. Return node.value
        4. If not exists: return -1

        Moving to head:
        1. Remove node from current position
        2. Add node right after dummy head
        """
        pass

    def put(self, key: int, value: int) -> None:
        """
        Insert or update key-value pair.

        TODO: Implement put operation
        Hints:
        1. If key exists: remove old node from list
        2. Create new node with key, value
        3. Add node to head (most recently used)
        4. Add to hash map
        5. If over capacity: remove LRU node (tail.prev)
        6. Don't forget to remove from hash map when evicting
        """
        pass

    def _remove(self, node: Node) -> None:
        """
        Remove node from doubly linked list.

        TODO: Implement node removal
        Hints:
        1. Connect node.prev.next = node.next
        2. Connect node.next.prev = node.prev
        """
        pass

    def _add(self, node: Node) -> None:
        """
        Add node right after head (most recently used position).

        TODO: Implement node addition
        Hints:
        1. Insert between head and head.next
        2. node.prev = head
        3. node.next = head.next
        4. head.next.prev = node
        5. head.next = node
        """
        pass
