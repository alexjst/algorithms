/*
Given an unsorted integer array, find the first missing positive integer.
For example, Given[1, 2, 0] return 3, and[3, 4, -1, 1] return 2.
Your algorithm should run in O(n) time and uses constant space.
*/

#include "FirstMissingPositive.h"

#include <iostream>
using namespace std;

void FirstMissingPositive::run()
{
	int data[] = { 3, 4, -1, 1, 7, -3, 2, 9 }; // missing 5
	int len = sizeof(data) / sizeof(int);

    for (int i = 0; i < len; i++) {
        while (data[i] >= 1 && data[i] <= len && data[i]!=data[data[i]-1]) {
            swap(data[i], data[data[i]-1]);
        }
    }

	// now expecting [1, 2, 3, ....]
	int missing = len + 1;
	for (int i = 0; i < len; i++) {
		if (data[i] != i + 1) {
			missing = i + 1;
			break;
		}
	}

	cout << "First missing positive number = " << missing << endl;
}

