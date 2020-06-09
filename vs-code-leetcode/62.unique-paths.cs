/*
 * @lc app=leetcode id=62 lang=csharp
 *
 * [62] Unique Paths
 *
 * https://leetcode.com/problems/unique-paths/description/
 *
 * algorithms
 * Medium (52.27%)
 * Likes:    2943
 * Dislikes: 199
 * Total Accepted:    445.6K
 * Total Submissions: 847.1K
 * Testcase Example:  '3\n2'
 *
 * A robot is located at the top-left corner of a m x n grid (marked 'Start' in
 * the diagram below).
 * 
 * The robot can only move either down or right at any point in time. The robot
 * is trying to reach the bottom-right corner of the grid (marked 'Finish' in
 * the diagram below).
 * 
 * How many possible unique paths are there?
 * 
 * 
 * Above is a 7 x 3 grid. How many possible unique paths are there?
 * 
 * 
 * Example 1:
 * 
 * 
 * Input: m = 3, n = 2
 * Output: 3
 * Explanation:
 * From the top-left corner, there are a total of 3 ways to reach the
 * bottom-right corner:
 * 1. Right -> Right -> Down
 * 2. Right -> Down -> Right
 * 3. Down -> Right -> Right
 * 
 * 
 * Example 2:
 * 
 * 
 * Input: m = 7, n = 3
 * Output: 28
 * 
 * 
 * 
 * Constraints:
 * 
 * 
 * 1 <= m, n <= 100
 * It's guaranteed that the answer will be less than or equal to 2 * 10 ^ 9.
 * 
 * 
 */

// @lc code=start
public class Solution {
    /// <summary>
    /// DP solution is even faster than direct math calculations?
    /// Well no! Raunning each multiple times and I will see variances of run times.
    /// So performances between DP and direct math calculations are pretty close!
    /// </summary>
    /// <param name="m"></param>
    /// <param name="n"></param>
    /// <returns></returns>
    public int UniquePaths(int m, int n) {
        return Solution1(m, n);
        // return Solution2(m, n);
    }

    public int Solution1(int m, int n) {
        // there are m-1 down segments and n-1 right segments, we need to select which ones to go rightward
        // so we have a math solution: C(m+n-2, n-1) (i.e. select n-1 from m+n-2)
        int N = m + n - 2;
        int K = n - 1;

        K = Math.Min(K, N - K);

        long res = 1;
        for (int i = 0; i < K; i++) {
            res = res * (N - i) / (i + 1);
        }

        return (int)res;
    }

    public int Solution2(int m, int n) {
        int[,] paths = new int[m, n];
        for (int i=0; i<m; i++) paths[i, 0] = 1;
        for (int i=0; i<n; i++) paths[0, i] = 1;
        for (int i=1; i<m; i++) {
            for (int j=1; j<n; j++) {
                paths[i, j] = paths[i-1, j] + paths[i, j-1];
            }
        }
        return paths[m-1, n-1];
    }
}
// @lc code=end

