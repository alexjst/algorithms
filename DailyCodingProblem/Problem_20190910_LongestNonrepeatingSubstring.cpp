/**
 * This problem was recently asked by Microsoft:

Given a string, find the length of the longest substring without repeating characters.

Here is an example solution in Python language. (Any language is OK to use in an interview, though we'd recommend Python as a generalist language utilized by companies like Google, Facebook, Netflix, Dropbox, Pinterest, Uber, etc.,)

class Solution:
  def lengthOfLongestSubstring(self, s):
    # Fill this in.

print Solution().lengthOfLongestSubstring('abrkaabcdefghijjxxx')
# 10

Can you find a solution in linear time?
*/

/**
 * I will code in CPP
 */

#include <iostream>
#include <string>
#include <vector>

using namespace std;

int lengthOfLongestSubstring(string input) {
    int len = input.length();
    if (len<2) return len;

    // has for 26*2 = 52 chars
    vector<bool> flag(52, false);

    int left = 0;
    flag[input[left]-'A'] = true;

    int right = 0;

    int result = 1;
    while (left<len) {
        while (right<len && flag[input[right]-'A']) {
            flag[input[right]-'A'] = true;
            right++;
        }
        result = max(result, right - left);
        while (left<len) {
            flag[input[left]-'A'] = false;
            left++;
        }
    }
    return result;

}

int main(int argc, char* argv[]) {
    string input = "abrkaabcdefghijjxxx";
    cout << lengthOfLongestSubstring(input) << endl;
}