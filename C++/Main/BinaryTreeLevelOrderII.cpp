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
#include <algorithm>
using namespace std;

struct Node {
	int data;
	Node* left;
	Node* right;
	Node(int d) : data(d), left(nullptr), right(nullptr) {};
};

void dfs(Node* parent, vector<vector<int> >& result, int level) {
	if (!parent) return;
	if (level == result.size())
		result.push_back(vector<int>());
	result[level].push_back(parent->data);
	dfs(parent->left, result, level + 1);
	dfs(parent->right, result, level + 1);
}

vector<vector<int>>  bottomUpLevelOrder(Node* root) {
	vector<vector<int> > result;
	dfs(root, result, 0);
	reverse(result.begin(), result.end());
	return result;
}


void BinaryTreeLevelOrderII::run()
{
    //3,9,20,#,#,15,7
    Node n1(3);
    Node n2(9); n1.left = &n2;
    Node n3(20); n1.right = &n3;
    Node n4(15); n2.left = &n4;
    Node n5(7); n2.right = &n5;

    auto result = bottomUpLevelOrder(&n1);
    for (auto level : result) {
        cout << "\n------------" << endl;
        for (auto d : level) cout << d << " ";
    }
}
