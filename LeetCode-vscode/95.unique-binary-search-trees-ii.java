/*
 * @lc app=leetcode id=95 lang=java
 *
 * [95] Unique Binary Search Trees II
 *
 * https://leetcode.com/problems/unique-binary-search-trees-ii/description/
 *
 * algorithms
 * Medium (38.28%)
 * Likes:    1741
 * Dislikes: 140
 * Total Accepted:    170K
 * Total Submissions: 442K
 * Testcase Example:  '3'
 *
 * Given an integer n, generate all structurally unique BST's (binary search
 * trees) that store values 1 ... n.
 * 
 * Example:
 * 
 * 
 * Input: 3
 * Output:
 * [
 * [1,null,3,2],
 * [3,2,null,1],
 * [3,1,null,null,2],
 * [2,1,3],
 * [1,null,2,null,3]
 * ]
 * Explanation:
 * The above output corresponds to the 5 unique BST's shown below:
 * 
 * ⁠  1         3     3      2      1
 * ⁠   \       /     /      / \      \
 * ⁠    3     2     1      1   3      2
 * ⁠   /     /       \                 \
 * ⁠  2     1         2                 3
 * 
 * 
 */

import java.util.*;

import javax.swing.tree.TreeNode;

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
    public List<TreeNode> generateTrees(int n) {
        return gen(1, n);
    }

    private List<TreeNode> gen(int lo, int hi) {
        List<TreeNode> res = new ArrayList<>();
        if (hi<lo) return res;
        if (lo==hi) {
            TreeNode root = new TreeNode(lo);
            res.add(root);
            return res;
        }
        for (int i=lo; i<=hi; i++) {
            List<TreeNode> left = gen(lo, i-1);
            List<TreeNode> right = gen(i+1, hi);
            if (left.isEmpty()) {
                for (TreeNode node : right) {
                    TreeNode root = new TreeNode(i);
                    root.right = node;
                    res.add(root);
                }
            }
            if (right.isEmpty()) {
                for (TreeNode node : left) {
                    TreeNode root = new TreeNode(i);
                    root.left = node;
                    res.add(root);
                }
            }
            for (TreeNode l : left) {
                for (TreeNode r : right) {
                    TreeNode root = new TreeNode(i);
                    root.left = l;
                    root.right = r;
                    res.add(root);
                }
            }
        }
        return res;
    }
}
// @lc code=end

