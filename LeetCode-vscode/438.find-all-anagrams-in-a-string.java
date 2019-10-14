/*
 * @lc app=leetcode id=438 lang=java
 *
 * [438] Find All Anagrams in a String
 *
 * https://leetcode.com/problems/find-all-anagrams-in-a-string/description/
 *
 * algorithms
 * Medium (38.71%)
 * Likes:    1862
 * Dislikes: 143
 * Total Accepted:    150.4K
 * Total Submissions: 388.6K
 * Testcase Example:  '"cbaebabacd"\n"abc"'
 *
 * Given a string s and a non-empty string p, find all the start indices of p's
 * anagrams in s.
 * 
 * Strings consists of lowercase English letters only and the length of both
 * strings s and p will not be larger than 20,100.
 * 
 * The order of output does not matter.
 * 
 * Example 1:
 * 
 * Input:
 * s: "cbaebabacd" p: "abc"
 * 
 * Output:
 * [0, 6]
 * 
 * Explanation:
 * The substring with start index = 0 is "cba", which is an anagram of "abc".
 * The substring with start index = 6 is "bac", which is an anagram of
 * "abc".
 * 
 * 
 * 
 * Example 2:
 * 
 * Input:
 * s: "abab" p: "ab"
 * 
 * Output:
 * [0, 1, 2]
 * 
 * Explanation:
 * The substring with start index = 0 is "ab", which is an anagram of "ab".
 * The substring with start index = 1 is "ba", which is an anagram of "ab".
 * The substring with start index = 2 is "ab", which is an anagram of "ab".
 * 
 * 
 */

// @lc code=start
import java.util.*;

class Solution {
    public List<Integer> findAnagrams(String s, String p) {
        List<Integer> result = new ArrayList<>();
        if (p.length()>s.length() || p.length()==0) return result;
        Map<Character, Integer> map = new HashMap<>();
        for (int i=0; i<p.length(); i++) {
            map.put(p.charAt(i), map.getOrDefault(p.charAt(i), 0) + 1);
        }

        int cnt = map.size();
        int lo = 0, hi = -1;
        while (hi < s.length()) {
            int len = hi - lo + 1;
            if (len > p.length()) {
                if (map.containsKey(s.charAt(lo))) {
                    map.put(s.charAt(lo), map.get(s.charAt(lo)) + 1);
                    if (map.get(s.charAt(lo)) == 1) {
                        cnt++;
                    }
                }
                lo++;
                continue;
            } else {
                if (cnt == 0 && len == p.length())
                    result.add(lo);
                hi++;
                if (hi < s.length() && map.containsKey(s.charAt(hi))) {
                    map.put(s.charAt(hi), map.get(s.charAt(hi)) - 1);
                    if (map.get(s.charAt(hi)) == 0) {
                        cnt--;
                    }
                }
                continue;
            }
        }
        return result;
    }
}
// @lc code=end

