/*
 * @lc app=leetcode id=508 lang=java
 *
 * [508] Most Frequent Subtree Sum
 *
 * https://leetcode.com/problems/most-frequent-subtree-sum/description/
 *
 * algorithms
 * Medium (56.47%)
 * Likes:    514
 * Dislikes: 103
 * Total Accepted:    62.1K
 * Total Submissions: 109.8K
 * Testcase Example:  '[5,2,-3]'
 *
 * 
 * Given the root of a tree, you are asked to find the most frequent subtree
 * sum. The subtree sum of a node is defined as the sum of all the node values
 * formed by the subtree rooted at that node (including the node itself). So
 * what is the most frequent subtree sum value? If there is a tie, return all
 * the values with the highest frequency in any order.
 * 
 * 
 * Examples 1
 * Input:
 * 
 * ⁠ 5
 * ⁠/  \
 * 2   -3
 * 
 * return [2, -3, 4], since all the values happen only once, return all of them
 * in any order.
 * 
 * 
 * Examples 2
 * Input:
 * 
 * ⁠ 5
 * ⁠/  \
 * 2   -5
 * 
 * return [2], since 2 happens twice, however -5 only occur once.
 * 
 * 
 * Note:
 * You may assume the sum of values in any subtree is in the range of 32-bit
 * signed integer.
 * 
 */

import java.util.*;

// @lc code=start
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class Solution {
    // elements -> freq
    Map<Integer,Integer> map = new HashMap<>();
    // freq -> list of elements
    Map<Integer,List<Integer>> fmap = new HashMap<>();
    int maxf = 0;
    public int[] findFrequentTreeSum(TreeNode root) {
        List<Integer> res = new ArrayList<>();
        if (root==null) return new int[0];
        dfs(root);
        for (Map.Entry<Integer,Integer> entry : map.entrySet()) {
            if (entry.getValue() == maxf) {
                res.add(entry.getKey());
            }
        }
        int[] ares = new int[res.size()];
        for (int i=0; i<res.size(); i++) {
            ares[i] = res.get(i);
        }
        return ares;
    }

    private Integer dfs(TreeNode parent) {
        if (parent==null) return null;
        int sum  = parent.val;
        if (parent.left != null) {
            sum += dfs(parent.left);
        }
        if (parent.right != null) {
            sum += dfs(parent.right);
        }
        int freq = map.getOrDefault(sum, 0) + 1;
        map.put(sum, freq);
        maxf = Math.max(maxf, freq);
        return sum;
    }
}
// @lc code=end

