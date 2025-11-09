#!/usr/bin/env python3
"""
Problem 2: Metadata Search Index

DataHub needs efficient search across dataset metadata (names, descriptions, tags).
Implement a search index that supports prefix matching and ranking by relevance.

Requirements:
- Index datasets with name, description, and tags
- Support prefix search (e.g., "user" matches "user_events", "user_profile")
- Rank results by relevance (exact match > prefix match)
- Return top K results

Example:
    index = MetadataSearchIndex()
    index.add_dataset("user_events", "User activity events", ["analytics"])
    index.add_dataset("user_profile", "User profile data", ["users"])
    index.add_dataset("product_sales", "Sales transactions", ["sales"])

    index.search("user", k=2)  # Returns ["user_events", "user_profile"]
    index.search("sal", k=1)   # Returns ["product_sales"]

Time Complexity: O(m log n) for search where m is prefix length, n is results
Space Complexity: O(N × M) where N is datasets, M is avg metadata size
"""

# Import the solution
try:
    import importlib.util
    spec = importlib.util.spec_from_file_location(
        "solution_module",
        "02_metadata_search_index_solution.py"
    )
    solution_module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(solution_module)
    MetadataSearchIndex = solution_module.MetadataSearchIndex
except Exception as e:
    print(f"❌ Error importing solution: {e}")
    print(f"   Make sure 02_metadata_search_index_solution.py exists.")
    exit(1)

def test_metadata_search_index():
    """Test the metadata search index implementation."""

    print("Testing Metadata Search Index...")
    print()

    # Test 1: Basic prefix search
    print("Test 1: Basic prefix search")
    index1 = MetadataSearchIndex()
    index1.add_dataset("user_events", "User activity events", ["analytics"])
    index1.add_dataset("user_profile", "User profile data", ["users"])
    result1 = index1.search("user", k=5)
    assert len(result1) == 2, f"Test 1a failed: expected 2 results, got {len(result1)}"
    assert "user_events" in result1, "Test 1b failed: user_events should be in results"
    assert "user_profile" in result1, "Test 1c failed: user_profile should be in results"
    print("✓ Test 1 passed: Basic prefix search works")
    print()

    # Test 2: Exact match priority
    print("Test 2: Exact match gets higher priority")
    index2 = MetadataSearchIndex()
    index2.add_dataset("sales", "Sales data", ["revenue"])
    index2.add_dataset("sales_daily", "Daily sales", ["revenue"])
    result2 = index2.search("sales", k=2)
    assert result2[0] == "sales", f"Test 2 failed: exact match 'sales' should be first, got {result2[0]}"
    print("✓ Test 2 passed: Exact match prioritized")
    print()

    # Test 3: Top K results
    print("Test 3: Top K results limitation")
    index3 = MetadataSearchIndex()
    index3.add_dataset("data_v1", "Version 1", [])
    index3.add_dataset("data_v2", "Version 2", [])
    index3.add_dataset("data_v3", "Version 3", [])
    result3 = index3.search("data", k=2)
    assert len(result3) <= 2, f"Test 3 failed: expected at most 2 results, got {len(result3)}"
    print("✓ Test 3 passed: Top K limitation works")
    print()

    # Test 4: Tag search
    print("Test 4: Search in tags")
    index4 = MetadataSearchIndex()
    index4.add_dataset("events_table", "Event data", ["analytics", "tracking"])
    index4.add_dataset("metrics_table", "Metrics data", ["analytics"])
    result4 = index4.search("analytics", k=5)
    assert len(result4) >= 1, f"Test 4 failed: should find datasets with 'analytics' tag"
    print("✓ Test 4 passed: Tag search works")
    print()

    # Test 5: No matches
    print("Test 5: No matches returns empty")
    index5 = MetadataSearchIndex()
    index5.add_dataset("users", "User data", ["people"])
    result5 = index5.search("xyz", k=5)
    assert result5 == [], f"Test 5 failed: expected empty list, got {result5}"
    print("✓ Test 5 passed: No matches handled")
    print()

    print("All tests passed! ✓")

if __name__ == "__main__":
    test_metadata_search_index()
