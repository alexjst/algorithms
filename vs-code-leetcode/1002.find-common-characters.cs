/*
 * @lc app=leetcode id=1002 lang=csharp
 *
 * [1002] Find Common Characters
 *
 * https://leetcode.com/problems/find-common-characters/description/
 *
 * algorithms
 * Easy (67.19%)
 * Likes:    776
 * Dislikes: 94
 * Total Accepted:    64.7K
 * Total Submissions: 96.1K
 * Testcase Example:  '["bella","label","roller"]'
 *
 * Given an array A of strings made only from lowercase letters, return a list
 * of all characters that show up in all strings within the list (including
 * duplicates).  For example, if a character occurs 3 times in all strings but
 * not 4 times, you need to include that character three times in the final
 * answer.
 * 
 * You may return the answer in any order.
 * 
 * 
 * 
 * 
 * Example 1:
 * 
 * 
 * Input: ["bella","label","roller"]
 * Output: ["e","l","l"]
 * 
 * 
 * 
 * Example 2:
 * 
 * 
 * Input: ["cool","lock","cook"]
 * Output: ["c","o"]
 * 
 * 
 * 
 * 
 * Note:
 * 
 * 
 * 1 <= A.length <= 100
 * 1 <= A[i].length <= 100
 * A[i][j] is a lowercase letter
 * 
 * 
 * 
 */

// @lc code=start
using System;
using System.Linq;
using System.Collections.Generic;
public class Solution {
    public IList<string> CommonChars(string[] A) {
        IList<string> res = new List<string>();
        if (A == null || A.Length<1) return res;

        int[] counts = new int[26];
        Array.Fill(counts, int.MaxValue);

        int[] ccounts = new int[26];
        foreach (var a in A)
        {
            foreach (var c in a.ToCharArray())
            {
                ccounts[c-'a']++;
            }
            for (int i=0; i<26; i++) {
                if (counts[i] > 0) {
                    counts[i] = Math.Min(counts[i], ccounts[i]);
                }
            }
            Array.Fill(ccounts, 0);
        }

        for (int i=0; i<26; i++) {
            int cnt = counts[i];
            if (cnt > 0) {
                for (int j=0; j<cnt; j++) {
                    res.Add(((char)('a'+i)).ToString());
                }
            }
        }
        return res;
    }
}
// @lc code=end

