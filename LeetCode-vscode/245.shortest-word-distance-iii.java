/*
 * @lc app=leetcode id=245 lang=java
 *
 * [245] Shortest Word Distance III
 *
 * https://leetcode.com/problems/shortest-word-distance-iii/description/
 *
 * algorithms
 * Medium (54.76%)
 * Likes:    175
 * Dislikes: 68
 * Total Accepted:    45.9K
 * Total Submissions: 83.8K
 * Testcase Example:  '["practice", "makes", "perfect", "coding", "makes"]\n"makes"\n"coding"'
 *
 * Given a list of words and two words word1 and word2, return the shortest
 * distance between these two words in the list.
 * 
 * word1 and word2 may be the same and they represent two individual words in
 * the list.
 * 
 * Example:
 * Assume that words = ["practice", "makes", "perfect", "coding", "makes"].
 * 
 * 
 * Input: word1 = “makes”, word2 = “coding”
 * Output: 1
 * 
 * 
 * 
 * Input: word1 = "makes", word2 = "makes"
 * Output: 3
 * 
 * 
 * Note:
 * You may assume word1 and word2 are both in the list.
 * 
 */

import java.util.*;

// @lc code=start
class Solution {
    public int shortestWordDistance(String[] words, String word1, String word2) {
        // first build a map from word to positions
        Map<String, List<Integer>> map = new HashMap<>();
        for (int i = 0; i < words.length; i++) {
            map.putIfAbsent(words[i], new ArrayList<>());
            List<Integer> list = map.get(words[i]);
            list.add(i);
        }
        List<Integer> l1 = map.get(word1);
        List<Integer> l2 = map.get(word2);
        int i=0, j=0;
        int res = words.length;
        while (i<l1.size() && j<l2.size()) {
            int ival = l1.get(i);
            int jval = l2.get(j);
            if (ival != jval) {
                res = Math.min(res, Math.abs(ival-jval));
            }
            if (ival <= jval) {
                i++;
            } else {
                j++;
            }
        }
        return res;
    }
}
// @lc code=end

