#!/usr/bin/env python3
"""
Problem 1: LRU Cache

THE MOST COMMON OpenAI coding problem - appears in almost every onsite.
Implement Least Recently Used cache with O(1) operations.

Requirements:
- get(key): Return value if exists, -1 otherwise (O(1))
- put(key, value): Insert/update key-value pair (O(1))
- When capacity exceeded, evict least recently used item
- Both get and put count as "using" the key

Example:
    cache = LRUCache(capacity=2)

    cache.put(1, 1)  # cache: {1=1}
    cache.put(2, 2)  # cache: {1=1, 2=2}
    cache.get(1)     # returns 1, cache: {2=2, 1=1}
    cache.put(3, 3)  # evicts key 2, cache: {1=1, 3=3}
    cache.get(2)     # returns -1 (not found)
    cache.put(4, 4)  # evicts key 1, cache: {3=3, 4=4}
    cache.get(1)     # returns -1 (not found)
    cache.get(3)     # returns 3
    cache.get(4)     # returns 4

Time Complexity: O(1) for both get and put
Space Complexity: O(capacity)

Implementation Hint:
Use doubly linked list + hash map:
- Hash map: key -> node (for O(1) lookup)
- Doubly linked list: maintain recency order (MRU at head, LRU at tail)
"""

try:
    import importlib.util
    spec = importlib.util.spec_from_file_location("solution_module",
                                                   "01_lru_cache_solution.py")
    solution_module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(solution_module)
    LRUCache = solution_module.LRUCache
except Exception as e:
    print(f"❌ Error importing solution: {e}")
    exit(1)

def test_lru_cache():
    print("Testing LRU Cache (Most Common OpenAI Problem)...")
    print()

    # Test 1: Basic operations
    print("Test 1: Basic put and get")
    cache1 = LRUCache(2)
    cache1.put(1, 1)
    cache1.put(2, 2)
    assert cache1.get(1) == 1, "Test 1 failed: get(1) should return 1"
    print("✓ Test 1 passed")
    print()

    # Test 2: Eviction
    print("Test 2: LRU eviction")
    cache2 = LRUCache(2)
    cache2.put(1, 1)
    cache2.put(2, 2)
    cache2.put(3, 3)  # Evicts key 1
    assert cache2.get(1) == -1, "Test 2 failed: key 1 should be evicted"
    assert cache2.get(2) == 2, "Test 2 failed: key 2 should exist"
    print("✓ Test 2 passed")
    print()

    # Test 3: Get updates recency
    print("Test 3: Get operation updates recency")
    cache3 = LRUCache(2)
    cache3.put(1, 1)
    cache3.put(2, 2)
    cache3.get(1)     # Access 1 (makes it most recent)
    cache3.put(3, 3)  # Should evict 2 (not 1)
    assert cache3.get(1) == 1, "Test 3 failed: key 1 should still exist"
    assert cache3.get(2) == -1, "Test 3 failed: key 2 should be evicted"
    print("✓ Test 3 passed")
    print()

    # Test 4: Update existing key
    print("Test 4: Update existing key")
    cache4 = LRUCache(2)
    cache4.put(2, 1)
    cache4.put(2, 2)  # Update existing key
    assert cache4.get(2) == 2, "Test 4 failed: updated value should be 2"
    print("✓ Test 4 passed")
    print()

    # Test 5: Complex scenario
    print("Test 5: Complex operations")
    cache5 = LRUCache(2)
    cache5.put(1, 1)
    cache5.put(2, 2)
    assert cache5.get(1) == 1
    cache5.put(3, 3)
    assert cache5.get(2) == -1
    cache5.put(4, 4)
    assert cache5.get(1) == -1
    assert cache5.get(3) == 3
    assert cache5.get(4) == 4
    print("✓ Test 5 passed")
    print()

    print("All tests passed! ✓")

if __name__ == "__main__":
    test_lru_cache()
