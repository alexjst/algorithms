/*
 * @lc app=leetcode id=58 lang=java
 *
 * [58] Length of Last Word
 *
 * https://leetcode.com/problems/length-of-last-word/description/
 *
 * algorithms
 * Easy (32.43%)
 * Likes:    533
 * Dislikes: 2115
 * Total Accepted:    336.6K
 * Total Submissions: 1M
 * Testcase Example:  '"Hello World"'
 *
 * Given a string s consists of upper/lower-case alphabets and empty space
 * characters ' ', return the length of last word (last word means the last
 * appearing word if we loop from left to right) in the string.
 * 
 * If the last word does not exist, return 0.
 * 
 * Note: A word is defined as a maximal substring consisting of non-space
 * characters only.
 * 
 * Example:
 * 
 * 
 * Input: "Hello World"
 * Output: 5
 * 
 * 
 * 
 * 
 */

// @lc code=start
class Solution {
    public int lengthOfLastWord(String s) {
        if (s.isEmpty()) return 0;
        int i = s.length() - 1;
        while (i>=0 && s.charAt(i) == ' ') {
            i--;
        }
        int j = i;
        while (j>=0 && s.charAt(j) != ' ') {
            j--;
        }
        return i-j;
    }
}
// @lc code=end

