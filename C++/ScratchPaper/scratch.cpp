#include <vector>
#include <queue>
#include <functional>
#include <numeric>
#include <algorithm>
#include <iostream>
#include <stack>
#include <string>
#include <sstream>
#include <unordered_map>

using namespace std;

class Solution {
public:
    bool splitArraySameAverage(vector<int>& A) {
        int sz = A.size();
        if (sz < 2) return false;
        
        sort(A.begin(), A.end());
        int sum = accumulate(A.begin(), A.end(), 0);
        vector<pair<int, int>> countSumList;
        double totalAvg = ((double)sum)/((double)sz);
        countSumList.push_back(make_pair(0,0));
        for (int i=0; i<sz; i++) {
            vector<pair<int, int>> without(countSumList);
            vector<pair<int, int>> withAi;
            for (auto& p : without) {
                p.first += 1;
                p.second += A[i];
                if (equalAvg(p,totalAvg)) {
                    return true;
                } else if (gtAvg(p, totalAvg)) {
                    // do nothing
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

private:
    bool equalAvg(pair<int, int>& p, double avg) {
        return doubleEqual(((double)(p.second))/((double)(p.first)), avg);
    }
    bool gtAvg(pair<int, int>& p, double avg) {
        return doubleEqual(((double)(p.second))/((double)(p.first)), avg);
    }
    bool doubleEqual(double a, double b) {
        if (abs(a-b) < 0.0001) return true;
        else return false;
    }
    bool doubleGt(double a, double b) {
        if ((a-b) > 0.0001) return true;
        else return false;
    }
};

int main()
{
    Solution s;
    vector<int> A = {1, 2, 3, 4, 5, 6, 7, 8};
    bool result = s.splitArraySameAverage(A);
    cout << result << endl;
	//system("pause");
}