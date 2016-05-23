/*
Given a string s, partition s such that every substring of the partition is a palindrome.
Return all possible palindrome partitioning of s.
For example, given s = ¡±aab¡±, Return
[
["aa","b"],
["a","a","b"]
]
*/

#include "ParlindromePartitioning.h"
#include <string>
#include <iostream>

using namespace std;

bool isParlindrome(const string& input, int start, int end)
{
    if (start >= input.length() || end < 0 || end < start) return false;

    while (start < end) {
        if (input[start++] != input[end--])
            return false;
    }
    return true;
}
void doPartition(const string& input, int start, int end)
{
    for (unsigned int i = start; i <= end; i++) {
        if (isParlindrome(input, start, i)) {
            if (start == 0)
                cout << endl;
            cout << "\"" << input.substr(start, i - start + 1) << "\"";
            doPartition(input, i + 1, end);
        }
    }
}
void parlinDromePartition(const string& input)
{
    int len = input.length();
    doPartition(input, 0, len - 1);
}

void ParlindromePartitioning::run()
{
    string input("aab");
    parlinDromePartition(input);
}

