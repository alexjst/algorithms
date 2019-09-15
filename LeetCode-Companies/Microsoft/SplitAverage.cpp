#include <vector>
#include <queue>
#include <functional>
#include <numeric>
#include <algorithm>
#include <iostream>
#include <stack>
#include <string>
#include <sstream>
#include <unordered_set>
#include <unordered_map>

using namespace std;

/** In a given integer array A, we must move every element of A to either list B or list C. (B and C initially start empty.)

Return true if and only if after such a move, it is possible that the average value of B is equal to the average value of C, and B and C are both non-empty.

Example :
Input:
[1,2,3,4,5,6,7,8]
Output: true
Explanation: We can split the array into [1,4,5,8] and [2,3,6,7], and both of them have the average of 4.5.
Note:

The length of A will be in the range [1, 30].
A[i] will be in the range of [0, 10000].
*/

/* This questions queries two things:
 * 1. How to generate all combinations of a sequence.
 * 2. Floating point number comparison.
 */
class Solution {
public:
    // this solution exceeds memory limit because we are basically keeping all solutions in memory as vector
    // so it may not be scalable to larger array
    bool splitArraySameAverage(vector<int>& A) {
        int sz = A.size();
        if (sz < 2) return false;

        sort(A.begin(), A.end());
        int sum = accumulate(A.begin(), A.end(), 0);
        // the pair contains the count of numbers and the sum of them
        vector<pair<int, int>> countSumList;
        countSumList.push_back(make_pair(0,0));
        for (int i=0; i<(sz-1); i++) {
            int curSz = countSumList.size();
            vector<pair<int, int>> withAi;
            for (int j=0; j<curSz; j++) {
                pair<int,int> p(countSumList[j]);
                p.first += 1;
                p.second += A[i];
                if (equalAvg(p,sum, sz)) {
                    return true;
                } else if (gtAvg(p, sum, sz) || p.first>sz/2) {
                    // prune
                } else {
                    withAi.push_back(p);
                }
            }
            for (auto& p : withAi) {
                countSumList.push_back(p);
            }
        }
        return false;
    }

    // this solution should does DFS
    bool splitArraySameAverageDfs(vector<int>& A) {
        int sz = A.size();
        if (sz < 2) return false;

        sort(A.begin(), A.end());
        int sum = accumulate(A.begin(), A.end(), 0);

        // DFS, like a binary tree, left side is NOT having the number,
        // right side is having the next number
        // <dummy root>
        // |
        // |------------------------------
        // |                             |
        // (no A[0])                     (A[0])
        // |                             |
        // |--------------         |-------------|
        // |             |         |             |
        // (no A[1])    (A[1])     (no A[1])     (A[1])
        // ...
        // ...
        //
        //
        pair<int, int> p = make_pair(0,0);
        bool found = false;
        dfs(A, sum, sz, 0, p, found);
        return found;
    }

    void dfs(const vector<int>& A, const int sum, const int sz, int index, pair<int,int> p, bool& found) {
        if (found) return;
        if (index==sz-1 || p.first>(sz/2)) return;
        auto newP = make_pair(p.first+1, p.second+A[index]);
        if (equalAvg(newP, sum, sz)) {
            found = true;
            return;
        } else if (gtAvg(newP, sum, sz)) {
            return;
        } else {
            dfs(A, sum, sz, index+1, p, found);
            dfs(A, sum, sz, index+1, newP, found);
        }
    }

    // this solution should does DP
    bool splitArraySameAverageDP(vector<int>& A) {
        int sz = A.size();
        if (sz < 2) return false;
        int sum = accumulate(A.begin(), A.end(), 0);
        int limit = sz/2;

        // Dynamic Programming
        vector<unordered_set<int>> dp(limit);
        for (int a : A) {
            for (int i=(limit-1); i>=0; i--) {
                if (i==0) {
                    if (a*sz == sum) return true;
                    dp[i].insert(a);
                } else {
                    for (auto b : dp[i-1]) {
                        if ((b+a)*sz == sum *(i+1)) return true;
                        dp[i].insert(b+a);
                    }
                }
            }
        }
        return false;
    }

private:
    // avoid calculating the 'double' average value
    // for inaccurate comparison, instead, work in integers
    bool equalAvg(pair<int, int>& p, int sum, int sz) {
        return (long)(p.second) * sz == (long)(p.first) * sum;
    }

    bool gtAvg(pair<int, int>& p, int sum, int sz) {
        return (long)(p.second) * sz > (long)(p.first) * sum;
    }
};

int main()
{
    Solution s;
    vector<int> A = {1, 2, 3, 4, 5, 6, 7, 8};
    vector<int> B = {60,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30};
    bool resultA = s.splitArraySameAverage(A);
    cout << resultA << endl;
    bool resultA2 = s.splitArraySameAverageDfs(A);
    cout << resultA2 << endl;
    bool resultB = s.splitArraySameAverageDP(A);
    cout << resultB << endl;
    bool resultC = s.splitArraySameAverageDP(B);
    cout << resultC << endl;
    //system("pause");
}


