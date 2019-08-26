/**
 * This problem was asked by Google.

Given the root to a binary tree, implement serialize(root), which serializes the tree into a string, and deserialize(s), which deserializes the string back into the tree.

For example, given the following Node class

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
The following test should pass:

node = Node('root', Node('left', Node('left.left')), Node('right'))
assert deserialize(serialize(node)).left.left.val == 'left.left'
 */

class Node {
    int data;
    Node left;
    Node right;
    Node(int data) {
        this.data = data;
    }
}

class Problem_20190824_TreeSerialization {
    public static String serialize(Node root) {
        if (root == null) return "null";
        else {
            return "(" + String.valueOf(root.data) + "," + serialize(root.left) + "," + serialize(root.right) + ")";
        }
    }

    public static Node deserialize(String s) {
        if (s.equals("null")) return null;
        else {
        }
    }

    public static void main(String[] args) {
        Node n1 = new Node(1);
        Node n2 = new Node(2);
        Node n3 = new Node(3);
        Node n4 = new Node(4);
        n1.left = n2;
        n2.right = n3;
        n1.right = n4;
        Node root = n1;

        String s = serialize(root);
        System.out.println(s);
        // Node r = deserialize(s);
    }
}