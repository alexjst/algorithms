/*
 * @lc app=leetcode id=94 lang=java
 *
 * [94] Binary Tree Inorder Traversal
 *
 * https://leetcode.com/problems/binary-tree-inorder-traversal/description/
 *
 * algorithms
 * Medium (60.47%)
 * Likes:    2463
 * Dislikes: 102
 * Total Accepted:    623.8K
 * Total Submissions: 1M
 * Testcase Example:  '[1,null,2,3]'
 *
 * Given a binary tree, return the inorder traversal of its nodes' values.
 * 
 * Example:
 * 
 * 
 * Input: [1,null,2,3]
 * ⁠  1
 * ⁠   \
 * ⁠    2
 * ⁠   /
 * ⁠  3
 * 
 * Output: [1,3,2]
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
    /**
     * 1) Create an empty stack S.
     * 2) Initialize current node as root
     * 3) Push the current node to S and set current = current->left until current is NULL
     * 4) If current is NULL and stack is not empty then
     *     a) Pop the top item from stack.
     *     b) Print the popped item, set current = popped_item->right
     *     c) Go to step 3.
     * 5) If current is NULL and stack is empty then we are done.
     */
    public List<Integer> inorderTraversal(TreeNode root) {
        // non-trival solution to use iteration and a stack
        List<Integer> res = new ArrayList<>();
        if (root==null) return res;
        Stack<TreeNode> s = new Stack<>();
        TreeNode cur = root;
        while (!s.isEmpty() || cur !=null) {
            while (cur != null) {
                s.push(cur);
                cur = cur.left;
            }
            if (cur == null && !s.isEmpty()) {
                TreeNode popped = s.pop();
                res.add(popped.val);
                cur = popped.right;
            }
        }
        return res;
    }
}
// @lc code=end

