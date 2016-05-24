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
	ifstream in("d:/test.txt");
	int n, k, a;
	in >> n >> k;

	vector<int> flags(k);

	for (int i = 0; i<n; i++) {
		in >> a;
		a = a % k;
		flags[a] += 1;
	}

	int result = 0;
	if (flags[0] > 1)
		result += 1;

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
