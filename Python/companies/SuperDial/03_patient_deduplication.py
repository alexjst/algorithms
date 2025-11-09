#!/usr/bin/env python3
"""
Problem 3: Patient Data Deduplication

SuperDial's healthcare platform needs to detect duplicate patient records.
Implement a system to identify potential duplicate patient entries using
fuzzy matching on names and exact matching on identifiers.

Requirements:
- Detect duplicates based on similar names (Levenshtein distance)
- Exact match on phone numbers or patient IDs
- Return groups of potential duplicates
- Handle edge cases (missing data, empty fields)

Example:
    patients = [
        {"id": "P1", "name": "John Smith", "phone": "555-1234"},
        {"id": "P2", "name": "Jon Smith", "phone": "555-1234"},
        {"id": "P3", "name": "Jane Doe", "phone": "555-5678"},
    ]

    detector = PatientDeduplicator()
    duplicates = detector.find_duplicates(patients)
    # Returns: [[0, 1]] (indices 0 and 1 are duplicates)

Time Complexity: O(n²) for pairwise comparison
Space Complexity: O(n) for storing results
"""

# Import the solution
try:
    import importlib.util
    spec = importlib.util.spec_from_file_location(
        "solution_module",
        "03_patient_deduplication_solution.py"
    )
    solution_module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(solution_module)
    PatientDeduplicator = solution_module.PatientDeduplicator
except Exception as e:
    print(f"❌ Error importing solution: {e}")
    print(f"   Make sure 03_patient_deduplication_solution.py exists.")
    exit(1)

def test_patient_deduplication():
    """Test the patient deduplication implementation."""

    print("Testing Patient Deduplication...")
    print()

    # Test 1: Exact phone number match
    print("Test 1: Exact phone number match")
    patients1 = [
        {"id": "P1", "name": "John Smith", "phone": "555-1234"},
        {"id": "P2", "name": "Jane Doe", "phone": "555-1234"},
    ]
    detector1 = PatientDeduplicator()
    result1 = detector1.find_duplicates(patients1)
    assert len(result1) == 1, f"Test 1a failed: expected 1 duplicate group, got {len(result1)}"
    assert set(result1[0]) == {0, 1}, f"Test 1b failed: expected {{0, 1}}, got {set(result1[0])}"
    print("✓ Test 1 passed: Exact phone match detected")
    print()

    # Test 2: Similar names (typo)
    print("Test 2: Similar names detection")
    patients2 = [
        {"id": "P1", "name": "John Smith", "phone": "555-1111"},
        {"id": "P2", "name": "Jon Smith", "phone": "555-2222"},
        {"id": "P3", "name": "Jane Doe", "phone": "555-3333"},
    ]
    detector2 = PatientDeduplicator(name_threshold=2)
    result2 = detector2.find_duplicates(patients2)
    assert len(result2) == 1, f"Test 2a failed: expected 1 duplicate group, got {len(result2)}"
    assert set(result2[0]) == {0, 1}, f"Test 2b failed: expected {{0, 1}}, got {set(result2[0])}"
    print("✓ Test 2 passed: Similar names detected")
    print()

    # Test 3: No duplicates
    print("Test 3: No duplicates")
    patients3 = [
        {"id": "P1", "name": "John Smith", "phone": "555-1111"},
        {"id": "P2", "name": "Jane Doe", "phone": "555-2222"},
        {"id": "P3", "name": "Bob Johnson", "phone": "555-3333"},
    ]
    detector3 = PatientDeduplicator()
    result3 = detector3.find_duplicates(patients3)
    assert len(result3) == 0, f"Test 3 failed: expected no duplicates, got {len(result3)} groups"
    print("✓ Test 3 passed: No false positives")
    print()

    # Test 4: Same patient ID
    print("Test 4: Same patient ID match")
    patients4 = [
        {"id": "P123", "name": "John Smith", "phone": "555-1111"},
        {"id": "P123", "name": "J. Smith", "phone": "555-2222"},
    ]
    detector4 = PatientDeduplicator()
    result4 = detector4.find_duplicates(patients4)
    assert len(result4) == 1, f"Test 4 failed: expected 1 duplicate group, got {len(result4)}"
    print("✓ Test 4 passed: Same ID detected")
    print()

    # Test 5: Multiple duplicate groups
    print("Test 5: Multiple duplicate groups")
    patients5 = [
        {"id": "P1", "name": "John Smith", "phone": "555-1111"},
        {"id": "P2", "name": "Jon Smith", "phone": "555-1111"},
        {"id": "P3", "name": "Jane Doe", "phone": "555-2222"},
        {"id": "P4", "name": "Jane Do", "phone": "555-2222"},
    ]
    detector5 = PatientDeduplicator(name_threshold=2)
    result5 = detector5.find_duplicates(patients5)
    assert len(result5) == 2, f"Test 5 failed: expected 2 duplicate groups, got {len(result5)}"
    print("✓ Test 5 passed: Multiple groups detected")
    print()

    print("All tests passed! ✓")

if __name__ == "__main__":
    test_patient_deduplication()
