#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <fstream>
#include <algorithm>

using namespace std;

int main() {
	/* Enter your code here. Read input from STDIN. Print output to STDOUT */
	ifstream in("d:/test.txt");
	int n, k, a;
	in >> n >> k;

    // will be init to 0 when allocated on the stack
	vector<int> flags(k);

	for (int i = 0; i<n; i++) {
		in >> a;
		a = a % k;
		flags[a] += 1;
	}

	int result = 0;
	if (flags[0] >= 1)
		result += 1;

	for (int i = 1, j=k-1; i<=j; i++, j--) {
        if (i == j)
            result += 1;
        else
            result += max(flags[i], flags[j]);
	}

	cout << result << endl;

	in.close();

	system("pause");

	return 0;
}
