#!/usr/bin/env python3
"""
Problem 9: Nested Transaction KV Store

SNAP asks this for understanding of database transaction semantics.
Implement a key-value store supporting nested transactions with commit/abort.

Requirements:
- start_transaction(): Begin new nested transaction
- commit(): Merge current transaction into parent
- abort(): Discard current transaction changes
- put(key, value): Store key-value in current transaction
- get(key): Retrieve value (searches current to root)

Example:
    store = TransactionStore()

    store.start_transaction()
    store.put("foo", "bar")
    store.put("a", "b")

    store.start_transaction()  # Nested transaction
    store.put("foo", "car")
    store.put("a", "b2")

    store.commit()
    print(store.get("foo"))  # "car"
    print(store.get("a"))    # "b2"

    store.abort()
    print(store.get("foo"))  # None (all transactions aborted)

Time Complexity: O(1) for put/get, O(k) for commit where k is keys in transaction
Space Complexity: O(n*d) where n is keys and d is transaction depth
"""

try:
    import importlib.util
    spec = importlib.util.spec_from_file_location("solution_module",
                                                   "09_nested_transaction_kv_store_solution.py")
    solution_module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(solution_module)
    TransactionStore = solution_module.TransactionStore
except Exception as e:
    print(f"❌ Error importing solution: {e}")
    exit(1)

def test_transaction_store():
    print("Testing Nested Transaction KV Store...")
    print()

    # Test 1: Basic transaction commit
    print("Test 1: Basic transaction commit")
    store1 = TransactionStore()
    store1.start_transaction()
    store1.put("foo", "bar")
    store1.put("a", "b")
    store1.start_transaction()
    store1.put("foo", "car")
    store1.put("a", "b2")
    store1.commit()
    assert store1.get("foo") == "car", "Test 1 failed: wrong value for foo"
    assert store1.get("a") == "b2", "Test 1 failed: wrong value for a"
    print("✓ Test 1 passed")
    print()

    # Test 2: Transaction abort
    print("Test 2: Transaction abort")
    store2 = TransactionStore()
    store2.start_transaction()
    store2.put("foo", "bar")
    store2.start_transaction()
    store2.put("foo", "car")
    store2.abort()
    assert store2.get("foo") == "bar", "Test 2 failed: abort didn't restore value"
    print("✓ Test 2 passed")
    print()

    # Test 3: Multiple nested transactions
    print("Test 3: Multiple nested transactions")
    store3 = TransactionStore()
    store3.start_transaction()
    store3.put("a", "1")
    store3.start_transaction()
    store3.put("a", "2")
    store3.start_transaction()
    store3.put("a", "3")
    store3.commit()
    assert store3.get("a") == "3", "Test 3 failed"
    store3.commit()
    assert store3.get("a") == "3", "Test 3 failed"
    print("✓ Test 3 passed")
    print()

    print("All tests passed! ✓")

if __name__ == "__main__":
    test_transaction_store()
