#include "SearchInRotatedSortedArray_II.h"
#include <vector>
#include <iostream>

using namespace std;

// this problem is about binary search: binary search is not trivial to implement if not using the proper construct.
// the correct construct should be: 3-way compare and a while loop with 'lo', 'high' and 'mid'

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
	cout << locateFrom(input3, 5);//4
}