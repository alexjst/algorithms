/*
Flatten Binary Tree to Linked List

Given a binary tree, flatten it to a linked list in-place.
For example, Given
1
/  \
2    5
/ \    \
3   4    6
The flattened tree should look like:
1
\
2
\
3
\
4
\
5
\
6

*/
#include "FlattenBinaryTreeToLinkedList.h"

struct Node {
    int data;
    Node* left;
    Node* right;
    Node(int d) : data(d), left(0), right(0) {}
};

// in-place flatten
void flatten(Node* parent) {
    if (!parent) return;
    if (!parent->left && !parent->right) return;
    else {
        flatten(parent->left);
        flatten(parent->right);
        Node* leftNode = parent->left;
        Node* rightNode = parent->right;
        parent->left = 0;
        parent->right = leftNode;
        Node* node = parent;
        while (node->right) node = node->right;
        node->right = rightNode;
    }
}

void FlattenBinaryTreeToLinkedList::run()
{
    Node n1(1);
    Node n2(2);
    Node n3(3);
    Node n4(4);
    Node n5(5);
    Node n6(6);

    n1.left = &n2;
    n1.right = &n5;
    n2.left = &n3;
    n2.right = &n4;
    n5.right = &n6;

    flatten(&n1);

}