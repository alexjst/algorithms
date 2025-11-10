"""
Solution for Edit Distance

Implement your solution below.
"""

def minDistance(word1: str, word2: str) -> int:
    """
    Find minimum edit distance between two strings using DP.

    Args:
        word1: Source string
        word2: Target string

    Returns:
        Minimum number of operations (insert, delete, replace)

    Approach:
        2D DP table where dp[i][j] = min operations to convert
        word1[0...i-1] to word2[0...j-1]

        Base cases:
        - dp[0][j] = j (insert j characters)
        - dp[i][0] = i (delete i characters)

        Recurrence:
        If word1[i-1] == word2[j-1]:
            dp[i][j] = dp[i-1][j-1]  # No operation needed
        Else:
            dp[i][j] = 1 + min(
                dp[i-1][j],      # Delete from word1
                dp[i][j-1],      # Insert into word1
                dp[i-1][j-1]     # Replace character
            )

    Time: O(m * n)
    Space: O(m * n)
    """
    # TODO: Implement your solution

    # Hints:
    # 1. Create (m+1) x (n+1) DP table where m = len(word1), n = len(word2)
    # 2. Initialize first row: dp[0][j] = j for all j
    # 3. Initialize first column: dp[i][0] = i for all i
    # 4. Fill the table using the recurrence relation
    # 5. Return dp[m][n]

    # Space Optimization (Optional):
    # You only need previous row to compute current row
    # Can optimize to O(min(m, n)) space using 1D array

    raise NotImplementedError("Implement this function")
