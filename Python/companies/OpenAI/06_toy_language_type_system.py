#!/usr/bin/env python3
"""
Problem 6: Toy Language Type System

Actual OpenAI interview question - design a type system for a custom toy language.
Process and validate types with support for primitives, generics, and tuples.

Requirements:
- Support primitives: int, char, float
- Support generics: T1, T2, T3, ... (uppercase alpha + numbers)
- Support tuples: (type1, type2, ...) with nesting allowed
- Implement type checking and validation
- Detect type mismatches and conflicts
- Reduce/filter redundant types

Example Grammar:
    Primitives: int, char, float
    Generics:   T1, T2, T3, ... Tn
    Tuples:     (int, char), (T1, (int, float))

Example Operations:
    Input:  [int, char, int, int]
    Output: [int, char]  # Remove duplicates, keep order

    Input:  [int, int, int, int]
    Output: Error (type mismatch)

    Input:  [int, int, int, char]
    Output: Error (type conflict)

    Input:  [(int, char), (int, char), (float, T1)]
    Output: [(int, char), (float, T1)]

Time Complexity: O(n) for type processing
Space Complexity: O(n) for storing types
"""

try:
    import importlib.util
    spec = importlib.util.spec_from_file_location("solution_module",
                                                   "06_toy_language_type_system_solution.py")
    solution_module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(solution_module)
    TypeSystem = solution_module.TypeSystem
except Exception as e:
    print(f"❌ Error importing solution: {e}")
    exit(1)

def test_toy_language_type_system():
    print("Testing Toy Language Type System...")
    print()

    # Test 1: Basic type deduplication
    print("Test 1: Remove duplicate types")
    ts1 = TypeSystem()
    result1 = ts1.process_types(["int", "char", "int", "int"])
    assert result1 == ["int", "char"], f"Test 1 failed: got {result1}"
    print("✓ Test 1 passed")
    print()

    # Test 2: Basic primitives
    print("Test 2: All unique primitives")
    ts2 = TypeSystem()
    result2 = ts2.process_types(["int", "char", "float"])
    assert result2 == ["int", "char", "float"], f"Test 2 failed: got {result2}"
    print("✓ Test 2 passed")
    print()

    # Test 3: Type validation - valid
    print("Test 3: Valid type names")
    ts3 = TypeSystem()
    assert ts3.is_valid_type("int") == True, "Test 3a failed"
    assert ts3.is_valid_type("char") == True, "Test 3b failed"
    assert ts3.is_valid_type("float") == True, "Test 3c failed"
    assert ts3.is_valid_type("T1") == True, "Test 3d failed"
    assert ts3.is_valid_type("T123") == True, "Test 3e failed"
    print("✓ Test 3 passed")
    print()

    # Test 4: Type validation - invalid
    print("Test 4: Invalid type names")
    ts4 = TypeSystem()
    assert ts4.is_valid_type("invalid") == False, "Test 4a failed"
    assert ts4.is_valid_type("t1") == False, "Test 4b failed: lowercase generic"
    assert ts4.is_valid_type("Int") == False, "Test 4c failed"
    assert ts4.is_valid_type("T") == False, "Test 4d failed: no number"
    print("✓ Test 4 passed")
    print()

    # Test 5: Tuple types
    print("Test 5: Tuple type handling")
    ts5 = TypeSystem()
    result5 = ts5.process_types(["(int, char)", "(int, char)", "float"])
    assert result5 == ["(int, char)", "float"], f"Test 5 failed: got {result5}"
    print("✓ Test 5 passed")
    print()

    # Test 6: Nested tuples
    print("Test 6: Nested tuple types")
    ts6 = TypeSystem()
    result6 = ts6.process_types(["(int, (char, float))", "(int, (char, float))", "T1"])
    assert result6 == ["(int, (char, float))", "T1"], f"Test 6 failed: got {result6}"
    print("✓ Test 6 passed")
    print()

    # Test 7: Generic types
    print("Test 7: Generic type handling")
    ts7 = TypeSystem()
    result7 = ts7.process_types(["T1", "T2", "T1", "int", "T2"])
    assert result7 == ["T1", "T2", "int"], f"Test 7 failed: got {result7}"
    print("✓ Test 7 passed")
    print()

    # Test 8: Mixed tuple with generics
    print("Test 8: Tuples containing generics")
    ts8 = TypeSystem()
    result8 = ts8.process_types(["(T1, int)", "(T2, char)", "(T1, int)"])
    assert result8 == ["(T1, int)", "(T2, char)"], f"Test 8 failed: got {result8}"
    print("✓ Test 8 passed")
    print()

    # Test 9: Empty list
    print("Test 9: Empty type list")
    ts9 = TypeSystem()
    result9 = ts9.process_types([])
    assert result9 == [], f"Test 9 failed: got {result9}"
    print("✓ Test 9 passed")
    print()

    # Test 10: Single type
    print("Test 10: Single type")
    ts10 = TypeSystem()
    result10 = ts10.process_types(["int"])
    assert result10 == ["int"], f"Test 10 failed: got {result10}"
    print("✓ Test 10 passed")
    print()

    # Test 11: Complex nested structure
    print("Test 11: Complex nested tuples")
    ts11 = TypeSystem()
    result11 = ts11.process_types([
        "((int, char), (float, T1))",
        "((int, char), (float, T1))",
        "T2"
    ])
    assert result11 == ["((int, char), (float, T1))", "T2"], f"Test 11 failed: got {result11}"
    print("✓ Test 11 passed")
    print()

    print("All tests passed! ✓")

if __name__ == "__main__":
    test_toy_language_type_system()
