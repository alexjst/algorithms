#!/usr/bin/env python3
"""
Problem 8: Key-Value Store with Persistence

Actual OpenAI interview question - implement a KV store with shutdown/restore.
Support persistence to disk and recovery from crashes.

Requirements:
- put(key, value): Store key-value pair
- get(key): Retrieve value for key
- shutdown(): Persist all data to disk
- restore(): Restore data from disk after restart
- Handle crash scenarios (data not lost)

Example:
    # Session 1
    store1 = KVStore(filepath="data.db")
    store1.put("name", "Alice")
    store1.put("age", "30")
    store1.put("city", "SF")
    store1.shutdown()  # Persist to disk

    # Session 2 (after restart)
    store2 = KVStore(filepath="data.db")
    store2.restore()   # Load from disk
    assert store2.get("name") == "Alice"
    assert store2.get("age") == "30"
    assert store2.get("city") == "SF"

Advanced Features (Optional):
- Write-Ahead Log (WAL) for crash recovery
- Periodic auto-save
- Compaction to reduce file size
- Transaction support (commit/rollback)
- Snapshot versioning

Time Complexity:
- put/get: O(1) average (hash map)
- shutdown: O(n) to write all data
- restore: O(n) to read all data

Space Complexity: O(n) for storing n key-value pairs
"""

try:
    import importlib.util
    spec = importlib.util.spec_from_file_location("solution_module",
                                                   "08_kv_store_persistence_solution.py")
    solution_module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(solution_module)
    KVStore = solution_module.KVStore
except Exception as e:
    print(f"❌ Error importing solution: {e}")
    exit(1)

import os
import tempfile

def test_kv_store_persistence():
    print("Testing KV Store with Persistence...")
    print()

    # Create temporary file for testing
    temp_dir = tempfile.mkdtemp()
    filepath = os.path.join(temp_dir, "test_data.db")

    try:
        # Test 1: Basic put and get
        print("Test 1: Basic put and get operations")
        store1 = KVStore(filepath)
        store1.put("key1", "value1")
        store1.put("key2", "value2")
        assert store1.get("key1") == "value1", "Test 1a failed"
        assert store1.get("key2") == "value2", "Test 1b failed"
        print("✓ Test 1 passed")
        print()

        # Test 2: Shutdown and restore
        print("Test 2: Shutdown and restore")
        store2 = KVStore(filepath)
        store2.put("a", "1")
        store2.put("b", "2")
        store2.put("c", "3")
        store2.shutdown()

        # Create new instance and restore
        store3 = KVStore(filepath)
        store3.restore()
        assert store3.get("a") == "1", "Test 2a failed"
        assert store3.get("b") == "2", "Test 2b failed"
        assert store3.get("c") == "3", "Test 2c failed"
        print("✓ Test 2 passed")
        print()

        # Test 3: Update existing key
        print("Test 3: Update existing keys")
        store4 = KVStore(filepath)
        store4.put("x", "old")
        assert store4.get("x") == "old", "Test 3a failed"
        store4.put("x", "new")
        assert store4.get("x") == "new", "Test 3b failed"
        store4.shutdown()

        store5 = KVStore(filepath)
        store5.restore()
        assert store5.get("x") == "new", "Test 3c failed: update not persisted"
        print("✓ Test 3 passed")
        print()

        # Test 4: Non-existent key
        print("Test 4: Non-existent key")
        store6 = KVStore(filepath)
        assert store6.get("nonexistent") is None, "Test 4 failed"
        print("✓ Test 4 passed")
        print()

        # Test 5: Empty store persistence
        print("Test 5: Empty store shutdown and restore")
        filepath2 = os.path.join(temp_dir, "empty_data.db")
        store7 = KVStore(filepath2)
        store7.shutdown()

        store8 = KVStore(filepath2)
        store8.restore()
        assert store8.get("anything") is None, "Test 5 failed"
        print("✓ Test 5 passed")
        print()

        # Test 6: Large dataset
        print("Test 6: Large dataset persistence")
        filepath3 = os.path.join(temp_dir, "large_data.db")
        store9 = KVStore(filepath3)

        # Add 1000 entries
        for i in range(1000):
            store9.put(f"key{i}", f"value{i}")

        store9.shutdown()

        # Restore and verify
        store10 = KVStore(filepath3)
        store10.restore()
        assert store10.get("key0") == "value0", "Test 6a failed"
        assert store10.get("key500") == "value500", "Test 6b failed"
        assert store10.get("key999") == "value999", "Test 6c failed"
        print("✓ Test 6 passed")
        print()

        # Test 7: Multiple shutdown/restore cycles
        print("Test 7: Multiple shutdown/restore cycles")
        filepath4 = os.path.join(temp_dir, "cycle_data.db")

        store11 = KVStore(filepath4)
        store11.put("cycle", "1")
        store11.shutdown()

        store12 = KVStore(filepath4)
        store12.restore()
        store12.put("cycle", "2")
        store12.shutdown()

        store13 = KVStore(filepath4)
        store13.restore()
        assert store13.get("cycle") == "2", "Test 7 failed"
        print("✓ Test 7 passed")
        print()

        # Test 8: Restore without shutdown
        print("Test 8: Restore without prior shutdown")
        filepath5 = os.path.join(temp_dir, "no_shutdown.db")
        store14 = KVStore(filepath5)
        # Attempt restore on non-existent file (should handle gracefully)
        try:
            store14.restore()
            # Should either start empty or handle missing file
            print("✓ Test 8 passed")
        except FileNotFoundError:
            # Also acceptable to raise exception
            print("✓ Test 8 passed (raises FileNotFoundError for missing file)")
        print()

        print("All tests passed! ✓")

    finally:
        # Cleanup
        import shutil
        if os.path.exists(temp_dir):
            shutil.rmtree(temp_dir)

if __name__ == "__main__":
    test_kv_store_persistence()
