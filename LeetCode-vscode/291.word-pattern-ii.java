import java.util.*;

/*
 * @lc app=leetcode id=291 lang=java
 *
 * [291] Word Pattern II
 *
 * https://leetcode.com/problems/word-pattern-ii/description/
 *
 * algorithms
 * Hard (42.64%)
 * Likes:    371
 * Dislikes: 24
 * Total Accepted:    40.6K
 * Total Submissions: 95.2K
 * Testcase Example:  '"abab"\n"redblueredblue"'
 *
 * Given a pattern and a string str, find if str follows the same pattern.
 * 
 * Here follow means a full match, such that there is a bijection between a
 * letter in pattern and a non-empty substring in str.
 * 
 * Example 1:
 * 
 * 
 * Input: pattern = "abab", str = "redblueredblue"
 * Output: true
 * 
 * Example 2:
 * 
 * 
 * Input: pattern = pattern = "aaaa", str = "asdasdasdasd"
 * Output: true
 * 
 * Example 3:
 * 
 * 
 * Input: pattern = "aabb", str = "xyzabcxzyabc"
 * Output: false
 * 
 * 
 * Notes:
 * You may assume both pattern and str contains only lowercase letters.
 * 
 */

// @lc code=start
class Solution {
    public boolean wordPatternMatch(String pattern, String str) {
        if (pattern == null || str == null || pattern.length()>str.length()) return false;
        Map<Character,String> map = new HashMap<>();
        return match(map, pattern, 0, str, 0);
    }

    /**
     * 
     * @param map Char to String map for every char BEFORE the start position 'start'
     * @param pattern
     * @param start handle current start position in 'pattern' string
     * @param str
     * @return
     */
    private boolean match(Map<Character,String> map, String pattern, int startp, String str, int starts) {
        if (startp == pattern.length()) {
            return starts == str.length();
        } else if (startp > pattern.length() || starts > str.length()) {
            return false;
        }
        char p = pattern.charAt(startp);
        if (map.containsKey(p)) {
            String pstr = map.get(p);
            if (str.length()-starts >= pstr.length() && str.substring(starts, starts + pstr.length()).equals(pstr)) {
                return match(map, pattern, startp+1, str, starts + pstr.length());
            } else {
                return false;
            }
        } else {
            for (int plen=1; str.length()-starts-plen >= pattern.length() - startp -1; plen++) {
                String pstr = str.substring(starts, starts + plen);
                if (map.containsValue(pstr)) {
                    continue;
                }
                map.put(p, pstr);
                if (match(map, pattern, startp+1, str, starts+plen)) {
                    return true;
                }
                map.remove(p);
            }
            return false;
        }
    }
}
// @lc code=end

