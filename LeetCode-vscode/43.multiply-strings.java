/*
 * @lc app=leetcode id=43 lang=java
 *
 * [43] Multiply Strings
 *
 * https://leetcode.com/problems/multiply-strings/description/
 *
 * algorithms
 * Medium (32.51%)
 * Likes:    1417
 * Dislikes: 653
 * Total Accepted:    253.6K
 * Total Submissions: 779.8K
 * Testcase Example:  '"2"\n"3"'
 *
 * Given two non-negative integers num1 and num2 represented as strings, return
 * the product of num1 and num2, also represented as a string.
 * 
 * Example 1:
 * 
 * 
 * Input: num1 = "2", num2 = "3"
 * Output: "6"
 * 
 * Example 2:
 * 
 * 
 * Input: num1 = "123", num2 = "456"
 * Output: "56088"
 * 
 * 
 * Note:
 * 
 * 
 * The length of both num1 and num2 is < 110.
 * Both num1 and num2 contain only digits 0-9.
 * Both num1 and num2 do not contain any leading zero, except the number 0
 * itself.
 * You must not use any built-in BigInteger library or convert the inputs to
 * integer directly.
 * 
 * 
 */

// @lc code=start
class Solution {
    public String multiply(String num1, String num2) {
        String res = "0";
        if (num1.equals("0") || num2.equals("0")) {
            return res;
        }
        if (num1.length() < num2.length()) {
            return multiply(num2, num1);
        }

        for (int i = 0; i<num2.length(); i++) {
            StringBuilder sbPart = new StringBuilder();
            sbPart.append(mult(num1, num2.charAt(i)));
            int zeros = num2.length() - i - 1;
            for (int z = 0; z < zeros; z++) {
                sbPart.append('0');
            }
            res = add(res, sbPart.toString());
        }
        return res;
    }

    private String mult(String num1, char c) {
        StringBuilder res = new StringBuilder();
        int ca = 0;
        for (int i=num1.length()-1; i>=0 || ca>0; i--) {
            char ch = (i>=0 ? num1.charAt(i) : '0');
            int sum = (ch - '0') * (c - '0') + ca;
            int digit = sum % 10;
            ca = sum / 10;
            res.append((char)('0' + digit));
        }
        return res.reverse().toString();
    }

    private String add(String num1, String num2) {
        char[] chars1 = num1.toCharArray();
        char[] chars2 = num2.toCharArray();
        StringBuilder res = new StringBuilder();
        int c = 0;
        for (int i=chars1.length-1, j=chars2.length-1; i>=0 || j>=0 || c>0; i--, j--) {
            int sum = c + (i>=0?chars1[i]-'0':0) + (j>=0?chars2[j]-'0':0);
            int digit = sum % 10;
            c = sum / 10;
            res.append((char)('0' + digit));
        }
        return res.reverse().toString();
    }
}
// @lc code=end

