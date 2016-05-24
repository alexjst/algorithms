#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <fstream>
#include <numeric>
#include <algorithm>
#include <ctime>

using namespace std;


int main() {
	/* Enter your code here. Read input from STDIN. Print output to STDOUT */
	//ifstream in("d:/test.txt");
	srand((unsigned)time(NULL));
	int n, k, a;
	//in >> n >> k;
	n = rand() % (10000) + 1;
	k = rand() % 100 + 1;

	vector<int> flags(k);
	vector<int> bfflags(n);

	for (int i = 0; i<n; i++) {
		//in >> a;
		a = rand() % 1000000000 + 1;
		bfflags[i] = a;
		a = a % k;
		flags[a] += 1;
	}
	unsigned long long result = accumulate(flags.begin(), flags.end(), 0);
	result = result * (result - 1) / 2;
	cout << result << endl;
	if (flags[0] > 1)
		result -= flags[0] * (flags[0] - 1) / 2;
	cout << result << endl;
	int mid = (k+1) / 2;
	bool k_is_even = (k % 2 == 0);
	if (k_is_even && flags[mid]>1 && mid>0)
		result -= flags[mid] * (flags[mid] - 1) / 2;

	for (int i = 1; i<mid; i++) {
		result -= flags[i] * flags[k - i];
	}

	cout << result << endl;

	cout << "\nnow with brute force:" << endl;
	int bfcount = 0;
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < i; j++) {
			if ((bfflags[i] + bfflags[j]) % k != 0)
				bfcount++;
		}
	}
	cout << bfcount << endl;

	//in.close();

	//cout << ULLONG_MAX;
	if (bfcount != result)
		cout << "FAILED" << endl;
	else
		cout << "SUCCESS!" << endl;

	system("pause");

	return 0;
}
