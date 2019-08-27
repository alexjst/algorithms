#include "LongestPalindrome.h"

#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

class Solution {
    public:
        string longestPalindrome(string s) {
            int n = s.length();
            if (n==0 || n==1) return s;
            
            // dp[n][n] of boolean where dp[i][j] is true if substring
            // from index i to index j (inclusive) is a palindrome.
            vector<vector<bool>> dp(n, vector<bool>(n,false)) ;

            for (int i=0; i<n; i++) dp[i][i] = true;
            for (int i=1; i<n; i++) dp[i-1][i] = (s[i-1]==s[i]);

            int minStart = 0;
            int maxLen = 1;
            for (int i=2; i<n; i++) {
                for (int j=i-2; j>=0; j--) {
                    if (s[i]==s[j] && dp[j+1][i-1]) {
                        dp[j][i] = true;
                        if (maxLen < (i-j+1)) {
                            maxLen = (i-j+1);
                            minStart = j;
                        }
                    }
                }
            }

            return s.substr(minStart, maxLen);
        }
    };

    int main(int argc, char* argv[]) {
        Solution s;
        cout << s.longestPalindrome("balabala") << endl;
        return 0;
    }