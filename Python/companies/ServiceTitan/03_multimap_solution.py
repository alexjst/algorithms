#!/usr/bin/env python3
"""Solution for Problem 3: MultiMap Implementation"""

from typing import Set, Any
from collections import defaultdict

class MultiMap:
    def __init__(self):
        """
        Initialize multimap.

        TODO: Implement initialization
        Hints:
        1. Use dict mapping key -> set of values
        2. Or use defaultdict(set) for automatic set creation
        3. self.data = defaultdict(set)
        """
        pass

    def add(self, key: Any, value: Any) -> None:
        """
        Add value to key's value set.

        TODO: Implement add operation
        Hints:
        1. Get the set for this key (or create empty set if doesn't exist)
        2. Add value to the set
        3. self.data[key].add(value)

        Args:
            key: The key
            value: Value to add to key's set
        """
        pass

    def remove(self, key: Any, value: Any) -> None:
        """
        Remove value from key's value set.

        TODO: Implement remove operation
        Hints:
        1. Check if key exists in data
        2. If exists, remove value from set (use discard to avoid KeyError)
        3. Optionally: remove key if its set becomes empty
        4. self.data[key].discard(value)

        Args:
            key: The key
            value: Value to remove from key's set
        """
        pass

    def get(self, key: Any) -> Set[Any]:
        """
        Get all values for key.

        TODO: Implement get operation
        Hints:
        1. Return set of values for key
        2. Return empty set if key doesn't exist
        3. return self.data.get(key, set())
        4. Important: return copy of set to prevent external modification
           return self.data.get(key, set()).copy()

        Args:
            key: The key to lookup

        Returns:
            Set of values for key, or empty set if key doesn't exist
        """
        pass

    def union(self, other: 'MultiMap') -> 'MultiMap':
        """
        Return new multimap with union of both multimaps.

        TODO: Implement union operation
        Hints:
        1. Create new MultiMap
        2. For each key in self: add all values to result
        3. For each key in other: add all values to result
        4. Sets automatically handle duplicates

        Algorithm:
        result = MultiMap()
        for key in self.data:
            for value in self.data[key]:
                result.add(key, value)
        for key in other.data:
            for value in other.data[key]:
                result.add(key, value)
        return result

        Args:
            other: Another MultiMap

        Returns:
            New MultiMap with union of both
        """
        pass

    def intersection(self, other: 'MultiMap') -> 'MultiMap':
        """
        Return new multimap with common key-value pairs.

        TODO: Implement intersection operation
        Hints:
        1. Create new MultiMap
        2. For each key in both self and other:
           - Find intersection of value sets
           - Add to result
        3. Use set intersection: self.data[key] & other.data[key]

        Algorithm:
        result = MultiMap()
        for key in self.data:
            if key in other.data:
                common_values = self.data[key] & other.data[key]
                for value in common_values:
                    result.add(key, value)
        return result

        Args:
            other: Another MultiMap

        Returns:
            New MultiMap with only common key-value pairs
        """
        pass

    def symmetric_difference(self, other: 'MultiMap') -> 'MultiMap':
        """
        Return new multimap with pairs in either but not both.

        TODO: Implement symmetric difference operation
        Hints:
        1. Create new MultiMap
        2. For each key in self or other:
           - Find symmetric difference of value sets
           - Add to result
        3. Use set symmetric difference: self.data[key] ^ other.data[key]
        4. Or: (set1 - set2) | (set2 - set1)

        Algorithm:
        result = MultiMap()
        all_keys = set(self.data.keys()) | set(other.data.keys())
        for key in all_keys:
            self_values = self.data.get(key, set())
            other_values = other.data.get(key, set())
            diff_values = self_values ^ other_values
            for value in diff_values:
                result.add(key, value)
        return result

        Args:
            other: Another MultiMap

        Returns:
            New MultiMap with pairs in either but not both
        """
        pass
