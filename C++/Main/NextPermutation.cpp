#include "NextPermutation.h"

#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

void NextPermutation::run()
{
    vector<int> data = {4, 6, 5, 3, 2, 1};
    next_permutation(data.begin(), data.end());

}