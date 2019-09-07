/**
 * This problem was asked by Facebook.

Given a stream of elements too large to store in memory, pick a random element from the stream with uniform probability.
 */

/**
 * It is super important to understand the problem statement:
 * If the problem does not say "too large to store in memory", then we simply keep arr[N] in the memory and then select random i from [0,N)
 * and return arr[i]. But the problem with 'too large to store in memory' means, we cannot have the full array "arr[N]" in our program. What
 * we can have in our code is just the index number i which increases.
 * the elements itself is too large so we need to release it while processing.
 * 
 */
#include <cstdlib>
#include <iostream>
#include <vector>
#include <ctime>

using namespace std;

class Problem_20190905_RandomFromHugeSet {
public:
    Problem_20190905_RandomFromHugeSet(): count(0) {
    }

    int getRandom(int element) {
        count++;
        if (count==1) {
            lastElement = element;
            return element;
        }
        else {
            // let there's 1/count probability to return current element
            srand(time(NULL));
            if (rand() % count == 1) {
                lastElement = element;
                return element;
            } else return lastElement;
        }
    }
private:
    int count;
    int lastElement;
};

int main() {
    cout << RAND_MAX << endl;
    cout << "==============" << endl;

    vector<int> input = {1, 2, 3, 4, 5, 6, 7, 8, 9};
    Problem_20190905_RandomFromHugeSet solution;
    int sz = input.size();
    for (int i=0; i<sz; i++) {
        cout << solution.getRandom(input[i]) << " out of " << (i+1) << endl;
    }
}