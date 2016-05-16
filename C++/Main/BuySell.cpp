#include "BuySell.h"

#include <iostream>

using namespace std;

void BuySell::run()
{
	int data[] = { 7, -2, 6, 0, 2, 9, 2, -4, 8, 11, 7, 3 };
	//int data[] = { 15, 12, 10, 8, 2, -4, -13 };
	int len = sizeof(data) / sizeof(int);

	int buy = 0;
	int sell = 0;

	// TODO: write your code here:

	// backward differe
	//int* odata = new int[len-1];
	//for(int i = 0; i < len-1; i++)
	//    odata[i] = data[i+1] - data[i];

	// find maxSum and  locations
	int maxSum = INT_MIN;
	int sum = 0;
	int curstart = 0;
	for (int i = 0; i < len - 1; ++i)
	{
		if (sum < 0)
		{
			//sum = odata[i];
			sum = data[i + 1] - data[i];
			curstart = i;
		}
		else
		{
			//sum += odata[i];
			sum += data[i + 1] - data[i];
		}
		if (sum > maxSum)
		{
			maxSum = sum;
			buy = curstart;
			sell = i;
		}
	}
	sell++;


	cout << "Best buying time (index) = " << buy << endl;
	cout << "Best selling(index) = " << sell << endl;
	cout << "Largest gain = " << data[sell] - data[buy] << endl;
}
