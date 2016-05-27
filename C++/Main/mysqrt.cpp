/*

y = x*x;
y/x = x;
x = (x+y/x)2

*/
#include "mysqrt.h"

#include <iostream>
using namespace std;

double doSqrt(double input)
{
	if (input <= 0)
		return doSqrt(-input);
	double x = 1.0;
	while (abs(input / x - x) > 0.001) {
		x = (x + input / x) / 2.0;
	}
	return x;
}

void mysqrt::run()
{
	double input = 9000;
	cout << "mysqrt of " << input << " is " << doSqrt(input);

	// LeetCode's solution, which I currently do not understand
	/*
	int x = input;
	int left = 1, right = x / 2;
	int last_mid; // 记录最近一次mid
	if (x < 2) {
		cout << x << endl;
		return;
	}
	while (left <= right) {
		const int mid = left + (right - left) / 2;
		if (x / mid > mid) { // 不要用x > mid * mid，会溢出
			left = mid + 1;
			last_mid = mid;
		}
		else if (x / mid < mid) {
			right = mid - 1;
		}
		else {
			cout << mid << endl;
			return;
		}
	}
	cout << "\nLeetCode memo sample returns: " <<  last_mid << endl;
	*/
}