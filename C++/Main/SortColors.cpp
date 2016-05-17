/*Given an array with n objects colored red, white or blue, sort them so that objects of the same color are
adjacent, with the colors in the order red, white and blue.
Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.
Note: You are not suppose to use the library¡¯s sort function for this problem.
Follow up:
A rather straight forward solution is a two-pass algorithm using counting sort.
First, iterate the array counting number of 0¡¯s, 1¡¯s, and 2¡¯s, then overwrite array with total number of 0¡¯s,
then 1¡¯s and followed by 2¡¯s.
Could you come up with an one-pass algorithm using only constant space?*/

#include "SortColors.h"

#include <iostream>

using namespace std;

void SortColors::run()
{
	const int len = 30;
	int odata[len] = { 0 };

	srand((unsigned)time(NULL));
	cout << "Original sequence:" << endl;
	for (int i = 0; i < len; i++) {
		odata[i] = rand()%3;
		//cout << odata[i];
	}
	cout << endl;

	// copy the data for trying different algorithms on the same data
	int data[len];
	copy(odata, odata + len, data);

	cout << "The naive implementation with two passes:" << endl;
	PerfTimer* pt = new PerfTimer();
	int count[3] = { 0 };
	for (int i = 0; i < len; i++) {
		count[data[i]]++;
	}

	for (int idx = 0, i = 0; i < 3; i++) {
		for (int j = 0; j < count[i]; j++) {
			data[idx++] = i;
			cout << i;
		}
	}
	cout << endl;
	delete pt;

	copy(odata, odata + len, data);
	cout << "Now with one pass algorithm:" << endl;
	pt = new PerfTimer();
	/*
	* the idea is: scan the sequence, if 0 is hit, swap with the first none-zero element, if 2 is hit, swap with the none-2 element from the back
	*/
	int zeros = 0; int twos = 0;
	int i = 0;
	while (i<(len - twos)) {
		if (data[i] == 0) swap(data[i++], data[zeros++]);
		else if (data[i] == 2) swap(data[i], data[len - 1 - (twos++)]);
		else /* (data[i] == 1) */ i++;
	}

	delete pt;

	for (int i = 0; i < len; i++)
		cout << data[i];
	cout << endl;
}
