#!/usr/bin/env python3
"""Solution for Problem 8: KV Store with Persistence"""

import json
import pickle
from typing import Optional, Dict

class KVStore:
    def __init__(self, filepath: str):
        """
        Initialize KV store with persistence file path.

        TODO: Implement initialization
        Hints:
        1. Store filepath for persistence
        2. Initialize empty dict for in-memory storage
        3. Don't automatically restore here (let user call restore explicitly)

        Args:
            filepath: Path to persistence file
        """
        pass

    def put(self, key: str, value: str) -> None:
        """
        Store key-value pair in memory.

        TODO: Implement put operation
        Hints:
        1. Simply store in dict: self.data[key] = value
        2. Consider optional: write to WAL for crash recovery
        3. Consider optional: auto-save after N operations

        Args:
            key: Key to store
            value: Value to store
        """
        pass

    def get(self, key: str) -> Optional[str]:
        """
        Retrieve value for key.

        TODO: Implement get operation
        Hints:
        1. Return self.data.get(key)
        2. Return None if key doesn't exist

        Args:
            key: Key to lookup

        Returns:
            Value if key exists, None otherwise
        """
        pass

    def shutdown(self) -> None:
        """
        Persist all data to disk before shutdown.

        TODO: Implement shutdown/persistence
        Hints:
        1. Write self.data to file
        2. Options for serialization:
           - JSON: json.dump(self.data, file)
           - Pickle: pickle.dump(self.data, file)
           - Custom format: write each line as "key:value\n"
        3. Use 'w' mode for JSON/text, 'wb' for pickle
        4. Handle file I/O errors gracefully

        JSON Approach:
        with open(self.filepath, 'w') as f:
            json.dump(self.data, f)

        Pickle Approach:
        with open(self.filepath, 'wb') as f:
            pickle.dump(self.data, f)
        """
        pass

    def restore(self) -> None:
        """
        Restore data from disk.

        TODO: Implement restore operation
        Hints:
        1. Read data from file
        2. Load into self.data
        3. Handle missing file (file doesn't exist yet):
           - Initialize empty dict
           - Or raise FileNotFoundError
        4. Handle corrupted file gracefully

        JSON Approach:
        try:
            with open(self.filepath, 'r') as f:
                self.data = json.load(f)
        except FileNotFoundError:
            self.data = {}

        Pickle Approach:
        try:
            with open(self.filepath, 'rb') as f:
                self.data = pickle.load(f)
        except FileNotFoundError:
            self.data = {}
        """
        pass

    def _write_wal(self, key: str, value: str) -> None:
        """
        Write-Ahead Log for crash recovery (optional advanced feature).

        TODO: Implement WAL (optional)
        Hints:
        1. Append operation to WAL file before applying to memory
        2. WAL entry format: "PUT key value\n" or "DELETE key\n"
        3. On restore: replay WAL to recover state
        4. Periodically compact WAL by rewriting with current state
        """
        pass

    def _replay_wal(self) -> None:
        """
        Replay Write-Ahead Log for crash recovery (optional).

        TODO: Implement WAL replay (optional)
        Hints:
        1. Read WAL file line by line
        2. Parse each operation: "PUT key value" or "DELETE key"
        3. Apply operations to reconstruct state
        4. Handle partial writes (last line might be incomplete)
        """
        pass
