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

// this is actually binary search
int findLowerBound(int* data, int len, int target)
{
    int idx = -1;
    int low = 0, high = len - 1;
    if (low > high) return -1;
    if (target < data[low]) return -1;
    if (target == data[low]) return 0;
    if (target > data[high]) return high;
    while (data[low] < target && data[high] >= target && (high - low) > 1) {
        int mid = (low + high) / 2;
        if (data[mid] < target)
            low = mid;
        else
            high = mid;
    }
    if (data[high] == target)
        return high;
    else
        return low;
}

int findUpperBound(int* data, int len, int target)
{
    int idx = -1;
    int low = 0, high = len - 1;
    if (low > high) return -1;
    if (target > data[high]) return len;
    if (target == data[high]) return high;
    if (target < data[low]) return 0;
    while (data[low] <= target && data[high] > target && (high - low) > 1) {
        int mid = (low + high) / 2;
        if (data[mid] <= target)
            low = mid;
        else
            high = mid;
    }
    return high;
}

void SearchRangeFromSortedArray::run()
{
	int data[] = {1,1,2,2,3,4,5,5,5,5,6,6,7,8,9,9};
	int len = sizeof(data) / sizeof(int);

	int target = 5;
	int start = distance(data, lower_bound(data, data+len, target));
	int end = distance(data, upper_bound(data, data + len, target));

	cout << "Method 1: with std::lower_bound, std::upper_bound, std::distance :" << endl;
	cout << "range = [" << start << ", " << end - 1 << "]" << endl; // supposed to be [6, 9]

	cout << "Method 2: with handcrafted partition code :" << endl;
	start = findLowerBound(data, len, target);
	end = findUpperBound(data, len, target);
    cout << "range = [" << start << ", " << end-1 << "]" << endl; // supposed to be [6, 9]
}