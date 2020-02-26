/*
 * @lc app=leetcode id=688 lang=java
 *
 * [688] Knight Probability in Chessboard
 *
 * https://leetcode.com/problems/knight-probability-in-chessboard/description/
 *
 * algorithms
 * Medium (47.01%)
 * Likes:    579
 * Dislikes: 130
 * Total Accepted:    32.9K
 * Total Submissions: 69.8K
 * Testcase Example:  '3\n2\n0\n0'
 *
 * On an NxN chessboard, a knight starts at the r-th row and c-th column and
 * attempts to make exactly K moves. The rows and columns are 0 indexed, so the
 * top-left square is (0, 0), and the bottom-right square is (N-1, N-1).
 * 
 * A chess knight has 8 possible moves it can make, as illustrated below. Each
 * move is two squares in a cardinal direction, then one square in an
 * orthogonal direction.
 * 
 * 
 * 
 * 
 * 
 * 
 * 
 * Each time the knight is to move, it chooses one of eight possible moves
 * uniformly at random (even if the piece would go off the chessboard) and
 * moves there.
 * 
 * The knight continues moving until it has made exactly K moves or has moved
 * off the chessboard. Return the probability that the knight remains on the
 * board after it has stopped moving.
 * 
 * 
 * 
 * Example:
 * 
 * 
 * Input: 3, 2, 0, 0
 * Output: 0.0625
 * Explanation: There are two moves (to (1,2), (2,1)) that will keep the knight
 * on the board.
 * From each of those positions, there are also two moves that will keep the
 * knight on the board.
 * The total probability the knight stays on the board is 0.0625.
 * 
 * 
 * 
 * 
 * Note:
 * 
 * 
 * N will be between 1 and 25.
 * K will be between 0 and 100.
 * The knight always initially starts on the board.
 * 
 * 
 */

import java.util.*;

// @lc code=start
class Solution {
    public double knightProbability(int N, int K, int r, int c) {
        if (r<0 || r>=N || c<0 || c>=N) return 0.0;
        if (K==0) return 1.0;

        double[][] dp = new double[N][N];
        double[][] dp2 = new double[N][N];
        for (double[] row : dp) Arrays.fill(row, 1);

        int[] dirs = { 1, 2, 1, -2, -1, 2, -1, -2, 1 };
        for (int k = 0; k < K; k++) {
            for (int i = 0; i<N; i++) {
                for (int j=0; j<N; j++) {
                    double res = 0.0;
                    for (int d = 0; d < 8; d++) {
                        int ni = i + dirs[d];
                        int nj = j + dirs[d+1];
                        if (ni>=0 && ni<N && nj>=0 && nj<N) {
                            res += dp[ni][nj];
                        }
                    }
                    dp2[i][j] = res / 8;
                }
            }
            double[][] tmp = dp2;
            dp2 = dp;
            dp = tmp;
        }

        return dp[r][c];
    }
}
// @lc code=end

