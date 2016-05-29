#include "NextPermutation.h"

#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

void doNextPermutation(vector<int>& data)
{
    // Three steps below
    // 1 - Find the rightmost guy that's strickly less than its right guy, say A & B
    // 2 - Find the rightmost guy C that's greater than the guy we just found in step 1 (A), swap A & C
    // 3 - Reverse from B till end
    size_t sz = data.size();
    if (sz != 0 & sz != 1) {
        int A = -1, B = -1, C = -1;
        for (int i = sz - 2; i >= 0; i--) {
            if (data[i] < data[i + 1]) {
                A = i;
                break;
            }
        }

        if (A >= 0) {
            B = A + 1;
            // look for C
            for (int i = sz - 1; i > A; i--) {
                if (data[i] > data[A]) {
                    C = i;
                    break;
                }
            }
            swap(data[A], data[C]);
            reverse(data.begin() + B, data.end());
        }
        else {
            reverse(data.begin(), data.end());
        }
    }
}

void NextPermutation::run()
{
    vector<int> data = {1, 1, 5};
    // next_permutation(data.begin(), data.end()); // this is for studying STL's code, very interesting logic here to learn
    doNextPermutation(data);
    for_each(data.begin(), data.end(), [](int i){ cout << i << endl; });
}
