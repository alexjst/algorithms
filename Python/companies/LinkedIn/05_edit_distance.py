"""
Problem 5: Edit Distance (Medium)

**Classic DP Problem - Confirmed in LinkedIn Interviews**

Given two strings word1 and word2, return the minimum number of operations required
to convert word1 to word2.

You have the following three operations permitted on a word:
- Insert a character
- Delete a character
- Replace a character

Example 1:
Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation:
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')

Example 2:
Input: word1 = "intention", word2 = "execution"
Output: 5
Explanation:
intention -> inention (remove 't')
inention -> enention (replace 'i' with 'e')
enention -> exention (replace 'n' with 'x')
exention -> exection (replace 'n' with 'c')
exection -> execution (insert 'u')

Constraints:
- 0 <= word1.length, word2.length <= 500
- word1 and word2 consist of lowercase English letters

Approach:
Dynamic Programming with 2D table
dp[i][j] = minimum operations to convert word1[0...i-1] to word2[0...j-1]

If word1[i-1] == word2[j-1]: dp[i][j] = dp[i-1][j-1]
Else: dp[i][j] = 1 + min(dp[i-1][j],    # delete from word1
                          dp[i][j-1],    # insert into word1
                          dp[i-1][j-1])  # replace

Time Complexity: O(m * n)
Space Complexity: O(m * n), can optimize to O(min(m, n))

Implement your solution in 05_edit_distance_solution.py
"""

# Import the solution
try:
    from importlib import import_module
    solution = import_module('05_edit_distance_solution')
    minDistance = solution.minDistance
except (ImportError, AttributeError):
    def minDistance(word1: str, word2: str) -> int:
        raise NotImplementedError("Implement minDistance in 05_edit_distance_solution.py")


def test_edit_distance():
    print("Testing Edit Distance...\n")

    # Test 1: "horse" -> "ros"
    print("Test 1: word1 = 'horse', word2 = 'ros'")
    word1, word2 = "horse", "ros"
    result1 = minDistance(word1, word2)
    expected1 = 3
    assert result1 == expected1, f"Test 1 failed: expected {expected1}, got {result1}"
    print(f"✓ Test 1 passed: {result1}\n")

    # Test 2: "intention" -> "execution"
    print("Test 2: word1 = 'intention', word2 = 'execution'")
    word1, word2 = "intention", "execution"
    result2 = minDistance(word1, word2)
    expected2 = 5
    assert result2 == expected2, f"Test 2 failed: expected {expected2}, got {result2}"
    print(f"✓ Test 2 passed: {result2}\n")

    # Test 3: Empty strings
    print("Test 3: Empty strings")
    assert minDistance("", "") == 0, "Test 3a failed"
    assert minDistance("abc", "") == 3, "Test 3b failed"
    assert minDistance("", "xyz") == 3, "Test 3c failed"
    print(f"✓ Test 3 passed\n")

    # Test 4: Identical strings
    print("Test 4: Identical strings")
    word1, word2 = "linkedin", "linkedin"
    result4 = minDistance(word1, word2)
    expected4 = 0
    assert result4 == expected4, f"Test 4 failed: expected {expected4}, got {result4}"
    print(f"✓ Test 4 passed: {result4}\n")

    # Test 5: One character difference
    print("Test 5: One character difference")
    assert minDistance("a", "b") == 1, "Test 5a failed"
    assert minDistance("ab", "a") == 1, "Test 5b failed"
    assert minDistance("a", "ab") == 1, "Test 5c failed"
    print(f"✓ Test 5 passed\n")

    # Test 6: Completely different
    print("Test 6: Completely different strings")
    word1, word2 = "abc", "xyz"
    result6 = minDistance(word1, word2)
    expected6 = 3
    assert result6 == expected6, f"Test 6 failed: expected {expected6}, got {result6}"
    print(f"✓ Test 6 passed: {result6}\n")

    print("All tests passed! ✓")


if __name__ == "__main__":
    test_edit_distance()
