#include <vector>
#include <queue>
#include <functional>
#include <algorithm>
#include <iostream>
#include <stack>
#include <string>
#include <sstream>
#include <unordered_map>

using namespace std;

class Solution {
public:
    string simplifyPath(string path) {
        stack<string> pathStack;
        int len = path.length();
        if (len <= 1) return path;

        for (int i = 0; i<len; i++) {
            if (i == 0 || path[i] == '/') {
                // find the next '/' or end of string
                for (int j = i + 1; j <= len; j++) {
                    if (j == len || path[j] == '/') {
                        j--;
                        int start = i + 1, end = j;
                        if (end >= start) {
                            string sub = path.substr(start, end - start + 1);
                            if (sub.compare(".") == 0) {}
                            else if (sub.compare("..") == 0) {
                                if (pathStack.size()>0) pathStack.pop();
                            }
                            else {
                                pathStack.push(sub);
                            }
                        }
                        i = j; break;
                    }
                }
            }
        }
        vector<string> pathVec;
        while (!pathStack.empty()) {
            pathVec.push_back(pathStack.top());
            pathStack.pop();
        }
        reverse(pathVec.begin(), pathVec.end());
        string result;
        for (auto& p : pathVec) {
            result = result + "/" + p;
        }
        if (result.empty()) result = "/";
        return result;
    }
};

int main()
{
    Solution s;
    string result = s.simplifyPath("/a/./b/../../c/");
	system("pause");
}