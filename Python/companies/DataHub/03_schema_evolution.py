#!/usr/bin/env python3
"""
Problem 3: Schema Evolution Tracking

DataHub tracks schema changes over time to ensure compatibility.
Implement a system to detect schema changes and check compatibility.

Requirements:
- Store schema versions with timestamps
- Detect schema changes (added/removed/modified fields)
- Check backward compatibility (new schema can read old data)
- Check forward compatibility (old schema can read new data)

Example:
    tracker = SchemaEvolution()

    schema_v1 = {
        "user_id": "int",
        "name": "string",
        "email": "string"
    }

    schema_v2 = {
        "user_id": "int",
        "name": "string",
        "email": "string",
        "created_at": "timestamp"  # New optional field
    }

    tracker.add_schema("users", schema_v1, version=1)
    tracker.add_schema("users", schema_v2, version=2)

    changes = tracker.get_changes("users", version_from=1, version_to=2)
    # Returns: {"added": ["created_at"], "removed": [], "modified": []}

    tracker.is_backward_compatible("users", 2, 1)  # Returns True

Time Complexity: O(n) where n is number of fields
Space Complexity: O(v × n) where v is versions, n is fields per version
"""

# Import the solution
try:
    import importlib.util
    spec = importlib.util.spec_from_file_location(
        "solution_module",
        "03_schema_evolution_solution.py"
    )
    solution_module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(solution_module)
    SchemaEvolution = solution_module.SchemaEvolution
except Exception as e:
    print(f"❌ Error importing solution: {e}")
    print(f"   Make sure 03_schema_evolution_solution.py exists.")
    exit(1)

def test_schema_evolution():
    """Test the schema evolution implementation."""

    print("Testing Schema Evolution...")
    print()

    # Test 1: Detect added fields
    print("Test 1: Detect added fields")
    tracker1 = SchemaEvolution()
    schema1_v1 = {"id": "int", "name": "string"}
    schema1_v2 = {"id": "int", "name": "string", "email": "string"}
    tracker1.add_schema("table1", schema1_v1, version=1)
    tracker1.add_schema("table1", schema1_v2, version=2)
    changes1 = tracker1.get_changes("table1", version_from=1, version_to=2)
    assert "email" in changes1["added"], f"Test 1 failed: 'email' should be in added fields, got {changes1}"
    print("✓ Test 1 passed: Added fields detected")
    print()

    # Test 2: Detect removed fields
    print("Test 2: Detect removed fields")
    tracker2 = SchemaEvolution()
    schema2_v1 = {"id": "int", "name": "string", "deprecated": "string"}
    schema2_v2 = {"id": "int", "name": "string"}
    tracker2.add_schema("table2", schema2_v1, version=1)
    tracker2.add_schema("table2", schema2_v2, version=2)
    changes2 = tracker2.get_changes("table2", version_from=1, version_to=2)
    assert "deprecated" in changes2["removed"], f"Test 2 failed: 'deprecated' should be in removed fields"
    print("✓ Test 2 passed: Removed fields detected")
    print()

    # Test 3: Detect type changes
    print("Test 3: Detect type changes")
    tracker3 = SchemaEvolution()
    schema3_v1 = {"id": "int", "count": "int"}
    schema3_v2 = {"id": "int", "count": "long"}
    tracker3.add_schema("table3", schema3_v1, version=1)
    tracker3.add_schema("table3", schema3_v2, version=2)
    changes3 = tracker3.get_changes("table3", version_from=1, version_to=2)
    assert "count" in changes3["modified"], f"Test 3 failed: 'count' should be in modified fields"
    print("✓ Test 3 passed: Type changes detected")
    print()

    # Test 4: Backward compatibility - added optional field
    print("Test 4: Backward compatibility with added field")
    tracker4 = SchemaEvolution()
    schema4_v1 = {"id": "int"}
    schema4_v2 = {"id": "int", "optional_field": "string"}
    tracker4.add_schema("table4", schema4_v1, version=1)
    tracker4.add_schema("table4", schema4_v2, version=2)
    # New schema can read old data (old data just missing optional_field)
    result4 = tracker4.is_backward_compatible("table4", 2, 1)
    assert result4 == True, f"Test 4 failed: should be backward compatible"
    print("✓ Test 4 passed: Backward compatible with added field")
    print()

    # Test 5: Not backward compatible - removed required field
    print("Test 5: Not backward compatible when field removed")
    tracker5 = SchemaEvolution()
    schema5_v1 = {"id": "int", "required_field": "string"}
    schema5_v2 = {"id": "int"}
    tracker5.add_schema("table5", schema5_v1, version=1)
    tracker5.add_schema("table5", schema5_v2, version=2)
    # New schema cannot read old data (old data has extra field)
    result5 = tracker5.is_backward_compatible("table5", 2, 1)
    assert result5 == False, f"Test 5 failed: should not be backward compatible"
    print("✓ Test 5 passed: Detected backward incompatibility")
    print()

    print("All tests passed! ✓")

if __name__ == "__main__":
    test_schema_evolution()
