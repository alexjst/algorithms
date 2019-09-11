/**
 * This problem was asked by Google.

Given an array of integers and a number k, where 1 <= k <= length of the array, compute the maximum values of each subarray of length k.

For example, given array = [10, 5, 2, 7, 8, 7] and k = 3, we should get: [10, 7, 8, 8], since:

10 = max(10, 5, 2)
7 = max(5, 2, 7)
8 = max(2, 7, 8)
8 = max(7, 8, 7)
Do this in O(n) time and O(k) space. You can modify the input array in-place and you do not need to store the results. You can simply
print them out as you compute them.
*/

#include <iostream>
#include <vector>
#include <queue>
#include <set>
#include <algorithm>

using namespace std;

/**
 * The first solution uses a 'set' that is automatically sorted. A set can also easily add or delete an element.
 */
class Solution1 {
public:
    static void printSlidingWindowMax(const vector<int>& input, int width) {
        int sz = input.size();
        if (sz < width) return;

        // a set automatically has it's max element on in the first position
        set<int, greater<int>> s;
        for (int i=0; i<width; i++) {
            s.insert(input[i]);
        }

        cout << *(s.begin()) << endl;
        for (int i=width; i<sz; i++) {
            s.insert(input[i]);
            s.erase(input[i-width]);
            cout << *(s.begin()) << endl;
        }
    }
};

/**
 * The second solution uses a priority_queue of length 2~3 to make sure
 * the two largest number are in it. We need a min heap.
 */
class Solution2 {
public:
    static void printSlidingWindowMax(const vector<int>& input, int width) {
        int sz = input.size();
        if (sz < width) return;

        // a set automatically has it's max element on in the first position
        set<int, greater<int>> s;
        for (int i=0; i<width; i++) {
            s.insert(input[i]);
        }

        cout << *(s.begin()) << endl;
        for (int i=width; i<sz; i++) {
            s.insert(input[i]);
            s.erase(input[i-width]);
            cout << *(s.begin()) << endl;
        }
    }
};

int main(int argc, char* argv[]) {
    vector<int> myArray{10, 5, 2, 7, 8, 7};
    cout << "Solution 1:" << endl;
    Solution1::printSlidingWindowMax(myArray, 3);
    cout << "Solution 2:" << endl;
    Solution2::printSlidingWindowMax(myArray, 3);
}

/** 
 * The idea is just keep a ordered set to contain the elements from the window and always
 * return its max element. We are able to do this because we can find elements by value
 * from the set so making sure the content is correct.
 * 
 * The problem to implement this for the problem is that, performance is actually O(nlog(k)), because
 * for each new sliding window I'll need log(k) time to find its max.
 * 
 * To ensure O(n) linear time, we can actually keep the size of the set a small constant, because we
 * only need to keep two largest value in the set.
 * 
 **/
