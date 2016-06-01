#include "BalancedBinaryTree.h"

#include <iostream>
#include <vector>
#include <queue>
#include <set>
using namespace std;

struct Node {
    int data;
    Node* left;
    Node* right;
    Node(int d) :data(d), left(nullptr), right(nullptr) {}
};

void dfs(Node* parent, set<int>& depths, int depth)
{
    if (!parent) return;
    if (!parent->left && !parent->right)	{ depths.insert(depth); return; }
    if (parent->left)
        dfs(parent->left, depths, depth + 1);
    if (parent->right)
        dfs(parent->right, depths, depth + 1);

}

bool isBalanced(Node* root)
{
    if (!root) return true;
    set<int> depths;
    dfs(root, depths, 0);
    if ( depths.size() <= 1 || (abs(*depths.begin() - *(prev(depths.end())))<=1) )
        return true;
    else
        return false;
}

void BalancedBinaryTree::run()
{
    cout << "Empty tree: " << isBalanced(nullptr) << endl; // true
    Node n1(1);
    cout << "Single-node tree: " << isBalanced(&n1) << endl; // true
    Node n2(2); n1.left = &n2;
    cout << "Two-node tree: " << isBalanced(&n1) << endl; // true
    Node n3(3); n2.right = &n3;
    cout << "3-node tree: " << isBalanced(&n1) << endl; // true
    Node n4(4); n3.right = &n4;
    cout << "4-node tree: " << isBalanced(&n1) << endl; // true
    Node n5(5); n1.right = &n5;
    cout << "5-node tree: " << isBalanced(&n1) << endl; // false
    Node n6(6); n5.right = &n6;
    cout << "6-node tree: " << isBalanced(&n1) << endl; // true
}

