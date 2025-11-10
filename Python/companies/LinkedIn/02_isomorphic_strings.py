"""
Problem 2: Isomorphic Strings (Easy)

**Confirmed in LinkedIn Interviews - High Frequency**

Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving
the order of characters. No two characters may map to the same character, but a character
may map to itself.

Example 1:
Input: s = "egg", t = "add"
Output: true
Explanation: 'e' -> 'a', 'g' -> 'd'

Example 2:
Input: s = "foo", t = "bar"
Output: false
Explanation: 'o' appears twice in s but maps to two different characters in t

Example 3:
Input: s = "paper", t = "title"
Output: true
Explanation: 'p' -> 't', 'a' -> 'i', 'e' -> 'l', 'r' -> 'e'

Constraints:
- 1 <= s.length <= 5 * 10^4
- t.length == s.length
- s and t consist of any valid ascii character

Approach:
- Use two hash maps to maintain bidirectional mapping
- Map s[i] -> t[i] and t[i] -> s[i]
- Check consistency at each step

Time Complexity: O(n) where n is length of string
Space Complexity: O(1) - at most 256 ASCII characters

Implement your solution in 02_isomorphic_strings_solution.py
"""

# Import the solution
try:
    from importlib import import_module
    solution = import_module('02_isomorphic_strings_solution')
    isIsomorphic = solution.isIsomorphic
except (ImportError, AttributeError):
    def isIsomorphic(s: str, t: str) -> bool:
        raise NotImplementedError("Implement isIsomorphic in 02_isomorphic_strings_solution.py")


def test_isomorphic_strings():
    print("Testing Isomorphic Strings...\n")

    # Test 1: "egg", "add"
    print("Test 1: s = 'egg', t = 'add'")
    s1, t1 = "egg", "add"
    result1 = isIsomorphic(s1, t1)
    expected1 = True
    assert result1 == expected1, f"Test 1 failed: expected {expected1}, got {result1}"
    print(f"✓ Test 1 passed: {result1}\n")

    # Test 2: "foo", "bar"
    print("Test 2: s = 'foo', t = 'bar'")
    s2, t2 = "foo", "bar"
    result2 = isIsomorphic(s2, t2)
    expected2 = False
    assert result2 == expected2, f"Test 2 failed: expected {expected2}, got {result2}"
    print(f"✓ Test 2 passed: {result2}\n")

    # Test 3: "paper", "title"
    print("Test 3: s = 'paper', t = 'title'")
    s3, t3 = "paper", "title"
    result3 = isIsomorphic(s3, t3)
    expected3 = True
    assert result3 == expected3, f"Test 3 failed: expected {expected3}, got {result3}"
    print(f"✓ Test 3 passed: {result3}\n")

    # Test 4: Single character
    print("Test 4: s = 'a', t = 'b'")
    s4, t4 = "a", "b"
    result4 = isIsomorphic(s4, t4)
    expected4 = True
    assert result4 == expected4, f"Test 4 failed: expected {expected4}, got {result4}"
    print(f"✓ Test 4 passed: {result4}\n")

    # Test 5: "badc", "baba" - should be false
    print("Test 5: s = 'badc', t = 'baba'")
    s5, t5 = "badc", "baba"
    result5 = isIsomorphic(s5, t5)
    expected5 = False
    assert result5 == expected5, f"Test 5 failed: expected {expected5}, got {result5}"
    print(f"✓ Test 5 passed: {result5}\n")

    # Test 6: Same strings
    print("Test 6: s = 'linkedin', t = 'linkedin'")
    s6, t6 = "linkedin", "linkedin"
    result6 = isIsomorphic(s6, t6)
    expected6 = True
    assert result6 == expected6, f"Test 6 failed: expected {expected6}, got {result6}"
    print(f"✓ Test 6 passed: {result6}\n")

    # Test 7: "ab", "aa" - should be false
    print("Test 7: s = 'ab', t = 'aa'")
    s7, t7 = "ab", "aa"
    result7 = isIsomorphic(s7, t7)
    expected7 = False
    assert result7 == expected7, f"Test 7 failed: expected {expected7}, got {result7}"
    print(f"✓ Test 7 passed: {result7}\n")

    print("All tests passed! ✓")


if __name__ == "__main__":
    test_isomorphic_strings()
