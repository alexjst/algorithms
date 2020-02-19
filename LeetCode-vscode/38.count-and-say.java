/*
 * @lc app=leetcode id=38 lang=java
 *
 * [38] Count and Say
 *
 * https://leetcode.com/problems/count-and-say/description/
 *
 * algorithms
 * Easy (42.85%)
 * Likes:    1061
 * Dislikes: 8256
 * Total Accepted:    352.7K
 * Total Submissions: 821.3K
 * Testcase Example:  '1'
 *
 * The count-and-say sequence is the sequence of integers with the first five
 * terms as following:
 * 
 * 
 * 1.     1
 * 2.     11
 * 3.     21
 * 4.     1211
 * 5.     111221
 * 
 * 
 * 1 is read off as "one 1" or 11.
 * 11 is read off as "two 1s" or 21.
 * 21 is read off as "one 2, then one 1" or 1211.
 * 
 * Given an integer n where 1 ≤ n ≤ 30, generate the n^th term of the
 * count-and-say sequence. You can do so recursively, in other words from the
 * previous member read off the digits, counting the number of digits in groups
 * of the same digit.
 * 
 * Note: Each term of the sequence of integers will be represented as a
 * string.
 * 
 * 
 * 
 * Example 1:
 * 
 * 
 * Input: 1
 * Output: "1"
 * Explanation: This is the base case.
 * 
 * 
 * Example 2:
 * 
 * 
 * Input: 4
 * Output: "1211"
 * Explanation: For n = 3 the term was "21" in which we have two groups "2" and
 * "1", "2" can be read as "12" which means frequency = 1 and value = 2, the
 * same way "1" is read as "11", so the answer is the concatenation of "12" and
 * "11" which is "1211".
 * 
 * 
 */

// @lc code=start
class Solution {
    StringBuilder res = new StringBuilder();
    public String countAndSay(int n) {
        if (n==1) return "1";
        String prev = countAndSay(n-1);
        char[] chars = prev.toCharArray();
        int len = chars.length;
        res.setLength(0);
        int cnt = 0;
        char c = ' ';
        for (int i=0; i<len; i++) {
            if (i==0 || chars[i] == chars[i-1]) {
                cnt++;
                c = chars[i];
                continue;
            } else {
                res.append(String.valueOf(cnt));
                res.append(c);
                cnt = 1;
                c = chars[i];
            }
        }
        res.append(String.valueOf(cnt));
        res.append(c);
        return res.toString();
    }
}
// @lc code=end

