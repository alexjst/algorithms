package alexyang.algorithms.Java.src;

public class Test {
    public static void main(String[] args) {
        Node n1 = new Node(1, null, null);
        Node n3 = new Node(3, null, null);
        Node n2 = new Node(2, n1, n3);
        Node n5 = new Node(5, null, null);
        Node n4 = new Node(4, n2, n5);

        Test t = new Test();
        Node listHead = t.treeToDoublyList(n4);
    }

    // Definition for a Node.
    public static class Node {
        public int val;
        public Node left;
        public Node right;

        public Node() {
        }

        public Node(int _val, Node _left, Node _right) {
            val = _val;
            left = _left;
            right = _right;
        }
    }

    public Node treeToDoublyList(Node root) {
        if (root == null) return null;
        Node dummy = new Node();
        inorder(root, root, root, dummy);
        return dummy.right;
    }
    
    // specification on the output after each recursion: head and tail of list
    // then questions become: 1. how to init head and tail in first recursion
    // and 2. how to update head and tail (the list) after each recursion.
    private void inorder(Node parent, Node head, Node tail, Node dummy) {
        if (parent==null) return;
        if (parent.left==null && dummy.right==null) {
            dummy.right = parent;
            head = parent;
            tail = parent;
        }
        inorder(parent.left, head, tail, dummy);
        head.left = parent;
        tail.right = parent;
        parent.left = tail;
        parent.right = head;
        parent = tail;
        inorder(parent.right, head, tail, dummy);
    }
}
