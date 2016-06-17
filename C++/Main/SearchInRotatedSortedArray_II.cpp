/*
Study poing: Binary Search

Binary Search uses 3-way compare as shown below:

int binary_search(vector<int> input, int target)
{
    int lo = 0, hi = input.size()-1;
    while (lo<=hi) {
        int mid = (lo+hi)/2;
        if (input[mid]<target) lo = mid+1;
        else if (input[mid]>target) hi = mid-1;
        else return mid;
    }
    return -1; // not found
}

Then, starting from Binary Search, we have a varied version called "rotated sorted array's binary search, where the given input array is sorted but roated"

*/

#include "SearchInRotatedSortedArray_II.h"
#include <vector>
#include <iostream>

using namespace std;

// this problem is about binary search: binary search is not trivial to implement if not using the proper construct.
// the correct construct should be: 3-way compare and a while loop with 'lo', 'high' and 'mid'

// input is a rotated increasing sequence where duplicates are allowed
int bsearch(const vector<int>& input, const int& target) {
	int lo = 0, hi = input.size() - 1;
	while (lo <= hi) {
		int mid = (lo + hi) / 2;
		if (target == input[mid]) return mid;

		// find out if the left sub-sequence is increasing
		if (input[lo]<input[mid]) {
			if (input[lo] <= target && target<input[mid])
				hi = mid - 1;
			else lo = mid + 1;
		}
		else if (input[lo] == input[mid]) {
			while (lo<mid && input[lo] == input[lo + 1]) lo++;
			if (lo == mid) lo = mid + 1;
			else { // not an increasing seq, some bigger value between
				hi = mid - 1;
			}
		}
		else {// input[lo]>input[mid]
			if (input[lo] <= target || target<input[mid]) hi = mid - 1;
			else lo = mid + 1;
		}
	}
	return -1; // not found 
}

int locateFrom(vector<int>& input, int target) {
	int start = 0, end = input.size() - 1;
	while (start <= end) {
		int mid = (start + end) / 2;
		if (input[mid] == target) return mid;

		if (input[start] <= input[mid]) { // left is increasing, including the case start==mid
			if (input[start] <= target && target < input[mid])
				end = mid - 1;
			else
				start = mid + 1;
		}
		else {
			if (input[mid] < target && target <= input[end])
				start = mid + 1;
			else
				end = mid - 1;
		}
	}
}



void SearchInRotatedSortedArray_II::run()
{
	vector<int> input1 = { 3, 4, 5, 6, 7, 0, 1, 2 };
	vector<int> input2 = { 1, 2, 3, 4, 5, 6, 7, 0 };
	vector<int> input3 = { 1, 2, 3, 4, 5, 6, 7, 0, 1 };
	vector<int> input4 = { 1, 2, 3, 3, 1, 1, 1, 1, 1, 1 };

	cout << locateFrom(input1, 0); //5
	cout << locateFrom(input1, 5); //2
	cout << locateFrom(input1, 2); //7
	cout << locateFrom(input1, 3); //0
	cout << locateFrom(input2, 0); //7
	cout << locateFrom(input2, 1); //0
	cout << locateFrom(input2, 6); //5
	cout << locateFrom(input3, 6); //5
	cout << locateFrom(input3, 0); //7
	cout << locateFrom(input3, 1);//0
	cout << locateFrom(input3, 3);//2
	cout << locateFrom(input3, 5) << endl;//4

	cout << bsearch(input1, 0); //5
	cout << bsearch(input1, 5); //2
	cout << bsearch(input1, 2); //7
	cout << bsearch(input1, 3); //0
	cout << bsearch(input2, 0); //7
	cout << bsearch(input2, 1); //0
	cout << bsearch(input2, 6); //5
	cout << bsearch(input3, 6); //5
	cout << bsearch(input3, 0); //7
	cout << bsearch(input3, 1); //0
	cout << bsearch(input3, 3); //2
	cout << bsearch(input3, 5) << endl;//4

	cout << bsearch(input4, 1);//any of 0,4,5,6,7,8
	cout << bsearch(input4, 2);//1
	cout << bsearch(input4, 3);//2
	cout << bsearch(input4, 4) << endl;// -1
}