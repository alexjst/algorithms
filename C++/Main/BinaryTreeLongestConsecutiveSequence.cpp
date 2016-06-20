#include "BinaryTreeLongestConsecutiveSequence.h"

#include <algorithm>
#include <vector>
#include <iostream>

using namespace std;

struct TreeNode{
    int val;
    TreeNode* left;
    TreeNode* right;
    TreeNode(int v) : val(v), left(NULL), right(NULL) {}
};

class Solution {
public:
    int longestConsecutive(TreeNode* root) {
        vector<int> seq;
        int result = 0;
        int curLen = 0;
        dfs(root, seq, result, curLen);
        return result;
    }

    void dfs(TreeNode* parent, vector<int>& seq, int& result, int curLen) {
        if (!parent) return;

        seq.push_back(parent->val);
        if (seq.size() == 1) curLen = 1;
        else {
            // seq.size() > 1
            if (seq[seq.size() - 2] + 1 == seq[seq.size() - 1])
                curLen++;
            else
                curLen = 1;
        }
        result = max(result, curLen/*longest consec seq from 'seq'*/);
        dfs(parent->left, seq, result, curLen);
        dfs(parent->right, seq, result, curLen);
        seq.pop_back();
    }
};

void BinaryTreeLongestConsecutiveSequence::run()
{
    TreeNode n1(1);
    TreeNode n2(2);
    TreeNode n3(3);
    TreeNode n4(1);
    TreeNode n5(3);
    TreeNode n6(2);
    TreeNode n7(4);

    n1.left = &n2;
    n1.right = &n3;
    n2.left = &n4;
    n2.right = &n5;
    n3.left = &n6;
    n3.right = &n7;

    Solution s;

    cout << s.longestConsecutive(&n1) << endl;

}