#!/usr/bin/env python3
"""
Problem 1: First Non-Repeating Character

Actual ServiceTitan interview question - find the first unique character in a string.
Return the index of the first character that appears only once.

Requirements:
- Return index of first non-repeating character
- Return -1 if no such character exists
- Case-sensitive (lowercase != uppercase)
- O(n) time complexity preferred

Example:
    firstUniqChar("leetcode")   # 0 ('l' is first unique)
    firstUniqChar("loveleetcode") # 2 ('v' is first unique)
    firstUniqChar("aabb")       # -1 (no unique characters)
    firstUniqChar("ServiceTitan") # 0 ('S' appears once)

Time Complexity: O(n)
Space Complexity: O(1) - at most 26 letters + digits + symbols
"""

try:
    import importlib.util
    spec = importlib.util.spec_from_file_location("solution_module",
                                                   "01_first_non_repeating_char_solution.py")
    solution_module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(solution_module)
    firstUniqChar = solution_module.firstUniqChar
except Exception as e:
    print(f"❌ Error importing solution: {e}")
    exit(1)

def test_first_non_repeating_char():
    print("Testing First Non-Repeating Character...")
    print()

    # Test 1: Basic case
    print("Test 1: Basic example")
    assert firstUniqChar("leetcode") == 0, "Test 1 failed"
    print("✓ Test 1 passed")
    print()

    # Test 2: Multiple repeating characters
    print("Test 2: Multiple repeating characters")
    assert firstUniqChar("loveleetcode") == 2, "Test 2 failed"
    print("✓ Test 2 passed")
    print()

    # Test 3: All characters repeat
    print("Test 3: No unique characters")
    assert firstUniqChar("aabb") == -1, "Test 3 failed"
    print("✓ Test 3 passed")
    print()

    # Test 4: Single character
    print("Test 4: Single character")
    assert firstUniqChar("a") == 0, "Test 4 failed"
    print("✓ Test 4 passed")
    print()

    # Test 5: All unique characters
    print("Test 5: All unique characters")
    assert firstUniqChar("abcde") == 0, "Test 5 failed"
    print("✓ Test 5 passed")
    print()

    # Test 6: Unique character at end
    print("Test 6: Unique character at end")
    assert firstUniqChar("aabbcc d") == 7, "Test 6 failed"
    print("✓ Test 6 passed")
    print()

    # Test 7: Case sensitivity
    print("Test 7: Case sensitive")
    assert firstUniqChar("AaBbCc") == 0, "Test 7 failed: 'A' is unique"
    print("✓ Test 7 passed")
    print()

    # Test 8: Empty string
    print("Test 8: Empty string")
    assert firstUniqChar("") == -1, "Test 8 failed"
    print("✓ Test 8 passed")
    print()

    # Test 9: Company name example
    print("Test 9: ServiceTitan example")
    result = firstUniqChar("ServiceTitan")
    # 'S' appears once at index 0
    assert result == 0, f"Test 9 failed: got {result}, expected 0"
    print("✓ Test 9 passed")
    print()

    # Test 10: Numbers and special characters
    print("Test 10: Numbers and special characters")
    assert firstUniqChar("1122334455") == -1, "Test 10a failed"
    assert firstUniqChar("hello!world!") == 0, "Test 10b failed: 'h' is unique"
    print("✓ Test 10 passed")
    print()

    print("All tests passed! ✓")

if __name__ == "__main__":
    test_first_non_repeating_char()
