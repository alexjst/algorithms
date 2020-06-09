/*
 * @lc app=leetcode id=63 lang=csharp
 *
 * [63] Unique Paths II
 *
 * https://leetcode.com/problems/unique-paths-ii/description/
 *
 * algorithms
 * Medium (34.05%)
 * Likes:    1587
 * Dislikes: 233
 * Total Accepted:    284.6K
 * Total Submissions: 832.8K
 * Testcase Example:  '[[0,0,0],[0,1,0],[0,0,0]]'
 *
 * A robot is located at the top-left corner of a m x n grid (marked 'Start' in
 * the diagram below).
 * 
 * The robot can only move either down or right at any point in time. The robot
 * is trying to reach the bottom-right corner of the grid (marked 'Finish' in
 * the diagram below).
 * 
 * Now consider if some obstacles are added to the grids. How many unique paths
 * would there be?
 * 
 * 
 * 
 * An obstacle and empty space is marked as 1 and 0 respectively in the grid.
 * 
 * Note: m and n will be at most 100.
 * 
 * Example 1:
 * 
 * 
 * Input:
 * [
 * [0,0,0],
 * [0,1,0],
 * [0,0,0]
 * ]
 * Output: 2
 * Explanation:
 * There is one obstacle in the middle of the 3x3 grid above.
 * There are two ways to reach the bottom-right corner:
 * 1. Right -> Right -> Down -> Down
 * 2. Down -> Down -> Right -> Right
 * 
 * 
 */

// @lc code=start
public class Solution {
    public int UniquePathsWithObstacles(int[][] obstacleGrid) {
        int M = obstacleGrid.Length;
        if (M<1) return 0;
        int N = obstacleGrid[0].Length;
        if (N<1) return 0;
        int[,] dp = new int[M, N];
        dp[0,0] = obstacleGrid[0][0] == 0 ? 1 : 0;
        for (int i=1; i<M; i++) dp[i, 0] = obstacleGrid[i][0] == 0 ? dp[i-1, 0] : 0;
        for (int i=1; i<N; i++) dp[0, i] = obstacleGrid[0][i] == 0 ? dp[0, i-1] : 0;
        for (int i=1; i<M; i++) {
            for (int j=1; j<N; j++) {
                dp[i, j] = obstacleGrid[i][j] == 0 ? (
                    dp[i-1, j] + dp[i, j-1]
                ) : 0;
            }
        }
        return dp[M-1, N-1];
    }
}
// @lc code=end

