/*
 * @lc app=leetcode id=152 lang=java
 *
 * [152] Maximum Product Subarray
 *
 * https://leetcode.com/problems/maximum-product-subarray/description/
 *
 * algorithms
 * Medium (30.70%)
 * Likes:    3198
 * Dislikes: 135
 * Total Accepted:    287.1K
 * Total Submissions: 931.3K
 * Testcase Example:  '[2,3,-2,4]'
 *
 * Given an integer array nums, find the contiguous subarray within an array
 * (containing at least one number) which has the largest product.
 * 
 * Example 1:
 * 
 * 
 * Input: [2,3,-2,4]
 * Output: 6
 * Explanation: [2,3] has the largest product 6.
 * 
 * 
 * Example 2:
 * 
 * 
 * Input: [-2,0,-1]
 * Output: 0
 * Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
 * 
 */

import java.util.*;

// @lc code=start
class Solution {
    public int maxProduct(int[] nums) {
        int res = nums[0];
        int imax = res;
        int imin = res;
        for (int i=1; i<nums.length; i++) {
            if (nums[i]<0) {
                int tmp = imax;
                imax = imin;
                imin = tmp;
            }

            imax = Math.max(nums[i], nums[i]*imax);
            imin = Math.min(nums[i], nums[i]*imin);

            res = Math.max(res, imax);
        }
        return res;
    }
}
// @lc code=end

