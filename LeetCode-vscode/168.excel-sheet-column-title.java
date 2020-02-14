/*
 * @lc app=leetcode id=168 lang=java
 *
 * [168] Excel Sheet Column Title
 *
 * https://leetcode.com/problems/excel-sheet-column-title/description/
 *
 * algorithms
 * Easy (30.09%)
 * Likes:    957
 * Dislikes: 202
 * Total Accepted:    198.8K
 * Total Submissions: 660K
 * Testcase Example:  '1'
 *
 * Given a positive integer, return its corresponding column title as appear in
 * an Excel sheet.
 * 
 * For example:
 * 
 * 
 * ⁠   1 -> A
 * ⁠   2 -> B
 * ⁠   3 -> C
 * ⁠   ...
 * ⁠   26 -> Z
 * ⁠   27 -> AA
 * ⁠   28 -> AB 
 * ⁠   ...
 * 
 * 
 * Example 1:
 * 
 * 
 * Input: 1
 * Output: "A"
 * 
 * 
 * Example 2:
 * 
 * 
 * Input: 28
 * Output: "AB"
 * 
 * 
 * Example 3:
 * 
 * 
 * Input: 701
 * Output: "ZY"
 * 
 */

// @lc code=start
class Solution {
    public String convertToTitle(int n) {
        if (n<=26) {
            return Character.toString((char)('A' + n - 1));
        }
        int pre = n / 26;
        int rem = n % 26;
        if (rem==0) {
            rem = 26;
            pre--;
        }
        return convertToTitle(pre) + convertToTitle(rem);

    }
}
// @lc code=end

