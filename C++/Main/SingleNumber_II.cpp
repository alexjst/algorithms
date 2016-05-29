/*
Given an array of integers, every element appears three times except for one. Find that single one.

Note: Your algorithm should have a linear runtime complexity. Could you implement it without using
extra memory?

*/

#include "SingleNumber_II.h"
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

void mod3(int& a, vector<int>& result)
{
    for (int i = 0; i < 32; i++) {
        result[i] = ( ((a>>i)&1) + result[i]) % 3;
    }
}

void SingleNumber_II::run()
{
    vector<int> data = { 4, 4, 5, 4, 5, 2, 5, 2, 7, 2 };

    size_t sz = data.size();

    vector<int> result(32, 0);
    for (int i = 0; i<sz; i++) {
        mod3(data[i], result);
    }
    int theOne = 0;
    for (int i = 0; i<32; i++) {
        theOne += (result[i] << i);
    }

    cout << theOne << endl;
}