#include "CountOnesFromSequence.h"

#include <cmath>
#include <iostream>

using namespace std;

int ones(int n, bool cache = false)
{
	const int givenN = n;

	if (n < 1)
		return 0;
	else if (n < 10)
		return 1;

	// calculate how many digits is in n's demical representation
	int decimalLen = 0;

	while (n >= 10) {
		n = int(n / 10);
		++decimalLen;
	}

	++decimalLen;
	int firstDigit = n;

	// use cache is available
	static int cachedVals[9] = { 0 };
	if (cache) {
		if (cachedVals[decimalLen - 1] != 0) {
			cout << "Using cached value!" << endl;
			return cachedVals[decimalLen - 1];
		}
	}


	int total = 0;

	// calculate power 
	int tenToThePowerofLen = 1;
	for (int i = 0; i < (decimalLen - 1); ++i)
		tenToThePowerofLen *= 10;

	int remainder = givenN - firstDigit*tenToThePowerofLen;
	if (firstDigit == 1)
		total = ones(tenToThePowerofLen - 1, true) + (remainder + 1) + ones(remainder);
	else {
		total = ones(tenToThePowerofLen - 1, true) * firstDigit + tenToThePowerofLen + ones(remainder);
	}

	if (cache)
		cachedVals[decimalLen - 1] = total;

	return total;
}

void CountOnesFromSequence::run()
{
	cout << ones(1) << endl; // should be 1
	cout << ones(11) << endl; // should be 4
	cout << ones(12) << endl; // should be 5
	cout << ones(22) << endl; // should be 13
	cout << ones(1073741825) << endl; // should be fast...
}