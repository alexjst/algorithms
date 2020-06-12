/*
 * @lc app=leetcode id=994 lang=csharp
 *
 * [994] Rotting Oranges
 *
 * https://leetcode.com/problems/rotting-oranges/description/
 *
 * algorithms
 * Medium (47.05%)
 * Likes:    1548
 * Dislikes: 179
 * Total Accepted:    95.8K
 * Total Submissions: 202.6K
 * Testcase Example:  '[[2,1,1],[1,1,0],[0,1,1]]'
 *
 * In a given grid, each cell can have one of three values:
 * 
 * 
 * the value 0 representing an empty cell;
 * the value 1 representing a fresh orange;
 * the value 2 representing a rotten orange.
 * 
 * 
 * Every minute, any fresh orange that is adjacent (4-directionally) to a
 * rotten orange becomes rotten.
 * 
 * Return the minimum number of minutes that must elapse until no cell has a
 * fresh orange.  If this is impossible, return -1 instead.
 * 
 * 
 * 
 * 
 * Example 1:
 * 
 * 
 * 
 * 
 * Input: [[2,1,1],[1,1,0],[0,1,1]]
 * Output: 4
 * 
 * 
 * 
 * Example 2:
 * 
 * 
 * Input: [[2,1,1],[0,1,1],[1,0,1]]
 * Output: -1
 * Explanation:  The orange in the bottom left corner (row 2, column 0) is
 * never rotten, because rotting only happens 4-directionally.
 * 
 * 
 * 
 * Example 3:
 * 
 * 
 * Input: [[0,2]]
 * Output: 0
 * Explanation:  Since there are already no fresh oranges at minute 0, the
 * answer is just 0.
 * 
 * 
 * 
 * 
 * Note:
 * 
 * 
 * 1 <= grid.length <= 10
 * 1 <= grid[0].length <= 10
 * grid[i][j] is only 0, 1, or 2.
 * 
 * 
 * 
 * 
 * 
 */

// @lc code=start
public class Solution {
    public int OrangesRotting(int[][] grid) {
        int M = grid.Length;
        int N = grid[0].Length;

        int res = 0;
        int ones = 0;
        int[,] g = new int[M,N];
        for (int i=0; i<M; i++) {
            for (int j=0; j<N; j++) {
                g[i,j] = grid[i][j];
                if (g[i,j] == 1) {
                    ones++;
                }
            }
        }

        int[,] n = new int[M,N];
        int[] dirs = {-1, 0, 1, 0, -1};
        while (ones > 0) {
            res++;
            bool turn = false;
            for (int i=0; i<M; i++) {
                for (int j=0; j<N; j++) {
                    n[i,j] = g[i,j];
                    if (g[i,j]==1) {
                        for (int step = 0; step < 4; step++) {
                            int p = i + dirs[step];
                            int q = j + dirs[step+1];
                            if (p>=0 && p<M && q>=0 && q<N && g[p,q]==2) {
                                ones--;
                                n[i,j]=2;
                                turn = true;
                                break;
                            }
                        }
                    }
                }
            }

            // nothing turns rotton yet we still have ones
            if (!turn && ones>0) return -1;

            for (int i=0; i<M; i++) {
                for (int j=0; j<N; j++) {
                    g[i,j] = n[i,j];
                }
            }
        }

        return res;
    }
}
// @lc code=end

