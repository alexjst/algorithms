/*
 * @lc app=leetcode id=118 lang=java
 *
 * [118] Pascal's Triangle
 *
 * https://leetcode.com/problems/pascals-triangle/description/
 *
 * algorithms
 * Easy (49.80%)
 * Likes:    1079
 * Dislikes: 88
 * Total Accepted:    334.9K
 * Total Submissions: 668.1K
 * Testcase Example:  '5'
 *
 * Given a non-negative integer numRows, generate the first numRows of Pascal's
 * triangle.
 * 
 * 
 * In Pascal's triangle, each number is the sum of the two numbers directly
 * above it.
 * 
 * Example:
 * 
 * 
 * Input: 5
 * Output:
 * [
 * ⁠    [1],
 * ⁠   [1,1],
 * ⁠  [1,2,1],
 * ⁠ [1,3,3,1],
 * ⁠[1,4,6,4,1]
 * ]
 * 
 * 
 */
import java.util.*;

// @lc code=start
class Solution {
    public List<List<Integer>> generate(int numRows) {
        List<List<Integer>> res = new ArrayList<>();
        for (int i = 1; i <= numRows; i++) {
            List<Integer> lst = new ArrayList<>();
            lst.add(1);
            if (i>1) {
                List<Integer> preLst = res.get(i-2);
                for (int j=0; j<preLst.size()-1; j++) {
                    lst.add(preLst.get(j) + preLst.get(j+1));
                }
                lst.add(1);
            }
            res.add(lst);
        }
        return res;
    }
}
// @lc code=end

