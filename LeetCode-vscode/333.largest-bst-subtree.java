/*
 * @lc app=leetcode id=333 lang=java
 *
 * [333] Largest BST Subtree
 *
 * https://leetcode.com/problems/largest-bst-subtree/description/
 *
 * algorithms
 * Medium (34.59%)
 * Likes:    511
 * Dislikes: 50
 * Total Accepted:    40.2K
 * Total Submissions: 116K
 * Testcase Example:  '[10,5,15,1,8,null,7]'
 *
 * Given a binary tree, find the largest subtree which is a Binary Search Tree
 * (BST), where largest means subtree with largest number of nodes in it.
 * 
 * Note:
 * A subtree must include all of its descendants.
 * 
 * Example:
 * 
 * 
 * Input: [10,5,15,1,8,null,7]
 * 
 * ⁠  10 
 * ⁠  / \ 
 * ⁠ 5  15 
 * ⁠/ \   \ 
 * 1   8   7
 * 
 * Output: 3
 * Explanation: The Largest BST Subtree in this case is the highlighted one.
 * ⁠            The return value is the subtree's size, which is 3.
 * 
 * 
 * Follow up:
 * Can you figure out ways to solve it with O(n) time complexity?
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
/**
 * Do a postorder traversal, for each node return a tuple [left_bound, right_bound, subtree_size, is_bst]
 */
class Solution {
    int max = 0;
    public int largestBSTSubtree(TreeNode root) {
        if (root==null) return 0;
        postorder(root);
        return max;
    }

    private Res postorder(TreeNode root) {
        if (root==null) return null;
        Res leftRes = postorder(root.left);
        Res rightRes = postorder(root.right);
        int leftBound = root.val;
        int rightBound = root.val;
        int size = 1;
        boolean isBst = true;
        if (leftRes!=null) {
            leftBound = Math.min(leftBound, leftRes.leftBound);
            size += leftRes.size;
            if (leftRes.isBst==false || leftRes.rightBound>=root.val) {
                isBst = false;
            }
        }
        if (rightRes!=null) {
            rightBound = Math.max(rightBound, rightRes.rightBound);
            size += rightRes.size;
            if (rightRes.isBst==false || rightRes.leftBound<=root.val) {
                isBst = false;
            }
        }
        if (isBst) {
            max = Math.max(max, size);
        }
        return new Res(leftBound, rightBound, size, isBst);

    }
}

class Res {
    int leftBound;
    int rightBound;
    int size;
    boolean isBst;
    public Res(int leftBound, int rightBound, int size, boolean isBst) {
        this.leftBound = leftBound;
        this.rightBound = rightBound;
        this.size = size;
        this.isBst = isBst;
    }
}
// @lc code=end

