#include <iostream>
#include <vector>
#include <set>
#include <map>
#include <unordered_map>
#include <algorithm>

using namespace std;

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

class Solution {
public:
    void flatten(TreeNode* root) {
        flattenTree(root);
        cout << "List follows:" << endl;
        while (root) {
        	if (root->left) cout << endl << "Error: root with value " << root->val << " has left child with value " << root->left->val << endl;
        	cout << root->val;
        	root = root->right;
        }
        cout << endl << "End of list" << endl;
    }
    
    // returns the head and tail of the flattened linked list
    pair<TreeNode*, TreeNode*> flattenTree(TreeNode* root) {
        if (!root) return make_pair(nullptr, nullptr);
        TreeNode* head = root;
        TreeNode* tail = root;
        TreeNode* orgLeft = root->left;
        TreeNode* orgRight = root->right;
        if (orgLeft) {
            auto listEnds = flattenTree(orgLeft);
            tail->right = listEnds.first;
            tail = listEnds.second;
            root->left = nullptr;
            tail->right = nullptr;
        }
        if (orgRight) {
            auto listEnds = flattenTree(orgRight);
            tail->right = listEnds.first;
            tail = listEnds.second;
            root->left = nullptr;
            tail->right = nullptr;
        }
        cout << "With root value = " << root->val << "; flattened head=" << head->val << "; tail=" << tail->val << endl;
        return make_pair(head, tail);
    }
};

int main()
{
	TreeNode n1(1);
	TreeNode n2(2);
	n1.left = &n2;
	Solution s;
	s.flatten(&n1);

	cout << "Hello world" << endl;
	return 0;
}
