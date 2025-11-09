#!/usr/bin/env python3
"""
Problem 5: LRU Cache

SNAP asks this for caching mechanisms in their infrastructure.
Implement Least Recently Used cache with O(1) operations.

Requirements:
- get(key) and put(key, value) in O(1) time
- Evict least recently used item when capacity reached
- Update access order on get

Example:
    cache = LRUCache(capacity=2)
    cache.put(1, 1)
    cache.put(2, 2)
    cache.get(1)       # Returns 1
    cache.put(3, 3)    # Evicts key 2
    cache.get(2)       # Returns -1 (not found)

Time Complexity: O(1) for get and put
Space Complexity: O(capacity)
"""

try:
    import importlib.util
    spec = importlib.util.spec_from_file_location("solution_module",
                                                   "05_lru_cache_solution.py")
    solution_module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(solution_module)
    LRUCache = solution_module.LRUCache
except Exception as e:
    print(f"❌ Error importing solution: {e}")
    exit(1)

def test_lru_cache():
    print("Testing LRU Cache...")
    print()

    # Test 1: Basic operations
    print("Test 1: Basic get and put")
    cache1 = LRUCache(2)
    cache1.put(1, 1)
    cache1.put(2, 2)
    assert cache1.get(1) == 1, "Test 1 failed"
    print("✓ Test 1 passed")
    print()

    # Test 2: Eviction
    print("Test 2: LRU eviction")
    cache2 = LRUCache(2)
    cache2.put(1, 1)
    cache2.put(2, 2)
    cache2.put(3, 3)  # Evicts 1
    assert cache2.get(1) == -1, "Test 2 failed: key 1 should be evicted"
    assert cache2.get(2) == 2, "Test 2 failed: key 2 should exist"
    print("✓ Test 2 passed")
    print()

    # Test 3: Update on access
    print("Test 3: Update order on get")
    cache3 = LRUCache(2)
    cache3.put(1, 1)
    cache3.put(2, 2)
    cache3.get(1)      # Access 1
    cache3.put(3, 3)   # Should evict 2, not 1
    assert cache3.get(2) == -1, "Test 3 failed: key 2 should be evicted"
    assert cache3.get(1) == 1, "Test 3 failed: key 1 should exist"
    print("✓ Test 3 passed")
    print()

    print("All tests passed! ✓")

if __name__ == "__main__":
    test_lru_cache()
