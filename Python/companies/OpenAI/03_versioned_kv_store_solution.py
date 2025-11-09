#!/usr/bin/env python3
"""Solution for Problem 3: Versioned KV Store"""

from typing import Optional
from threading import Lock

class VersionedKVStore:
    def __init__(self):
        """
        Initialize versioned key-value store.

        TODO: Implement initialization
        Hints:
        1. Track global version counter (starts at 0)
        2. Store: key -> list of (version, value) tuples
        3. Use threading.Lock for thread safety
        4. Consider using dict of lists or dict of dict
        """
        pass

    def put(self, key: str, value: str) -> None:
        """
        Store key-value pair (creates new version).

        TODO: Implement put operation
        Hints:
        1. Acquire lock for thread safety
        2. Increment global version
        3. Append (version, value) to key's history
        4. If key doesn't exist, create new list
        5. Release lock
        """
        pass

    def get(self, key: str, version: Optional[int] = None) -> Optional[str]:
        """
        Get value for key at specific version (or latest if version=None).

        TODO: Implement get operation
        Hints:
        1. Acquire lock for thread safety
        2. If key doesn't exist, return None
        3. Get list of (version, value) tuples for key
        4. If version is None: return latest value
        5. If version specified: find latest value <= version
           - Can use binary search for O(log v)
           - Or linear search for simpler implementation
        6. Release lock
        7. Return value or None if not found

        Args:
            key: Key to lookup
            version: Specific version to query (None = latest)

        Returns:
            Value at version, or None if not found
        """
        pass
