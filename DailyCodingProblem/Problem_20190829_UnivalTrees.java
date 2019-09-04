/**
 * This problem was asked by Google.

A unival tree (which stands for "universal value") is a tree where all nodes under it have the same value.

Given the root to a binary tree, count the number of unival subtrees.

For example, the following tree has 5 unival subtrees:

   0
  / \
 1   0
    / \
   1   0
  / \
 1   1

 */

class Problem_20190829_UnivalTrees {
    static class Node {
        int val;
        Node left;
        Node right;
        Node(int d) { this.val = d; left = null; right = null;}
    }

    public static void main(String[] args) {
        Node n1 = new Node(0);
        Node n2 = new Node(1);
        Node n3 = new Node(0);
        Node n4 = new Node(1);
        Node n5 = new Node(0);
        Node n6 = new Node(1);
        Node n7 = new Node(1);

        n1.left = n2;
        n1.right = n3;
        n3.left = n4;
        n3.right = n5;
        n4.left = n6;
        n4.right = n7;

        System.out.println(getUnivalTreesCount(n1)[0]);
    }

    // returns a pair (a short array): [uival_subtrees_count, whole_tree_contains_single_value]
    public static int[] getUnivalTreesCount(Node root) {
        if (root == null) return new int[]{0, 1};

        int[] leftResult = getUnivalTreesCount(root.left);
        int[] rightResult = getUnivalTreesCount(root.right);

        boolean isLeftUnival = leftResult[1] == 1;
        boolean isRightUnival = rightResult[1] == 1;

        boolean isUnival = isLeftUnival && isRightUnival
            && (root.left == null || root.left.val == root.val)
            && (root.right == null || root.right.val == root.val);

        return new int[]{leftResult[0] + rightResult[0] + (isUnival ? 1 : 0), isUnival ? 1 : 0};
    }
}

/**
 * The unival subtrees count of a parent node is equal to the sum of unival subtrees counts of both children
 * and possibly 1 more if the whole tree under the parent node is unival. In order to tell if the whole subtree
 * is unival, we keep an extra recursion variable
 * 
 * Learnings: during tree DSF, we can return a strucutre of values for each recursion.
 */