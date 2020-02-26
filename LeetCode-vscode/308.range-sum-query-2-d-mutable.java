/*
 * @lc app=leetcode id=308 lang=java
 *
 * [308] Range Sum Query 2D - Mutable
 *
 * https://leetcode.com/problems/range-sum-query-2d-mutable/description/
 *
 * algorithms
 * Hard (34.07%)
 * Likes:    357
 * Dislikes: 50
 * Total Accepted:    42.8K
 * Total Submissions: 125K
 * Testcase Example:  '["NumMatrix","sumRegion","update","sumRegion"]\n' +
  '[[[[3,0,1,4,2],[5,6,3,2,1],[1,2,0,1,5],[4,1,0,1,7],[1,0,3,0,5]]],[2,1,4,3],[3,2,2],[2,1,4,3]]'
 *
 * Given a 2D matrix matrix, find the sum of the elements inside the rectangle
 * defined by its upper left corner (row1, col1) and lower right corner (row2,
 * col2).
 * 
 * 
 * 
 * The above rectangle (with the red border) is defined by (row1, col1) = (2,
 * 1) and (row2, col2) = (4, 3), which contains sum = 8.
 * 
 * 
 * Example:
 * 
 * Given matrix = [
 * ⁠ [3, 0, 1, 4, 2],
 * ⁠ [5, 6, 3, 2, 1],
 * ⁠ [1, 2, 0, 1, 5],
 * ⁠ [4, 1, 0, 1, 7],
 * ⁠ [1, 0, 3, 0, 5]
 * ]
 * 
 * sumRegion(2, 1, 4, 3) -> 8
 * update(3, 2, 2)
 * sumRegion(2, 1, 4, 3) -> 10
 * 
 * 
 * 
 * Note:
 * 
 * The matrix is only modifiable by the update function.
 * You may assume the number of calls to update and sumRegion function is
 * distributed evenly.
 * You may assume that row1 ≤ row2 and col1 ≤ col2.
 * 
 * 
 */

import java.util.*;

// @lc code=start
class NumMatrix {
    int[][] matrix;
    int[][] sums;
    int M, N;
    public NumMatrix(int[][] matrix) {
        this.matrix = matrix;
        M = matrix.length;
        if (M==0) return;
        N = matrix[0].length;
        if (N==0) return;
        sums = new int[M][N];
        for (int i=0; i<M; i++) {
            for (int j = 0; j < N; j++) {
                sums[i][j] = (j >= 1 ? sums[i][j - 1] : 0) + (i >= 1 ? sums[i - 1][j] : 0)
                        - (i >= 1 && j >= 1 ? sums[i - 1][j - 1] : 0) + matrix[i][j];
            }
        }
    }
    
    public void update(int row, int col, int val) {
        int diff = val - matrix[row][col];
        for (int i=row; i<M; i++) {
            for (int j=col; j<N; j++) {
                sums[i][j] += diff;
            }
        }
        matrix[row][col] = val;
    }
    
    public int sumRegion(int row1, int col1, int row2, int col2) {
        return sums[row2][col2]
                - (row1>=1 ? sums[row1-1][col2] : 0)
                - (col1>=1 ? sums[row2][col1-1] : 0)
                + (row1>=1 && col1>=1 ? sums[row1 - 1][col1 - 1] : 0);
    }
}

/**
 * Your NumMatrix object will be instantiated and called as such:
 * NumMatrix obj = new NumMatrix(matrix);
 * obj.update(row,col,val);
 * int param_2 = obj.sumRegion(row1,col1,row2,col2);
 */
// @lc code=end

