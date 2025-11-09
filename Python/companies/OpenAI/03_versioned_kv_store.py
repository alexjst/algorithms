#!/usr/bin/env python3
"""
Problem 3: Versioned Key-Value Store

OpenAI actual interview question - thread-safe KV store with version history.
Support get/put with versioning and time-travel queries.

Requirements:
- put(key, value): Store key-value pair (creates new version)
- get(key): Get current value for key
- get(key, version): Get value at specific version
- Thread-safe operations (consider locking)
- Track version history for all keys

Example:
    store = VersionedKVStore()

    store.put("a", "1")  # version 1
    store.put("b", "2")  # version 2
    store.put("a", "3")  # version 3 (update a)

    store.get("a")         # "3" (latest)
    store.get("a", 1)      # "1" (version 1)
    store.get("a", 2)      # "1" (a unchanged at v2)
    store.get("b", 2)      # "2"
    store.get("b", 1)      # None (b didn't exist)

Advanced Features (Optional):
- get_history(key): Return all versions for key
- delete(key): Soft delete (mark as deleted in new version)
- rollback(version): Restore entire store to version

Time Complexity: O(1) for get/put current, O(log v) for versioned get
Space Complexity: O(k * v) where k=keys, v=avg versions per key
"""

try:
    import importlib.util
    spec = importlib.util.spec_from_file_location("solution_module",
                                                   "03_versioned_kv_store_solution.py")
    solution_module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(solution_module)
    VersionedKVStore = solution_module.VersionedKVStore
except Exception as e:
    print(f"❌ Error importing solution: {e}")
    exit(1)

def test_versioned_kv_store():
    print("Testing Versioned KV Store...")
    print()

    # Test 1: Basic put and get
    print("Test 1: Basic operations")
    store1 = VersionedKVStore()
    store1.put("key1", "value1")
    assert store1.get("key1") == "value1", "Test 1 failed"
    print("✓ Test 1 passed")
    print()

    # Test 2: Versioned access
    print("Test 2: Version history")
    store2 = VersionedKVStore()
    store2.put("a", "v1")  # version 1
    store2.put("b", "v2")  # version 2
    store2.put("a", "v3")  # version 3

    assert store2.get("a") == "v3", "Test 2a failed: latest value"
    assert store2.get("a", 1) == "v1", "Test 2b failed: version 1"
    assert store2.get("a", 2) == "v1", "Test 2c failed: unchanged at v2"
    assert store2.get("b", 2) == "v2", "Test 2d failed"
    assert store2.get("b", 1) is None, "Test 2e failed: didn't exist"
    print("✓ Test 2 passed")
    print()

    # Test 3: Multiple updates
    print("Test 3: Multiple updates to same key")
    store3 = VersionedKVStore()
    store3.put("x", "1")
    store3.put("x", "2")
    store3.put("x", "3")

    assert store3.get("x") == "3", "Test 3a failed"
    assert store3.get("x", 1) == "1", "Test 3b failed"
    assert store3.get("x", 2) == "2", "Test 3c failed"
    assert store3.get("x", 3) == "3", "Test 3d failed"
    print("✓ Test 3 passed")
    print()

    # Test 4: Non-existent key
    print("Test 4: Non-existent keys")
    store4 = VersionedKVStore()
    store4.put("a", "1")
    assert store4.get("nonexistent") is None, "Test 4a failed"
    assert store4.get("nonexistent", 1) is None, "Test 4b failed"
    print("✓ Test 4 passed")
    print()

    # Test 5: Future version (should return latest)
    print("Test 5: Query future version")
    store5 = VersionedKVStore()
    store5.put("key", "value")
    # Requesting version 100 when only version 1 exists
    result = store5.get("key", 100)
    # Implementation can return latest or None - both acceptable
    print(f"  Future version query returned: {result}")
    print("✓ Test 5 passed")
    print()

    print("All tests passed! ✓")

if __name__ == "__main__":
    test_versioned_kv_store()
