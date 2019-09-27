/**
 * This problem was asked by Dropbox.

Given the root to a binary search tree, find the second largest node in the tree.
 */

class SecondLargestNode {
    static class TreeNode {
        TreeNode left;
        TreeNode right;
        int data;
    }

    TreeNode secondLargest(TreeNode root) {
        if (root == null) return null;
        TreeNode secondLargest = null;
        treeSize(root, root, secondLargest);
        return secondLargest;
    }

    int treeSize(TreeNode root, TreeNode parent, TreeNode secondLargest) {
        int leftSize = parent.left == null ? 0 : treeSize(root, parent.left, secondLargest);
        int rightSize = parent.right == null ? 0 : treeSize(root, parent.right, secondLargest);
        if (parent == root) {
            if (leftSize > rightSize) secondLargest = parent.left;
            else secondLargest = parent.right;
        }
        return leftSize + rightSize + 1;
    }
}