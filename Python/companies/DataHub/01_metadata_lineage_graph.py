#!/usr/bin/env python3
"""
Problem 1: Metadata Lineage Graph

DataHub tracks data lineage to understand dependencies between datasets.
Implement a system to find all downstream dependencies of a given dataset.

Requirements:
- Build a directed graph of dataset dependencies
- Find all datasets that depend on a given dataset (downstream)
- Detect circular dependencies
- Return dependencies in topological order

Example:
    lineage = MetadataLineage()
    lineage.add_dependency("table_c", "table_a")  # c depends on a
    lineage.add_dependency("table_c", "table_b")  # c depends on b
    lineage.add_dependency("table_d", "table_c")  # d depends on c

    lineage.get_downstream("table_a")  # Returns ["table_c", "table_d"]
    lineage.has_circular_dependency()  # Returns False

Time Complexity: O(V + E) for DFS/BFS traversal
Space Complexity: O(V + E) for graph storage
"""

# Import the solution
try:
    import importlib.util
    spec = importlib.util.spec_from_file_location(
        "solution_module",
        "01_metadata_lineage_graph_solution.py"
    )
    solution_module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(solution_module)
    MetadataLineage = solution_module.MetadataLineage
except Exception as e:
    print(f"❌ Error importing solution: {e}")
    print(f"   Make sure 01_metadata_lineage_graph_solution.py exists.")
    exit(1)

def test_metadata_lineage():
    """Test the metadata lineage implementation."""

    print("Testing Metadata Lineage Graph...")
    print()

    # Test 1: Basic downstream dependencies
    print("Test 1: Basic downstream dependencies")
    lineage1 = MetadataLineage()
    lineage1.add_dependency("table_b", "table_a")
    lineage1.add_dependency("table_c", "table_b")
    result1 = lineage1.get_downstream("table_a")
    assert set(result1) == {"table_b", "table_c"}, f"Test 1 failed: expected {{table_b, table_c}}, got {set(result1)}"
    print("✓ Test 1 passed: Basic downstream dependencies work")
    print()

    # Test 2: Multiple dependencies
    print("Test 2: Multiple dependencies")
    lineage2 = MetadataLineage()
    lineage2.add_dependency("table_c", "table_a")
    lineage2.add_dependency("table_c", "table_b")
    lineage2.add_dependency("table_d", "table_c")
    result2 = lineage2.get_downstream("table_a")
    assert "table_c" in result2, "Test 2a failed: table_c should be downstream of table_a"
    assert "table_d" in result2, "Test 2b failed: table_d should be downstream of table_a"
    print("✓ Test 2 passed: Multiple dependencies work")
    print()

    # Test 3: No dependencies
    print("Test 3: No dependencies")
    lineage3 = MetadataLineage()
    lineage3.add_dependency("table_b", "table_a")
    result3 = lineage3.get_downstream("table_b")
    assert result3 == [], f"Test 3 failed: expected empty list, got {result3}"
    print("✓ Test 3 passed: No dependencies handled")
    print()

    # Test 4: Circular dependency detection
    print("Test 4: Circular dependency detection")
    lineage4 = MetadataLineage()
    lineage4.add_dependency("table_b", "table_a")
    lineage4.add_dependency("table_c", "table_b")
    lineage4.add_dependency("table_a", "table_c")  # Creates cycle
    assert lineage4.has_circular_dependency() == True, "Test 4 failed: should detect circular dependency"
    print("✓ Test 4 passed: Circular dependency detected")
    print()

    # Test 5: No circular dependency
    print("Test 5: No circular dependency")
    lineage5 = MetadataLineage()
    lineage5.add_dependency("table_b", "table_a")
    lineage5.add_dependency("table_c", "table_b")
    assert lineage5.has_circular_dependency() == False, "Test 5 failed: should not detect circular dependency"
    print("✓ Test 5 passed: No false positive for circular dependency")
    print()

    print("All tests passed! ✓")

if __name__ == "__main__":
    test_metadata_lineage()
