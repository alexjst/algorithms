/*
5.1.5 Binary Tree Level Order Traversal II
√Ë ˆ
Given a binary tree, return the bottom-up level order traversal of its nodes°Ø values. (ie, from left to right,
level by level from leaf to root).
For example: Given binary tree {3,9,20,#,#,15,7},
3
/ \
9 20
/ \
15 7
return its bottom-up level order traversal as:
[
[15,7]
[9,20],
[3],
]

*/
#include "BinaryTreeLevelOrderII.h"

#include <iostream>
#include <vector>
#include <queue>
using namespace std;

struct Node {
    int data;
    Node* left;
    Node* right;
    Node(int d) :data(d), left(nullptr), right(nullptr) {}
};

void levelOrder(Node* root, vector<vector<int> >& result, int level)
{
    queue<Node*>* q1 = new queue<Node*>();
    queue<Node*>* q2 = new queue<Node*>();

    q1->push(root);

    while (!q1->empty()) {
        Node* n = q1->front();
        q1->pop();
        result.resize(level + 1);
        result[level].push_back(n->data);
        if (n->left) q2->push(n->left);
        if (n->right) q2->push(n->right);
        if (q1->empty()) {
            if (q2->empty()) return;
            swap(q1, q2); ++level;
        }
    }

    reverse(result.begin(), result.end());
}

vector<vector<int> >& bottomUpLevelOrder(Node* root)
{
    vector<vector<int> >* result = new vector<vector<int> >();
    if (root)	levelOrder(root, *result, 0);

    return *result;
}

void BinaryTreeLevelOrderII::run()
{
    //3,9,20,#,#,15,7
    Node n1(3);
    Node n2(9); n1.left = &n2;
    Node n3(20); n1.right = &n3;
    Node n4(15); n2.left = &n4;
    Node n5(7); n2.left = &n5;

    auto result = bottomUpLevelOrder(&n1);
    for (auto level : result) {
        cout << "------------" << endl;
        for (auto d : level) cout << d << " ";
    }
}