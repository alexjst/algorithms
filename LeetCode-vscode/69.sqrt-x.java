/*
 * @lc app=leetcode id=69 lang=java
 *
 * [69] Sqrt(x)
 *
 * https://leetcode.com/problems/sqrtx/description/
 *
 * algorithms
 * Easy (32.22%)
 * Likes:    912
 * Dislikes: 1539
 * Total Accepted:    425.6K
 * Total Submissions: 1.3M
 * Testcase Example:  '4'
 *
 * Implement int sqrt(int x).
 * 
 * Compute and return the square root of x, where x is guaranteed to be a
 * non-negative integer.
 * 
 * Since the return type is an integer, the decimal digits are truncated and
 * only the integer part of the result is returned.
 * 
 * Example 1:
 * 
 * 
 * Input: 4
 * Output: 2
 * 
 * 
 * Example 2:
 * 
 * 
 * Input: 8
 * Output: 2
 * Explanation: The square root of 8 is 2.82842..., and since 
 * the decimal part is truncated, 2 is returned.
 * 
 * 
 */

// @lc code=start
/**
 * x = y*y means x/y=y, so y = (x/y+y) / 2;
 * but a key to solve this problem is to use double for
 * internal result
 */
class Solution {
    public int mySqrt(int x) {
        if (x<=0) return 0;

        double prev = 0, y = x;
        while ( Math.abs(prev-y) >= 0.1 ) {
            prev = y;
            y = (x/y + y)/2;
        }
        return (int)y;
    }
}
// @lc code=end

