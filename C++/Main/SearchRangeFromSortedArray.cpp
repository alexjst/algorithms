/*
Given a sorted array of integers, find the starting and ending position of a given target value.
Your algorithm¡¯s runtime complexity must be in the order of O(log n).
If the target is not found in the array, return [-1, -1].
For example, Given [5, 7, 7, 8, 8, 10] and target value 8, return [3, 4].
*/

#include "SearchRangeFromSortedArray.h"

#include <iostream>
#include <algorithm>

using namespace std;

int findLowerBound(int* data, int len, int target)
{
}

int findUpperBound(int* data, int len, int target)
{
}

void SearchRangeFromSortedArray::run()
{
	int data[] = {1,1,2,2,3,4,5,5,5,5,6,6,7,8,9,9};
	int len = sizeof(data) / sizeof(int);

	int target = 5;
	int start = distance(data, lower_bound(data, data+len, target));
	int end = distance(data, upper_bound(data, data + len, target));

	cout << "With std::lower_bound, std::upper_bound, std::distance :" << endl;
	cout << "range = [" << start << ", " << end - 1 << "]" << endl; // supposed to be [6, 9]

	cout << "With handcrafted partition code :" << endl;
	start = findLowerBound(data, len, target);
	end = findUpperBound(data, len, target);
}