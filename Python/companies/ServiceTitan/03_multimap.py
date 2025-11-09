#!/usr/bin/env python3
"""
Problem 3: Multimap Implementation

Actual ServiceTitan interview question - implement a multimap data structure
with set operations (union, intersection, symmetric difference).

A multimap is a map where each key can have multiple values (stored as a set).

Requirements:
- add(key, value): Add value to key's value set
- remove(key, value): Remove value from key's value set
- get(key): Get all values for key
- union(other): Return new multimap with union of both multimaps
- intersection(other): Return new multimap with common key-value pairs
- symmetric_difference(other): Return new multimap with pairs in either but not both

Example:
    m1 = MultiMap()
    m1.add("a", 1)
    m1.add("a", 2)
    m1.add("b", 3)
    # m1 = {"a": {1, 2}, "b": {3}}

    m2 = MultiMap()
    m2.add("a", 2)
    m2.add("a", 3)
    m2.add("c", 4)
    # m2 = {"a": {2, 3}, "c": {4}}

    m1.union(m2)
    # {"a": {1, 2, 3}, "b": {3}, "c": {4}}

    m1.intersection(m2)
    # {"a": {2}}

    m1.symmetric_difference(m2)
    # {"a": {1, 3}, "b": {3}, "c": {4}}

Time Complexity:
- add/remove/get: O(1) average
- union/intersection/symmetric_difference: O(n + m) where n, m are sizes of multimaps

Space Complexity: O(n) for n key-value pairs
"""

try:
    import importlib.util
    spec = importlib.util.spec_from_file_location("solution_module",
                                                   "03_multimap_solution.py")
    solution_module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(solution_module)
    MultiMap = solution_module.MultiMap
except Exception as e:
    print(f"❌ Error importing solution: {e}")
    exit(1)

def test_multimap():
    print("Testing MultiMap Implementation...")
    print()

    # Test 1: Basic add and get
    print("Test 1: Basic add and get")
    m1 = MultiMap()
    m1.add("a", 1)
    m1.add("a", 2)
    m1.add("b", 3)
    assert m1.get("a") == {1, 2}, "Test 1a failed"
    assert m1.get("b") == {3}, "Test 1b failed"
    assert m1.get("c") == set(), "Test 1c failed: non-existent key"
    print("✓ Test 1 passed")
    print()

    # Test 2: Remove values
    print("Test 2: Remove values")
    m2 = MultiMap()
    m2.add("x", 1)
    m2.add("x", 2)
    m2.add("x", 3)
    m2.remove("x", 2)
    assert m2.get("x") == {1, 3}, "Test 2 failed"
    print("✓ Test 2 passed")
    print()

    # Test 3: Union operation
    print("Test 3: Union operation")
    m3a = MultiMap()
    m3a.add("a", 1)
    m3a.add("a", 2)
    m3a.add("b", 3)

    m3b = MultiMap()
    m3b.add("a", 2)
    m3b.add("a", 3)
    m3b.add("c", 4)

    result = m3a.union(m3b)
    assert result.get("a") == {1, 2, 3}, "Test 3a failed"
    assert result.get("b") == {3}, "Test 3b failed"
    assert result.get("c") == {4}, "Test 3c failed"
    print("✓ Test 3 passed")
    print()

    # Test 4: Intersection operation
    print("Test 4: Intersection operation")
    m4a = MultiMap()
    m4a.add("a", 1)
    m4a.add("a", 2)
    m4a.add("b", 3)

    m4b = MultiMap()
    m4b.add("a", 2)
    m4b.add("a", 3)
    m4b.add("c", 4)

    result = m4a.intersection(m4b)
    assert result.get("a") == {2}, "Test 4a failed"
    assert result.get("b") == set(), "Test 4b failed: no 'b' in intersection"
    assert result.get("c") == set(), "Test 4c failed: no 'c' in intersection"
    print("✓ Test 4 passed")
    print()

    # Test 5: Symmetric difference operation
    print("Test 5: Symmetric difference operation")
    m5a = MultiMap()
    m5a.add("a", 1)
    m5a.add("a", 2)
    m5a.add("b", 3)

    m5b = MultiMap()
    m5b.add("a", 2)
    m5b.add("a", 3)
    m5b.add("c", 4)

    result = m5a.symmetric_difference(m5b)
    assert result.get("a") == {1, 3}, "Test 5a failed: a should have {1, 3}"
    assert result.get("b") == {3}, "Test 5b failed: b should have {3}"
    assert result.get("c") == {4}, "Test 5c failed: c should have {4}"
    print("✓ Test 5 passed")
    print()

    # Test 6: Empty multimap operations
    print("Test 6: Empty multimap operations")
    m6a = MultiMap()
    m6b = MultiMap()
    m6b.add("a", 1)

    union_result = m6a.union(m6b)
    assert union_result.get("a") == {1}, "Test 6a failed"

    inter_result = m6a.intersection(m6b)
    assert inter_result.get("a") == set(), "Test 6b failed"
    print("✓ Test 6 passed")
    print()

    # Test 7: Duplicate adds (set behavior)
    print("Test 7: Duplicate values (set behavior)")
    m7 = MultiMap()
    m7.add("key", 1)
    m7.add("key", 1)  # Duplicate
    m7.add("key", 1)  # Duplicate
    assert m7.get("key") == {1}, "Test 7 failed: duplicates should be ignored"
    print("✓ Test 7 passed")
    print()

    # Test 8: Remove from empty set
    print("Test 8: Remove from non-existent key")
    m8 = MultiMap()
    m8.remove("nonexistent", 1)  # Should not raise error
    assert m8.get("nonexistent") == set(), "Test 8 failed"
    print("✓ Test 8 passed")
    print()

    # Test 9: Multiple keys
    print("Test 9: Multiple keys with operations")
    m9a = MultiMap()
    m9a.add("x", 1)
    m9a.add("y", 2)
    m9a.add("z", 3)

    m9b = MultiMap()
    m9b.add("x", 1)
    m9b.add("y", 5)
    m9b.add("w", 6)

    result = m9a.union(m9b)
    assert result.get("x") == {1}, "Test 9a failed"
    assert result.get("y") == {2, 5}, "Test 9b failed"
    assert result.get("z") == {3}, "Test 9c failed"
    assert result.get("w") == {6}, "Test 9d failed"
    print("✓ Test 9 passed")
    print()

    print("All tests passed! ✓")

if __name__ == "__main__":
    test_multimap()
