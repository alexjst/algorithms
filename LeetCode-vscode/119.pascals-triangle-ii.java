/*
 * @lc app=leetcode id=119 lang=java
 *
 * [119] Pascal's Triangle II
 *
 * https://leetcode.com/problems/pascals-triangle-ii/description/
 *
 * algorithms
 * Easy (46.72%)
 * Likes:    645
 * Dislikes: 188
 * Total Accepted:    252.5K
 * Total Submissions: 537.2K
 * Testcase Example:  '3'
 *
 * Given a non-negative index k where k ≤ 33, return the k^th index row of the
 * Pascal's triangle.
 * 
 * Note that the row index starts from 0.
 * 
 * 
 * In Pascal's triangle, each number is the sum of the two numbers directly
 * above it.
 * 
 * Example:
 * 
 * 
 * Input: 3
 * Output: [1,3,3,1]
 * 
 * 
 * Follow up:
 * 
 * Could you optimize your algorithm to use only O(k) extra space?
 * 
 */

import java.util.*;

// @lc code=start
class Solution {
    public List<Integer> getRow(int rowIndex) {
        List<Integer> res = new ArrayList<>();
        if (rowIndex==0) {
            res.add(1);
            return res;
        }
        List<Integer> prev = getRow(rowIndex-1);
        res.add(1);
        for (int i=0; i<prev.size()-1; i++) {
            res.add(prev.get(i) + prev.get(i+1));
        }
        res.add(1);
        return res;
    }
}
// @lc code=end

