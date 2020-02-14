/*
 * @lc app=leetcode id=250 lang=java
 *
 * [250] Count Univalue Subtrees
 *
 * https://leetcode.com/problems/count-univalue-subtrees/description/
 *
 * algorithms
 * Medium (50.95%)
 * Likes:    411
 * Dislikes: 97
 * Total Accepted:    53.7K
 * Total Submissions: 105.3K
 * Testcase Example:  '[5,1,5,5,5,null,5]'
 *
 * Given a binary tree, count the number of uni-value subtrees.
 * 
 * A Uni-value subtree means all nodes of the subtree have the same value.
 * 
 * Example :
 * 
 * 
 * Input:  root = [5,1,5,5,5,null,5]
 * 
 * ⁠             5
 * ⁠            / \
 * ⁠           1   5
 * ⁠          / \   \
 * ⁠         5   5   5
 * 
 * Output: 4
 * 
 * 
 */

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
    public int countUnivalSubtrees(TreeNode root) {
        return countEval(root).count;
    }

    private Result countEval(TreeNode root) {
        if (root == null) return new Result(0, true);
        if (root.left == null && root.right == null) return new Result(1, true);
        Result leftRes = countEval(root.left);
        Result rightRes = countEval(root.right);
        Result res = new Result(0, false);
        res.count += leftRes.count;
        res.count += rightRes.count;
        res.unival = leftRes.unival && rightRes.unival
                && (root.left == null || root.left.val == root.val)
                && (root.right == null || root.right.val == root.val);
        if (res.unival) {
            res.count++;
        }
        return res;
    }
}

class Result {
    int count;
    boolean unival;
    public Result(int count, boolean unival) {
        this.count = count;
        this.unival = unival;
    }
}
// @lc code=end

