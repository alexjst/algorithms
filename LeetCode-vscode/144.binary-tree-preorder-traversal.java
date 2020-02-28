/*
 * @lc app=leetcode id=144 lang=java
 *
 * [144] Binary Tree Preorder Traversal
 *
 * https://leetcode.com/problems/binary-tree-preorder-traversal/description/
 *
 * algorithms
 * Medium (53.76%)
 * Likes:    1166
 * Dislikes: 49
 * Total Accepted:    431.4K
 * Total Submissions: 800K
 * Testcase Example:  '[1,null,2,3]'
 *
 * Given a binary tree, return the preorder traversal of its nodes' values.
 * 
 * Example:
 * 
 * 
 * Input: [1,null,2,3]
 * ⁠  1
 * ⁠   \
 * ⁠    2
 * ⁠   /
 * ⁠  3
 * 
 * Output: [1,2,3]
 * 
 * 
 * Follow up: Recursive solution is trivial, could you do it iteratively?
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
    /*
     * Iterative solution thoughts: 
     * 1. Use a queue to keep the right arm (root, right, right, ...)
     * 2. Dequeue the first one, get its left child's right arm
     * 
     * Example:
     *  1
     *    2
     *  3
     * 
     * s (small stack): 2 1
     * S (result stack): 1 2
     * 
     * whils S is not empty:
     *   get top item "t"
     *   print t (put t to final result)
     *   get t's left child's right children chain into S
     */
    public List<Integer> preorderTraversal(TreeNode root) {
        List<Integer> res = new ArrayList<>();
        Stack<TreeNode> stack = new Stack<>();
        Stack<TreeNode> s = new Stack<>();
        while (root != null) {
            s.push(root);
            root = root.right;
        }
        while (!s.isEmpty()) {
            stack.push(s.pop());
        }

        /*
        if (stack.isEmpty()) {
            return res;
        }
        */

        while (!stack.isEmpty()) {
            TreeNode n = stack.pop();
            res.add(n.val);
            TreeNode cur = n.left;
            while (cur != null) {
                s.push(cur);
                cur = cur.right;
            }
            while (!s.isEmpty()) {
                stack.push(s.pop());
            }
        }
        return res;
    }
}
// @lc code=end

