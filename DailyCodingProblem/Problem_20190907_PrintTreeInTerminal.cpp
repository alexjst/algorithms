/**
 * This is the problem from Amazon onsite interview: Given a binary tree, how do you print it in termianl so it looks like a tree?
 */


#include <iostream>
#include <string>

using namespace std;

class Node {
public:
    Node(int value): left(nullptr), right(nullptr) {
        val = value;
    }
    int val;
    Node* left;
    Node* right;
};

void treePrint(const Node* parent, int indent) {
    for (int i=0; i<indent; i++) cout << "\t";
    cout << ((parent==nullptr) ? "null" : to_string(parent->val));
    cout << endl;
    if (parent) {
        treePrint(parent->left, indent+1);
        treePrint(parent->right, indent+1);
    }
}
void treePrint(const Node* node) {
    int indent = 0;
    treePrint(node, 0);
}

int main(int argc, char* argv[]) {
    Node n1(1);
    Node n2(2);
    Node n3(3);
    Node n4(4);
    Node n5(5);
    Node n6(6);
    Node n7(7);
    Node n8(8);
    Node n9(9);

    n1.left = &n2;
    n1.right = &n3;
    n3.left = &n4;
    n4.left = &n5;
    n5.right = &n6;
    n5.left = &n7;
    n7.left = &n8;
    n8.right = &n9;

    treePrint(&n1);

    return 0;
}