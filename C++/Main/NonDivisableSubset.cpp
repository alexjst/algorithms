#include "NonDivisableSubset.h"

#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

void NonDivisableSubset::run()
{
    //int n, k, a;
    int n = 4, k = 3;

    // will be init to 0 when allocated on the stack
    vector<int> flags(k);

    int nums[4] = {1, 7, 4, 3};
    for (int i = 0; i<n; i++) {
        int a = nums[i];
        a = a % k;
        flags[a] += 1;
    }

    int result = 0;
    if (flags[0] >= 1)
        result += 1;

    for (int i = 1, j = k - 1; i <= j; i++, j--) {
        if (i == j)
            result += 1;
        else
            result += max(flags[i], flags[j]);
    }

    cout << result << endl;
}
