#include "TreePreorderIteratively.h"

#include <iostream>
#include <stack>
#include <vector>

using namespace std;

struct Node{
	int data;
	Node* left;
	Node* right;

	Node(int d) { data = d; left = nullptr; right = nullptr; }
};

void TreePreorderIteratively::run()
{
	Node a(1);
	Node b(2);
	Node c(3);
	Node d(4);
	Node e(5);

	a.left = &b;
	a.right = &c;
	c.left = &d;
	c.right = &e;


	// now do preorder: 1, 2, 3, 4, 5
	cout << "PreOrder: ";
	Node* root = &a;
	vector<int> output;
	stack<Node*> nodeStack;
	Node* p = root;
	if (root != 0) nodeStack.push(p);
	while (!nodeStack.empty()) {
		Node* n = nodeStack.top();
		output.push_back(n->data);
		nodeStack.pop();
		p = n->right;
		if (p)
			nodeStack.push(p);
		p = n->left;
		if (p)
			nodeStack.push(p);
	}
	for (int i = 0; i < output.size(); i++) {
		cout << output[i] << ", ";
	}
	cout << endl;

	// now do PostOrder: 5
	cout << "PostOrder: ";
	output.clear();
	p = root;
	if (root != 0) nodeStack.push(p);
	while (!nodeStack.empty()) {
		Node* n = nodeStack.top();
		p = n->right;
		if (p)
			nodeStack.push(p);
		output.push_back(n->data);
		nodeStack.pop();
		p = n->left;
		if (p)
			nodeStack.push(p);
	}
	for (int i = 0; i < output.size(); i++) {
		cout << output[i] << ", ";
	}
	cout << endl;
}
