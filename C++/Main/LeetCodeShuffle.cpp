#include "LeetCodeShuffle.h"

#include <iostream>
#include <vector>
#include <string>
#include <ctime>
#include <algorithm>

using namespace std;

vector<string> problems_titles = {
    /*arrays*/
    "Remove Duplicated from Sorted Array",
    "Remove Duplicated from Sorted Array II",
    "Search in Rotated Sorted Array",
    "Seach in Rotated Sorted Array II",
    "Median of Two Sorted Arrays",
    "Longest Consecutive Sequence",
    "Two Sum",
    "3Sum",
    "3Sum Closest",
    "4Sum",
    "Remove Element",
    "Next Permutation",
    "Permutation Sequence",
    "Valid Sudoku",
    "Trapping Rain Water",
    "Rotate Image",
    "Plus One",
    "Climing Stairs",
    "Gray Code",
    "Set Matrix Zeroes",
    "Gas Station",
    "Candy",
    "Single Number",
    "Single Number II",
    /*linked list*/
    "Add Two Numbers",
    "Reverse Linked List II",
    "Parititin List",
    "Remove Duplicates from Sorted List",
    "Remove Duplicates from Sorted List II",
    "Rotate List",
    "Remove Nth Node from End of List",
    "Swap Nodes in Pairs",
    "Reverse Nodes in k-Group",
    "Copy List with Random Pointer",
    "Linked List Cycle",
    "Linked List Cycle II",
    "Reorder List",
    "LRU Cache",
    /* strings*/
    "Valid Palindrome",
    "Implement strStr()",
    "String to Integer (atoi)",
    "Add Binary",
    "Longest Palindromic Substring",
    "Regular Expression Matching",
    "Wildcard Matching",
    "Longest Common Prefix",
    "Valid Number",
    "Integer to Roman",
    "Roman to Integer",
    "Count and Say",
    "Anagrams",
    "Simplify Path",
    "Length of Last Word",
    /*stacks and queues*/
    "Valid Parentheses",
    "Longest Valid Parenthesis",
    "Largest Rectangle in Histogram",
    "Evaluate Reverse Polish Notation",
    /*trees*/
    "Binary Tree Preorder Traversal",
    "Binary Tree Inorder Traversal",
    "Binary Tree Postorder Traversal",
    "Binary Tree Level Order Traversal",
    "Binary Tree Level Order Traversal II",
    "Binary Tree Zigzag Level Order Traversal",
    "Recover Binary Search Tree",
    "Same Tree",
    "Symmetric Tree",
    "Balanced Binary Tree",
    "Flatten Binary Tree to Linked List",
    "Populating Next Right Pointers in Each Node II",
    /*constructing binary trees*/
    "Construct Binary Tree from Preorder and Inorder Traversal",
    "Construct Binary Tree from Inorder and Postorder Traversal",
    /*binary search trees*/
    "Unique Binary Search Trees",
    "Unique Binary Search Trees II",
    "Validate Binary Search Tree",
    "Convert Sorted Array to Binary Search Tree",
    /*recursion of binary trees*/
    "Minimum Depth of Binary Tree",
    "Maximum Depth of Binary Tree",
    "Path Sum",
    "Path Sum II",
    "Binary Tree Maximum Path Sum",
    "Populating Next Right Pointers in Each Node",
    "Sum Root to Leaf Numbers",
    /*Sorting*/
    "Merge Sorted Array",
    "Merge Two Sorted Lists",
    "Merge K sorted Lists",
    "Insertion Sort List",
    "Sort List",
    "First Missing Positive",
    "Sort Colors",
    /*searching*/
    "Search for a Range",
    "Search Insert Position",
    "Search a 2D matrix",
    /*brute force*/
    "Subset (recursion/iteration)",
    "Subset II (recursion/iteration)",
    "Permutations I",
    "Permutations II",
    "Combinations",
    "Letter Combinations of a Phone",
    /*BFS*/
    "Word Ladder",
    "Word Ladder II",
    "Surrounded Regions",
    /*DFS*/
    "Palindrome Partitining",
    "Unique Paths",
    "Unique Paths II",
    "N-Queens",
    "N-Queens II",
    "Restore IP Addresses",
    "Combination Sum",
    "Combination Sum II",
    "Generate Parnetheses",
    "Sudoku Solver",
    "Word Search",
    /*Divide&Conquer*/
    "Pow(x,n)",
    "Sqrt(x)",
    /*Greedy*/
    "Jump Game",
    "Jump Game II",
    "Best Time to Buy and Sell Stock",
    "Best Time to Buy and Sell Stock II",
    "Longest Substring Without Repeating Characters",
    "Container with Most Water",
    /*Dynamic Programming*/
    "Trangle",
    "Maximum Subarray",
    "Palindrome Partitioning II",
    "Maximal Rectangle",
    "Best Time to Buy and Sell Stock III",
    "Interleaving String",
    "Scramble String",
    "Minimum Path Sum",
    "Edit Distance",
    "Decode Ways",
    "Distinct Subsequences",
    "Word Break",
    "Word Break II",
    /*Graph*/
    "Clone Graph",
    /*details in coding*/
    "Reverse Integer",
    "Palindrome Number",
    "Insert Interval",
    "Merge Intervals",
    "Mininum Window Substring",
    "Multiply Strings",
    "Substring with Concatenation of All Words",
    "Pascal's Triangle",
    "Pascal's Triangle II",
    "Spiral Matrix",
    "Spiral Matrix II",
    "Zigzag Conversion",
    "Divide Two Integers",
    "Text Justification",
    "Max Points on a Line"
};


void LeetCodeShuffle::run()
{
    // i am running this program just to select random problems from LeetCode
    const int LOWER_BOUND = 1;
    const int UPPER_BOUND = problems_titles.size();
    const int PROBLEM_NUM = 10;

    int len = UPPER_BOUND - LOWER_BOUND + 1;
    vector<int> ids(len);
    int cnt = 0;
    generate(ids.begin(), ids.end(), [&cnt]()->int{ return ++cnt; });
    srand((unsigned)time(0));
    for (int i = 1; i < len; i++) {
        int idx = rand() % (i+1);
        swap(ids[idx], ids[i]);
    }
    vector<int> result;
    for_each(ids.begin(), ids.begin() + PROBLEM_NUM, [&result](int i){ result.push_back(i); });
    sort(result.begin(), result.end());
    for_each(result.begin(), result.end(), [&](int i){ cout << i+1 << ": " << problems_titles[i] << endl; });
}
