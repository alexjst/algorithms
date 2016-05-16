#include "InsertionSort.h"

#include <iostream>
#include <ctime>

using namespace std;

void InsertionSort::run()
{
    const int len = 10;
    int data[len] = { 0 };

    srand((unsigned)time(NULL));
    for (int i = 0; i < len; i++) {
        data[i] = rand();
        // cout << data[i] << endl;
    }

    PerfTimer pt = PerfTimer();
    for (int i = 1; i < len; i++) {
        // make sure data[i] in order among data[0] to data[i-1]
        for (int j = i; j>0; --j) {
            if (data[j] < data[j - 1]) {
                int swp = data[j];
                data[j] = data[j - 1];
                data[j - 1] = swp;
			}
			else {
				break;
			}
        }
    }

    for (int i = 0; i < len; i++) {
        cout << data[i] << endl;
    }
}