/*
Write an efficient algorithm that searches for a value in an m*n matrix. This matrix has the following
properties:
• Integers in each row are sorted from left to right.
• The first integer of each row is greater than the last integer of the previous row.
For example, Consider the following matrix:
[
[1, 3, 5, 7],
[10, 11, 16, 20],
[23, 30, 34, 50]
]
Given target = 3, return true.
*/
#include "Search2DMatrix.h"
#include <vector>
#include <algorithm>
#include <iostream>
using namespace std;

bool findInMatrix(vector<const vector<int> >& data, const int m, const int n, int target)
{
    vector<int> colvec;
    for (int i = 0; i < m;i++)
        colvec.push_back(data[i][0]);
    int row = distance(colvec.begin(), lower_bound(colvec.begin(), colvec.end(), target));
    if (colvec[row] > target) --row;
    int col = distance(data[row].begin(), lower_bound(data[row].begin(),data[row].end(), target));
    if (data[row][col] == target)
        return true;
    else
        return false;
}

void Search2DMatrix::run()
{
    vector<const vector<int>> data = { { 1, 3, 5, 7 }, { 10, 11, 16, 20 }, {23,30,34,50} };
    int target = 3;
    if (findInMatrix(data, 3, 4, target))
        cout << "found" << endl;
    else
        cout << "NOT found" << endl;
}