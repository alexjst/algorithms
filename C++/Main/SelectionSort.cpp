#include "SelectionSort.h"

#include <iostream>
#include <ctime>

using namespace std;

SelectionSort::SelectionSort()
{
}

SelectionSort::~SelectionSort()
{
}

void SelectionSort::run()
{
    const int len = 50000;
    int data[len] = { 0 };

    srand((unsigned)time(NULL));
    for (int i = 0; i < len; i++) {
        data[i] = rand();
        // cout << data[i] << endl;
    }

    PerfTimer pt = PerfTimer();
    for (int i = 0; i < len; i++) {
        int theMin = INT_MAX;
        int theMinIdx = i;
        for (int j = i; j < len; j++) {
            // select the smallest element and put it to result array
            if (theMin > data[j]) {
                theMin = data[j];
                theMinIdx = j;
            }
        }
        // swap data[i] and data[theMinIdx];
        if (i != theMinIdx && data[i] != data[theMinIdx]) {
            int tmp = data[i];
            data[i] = data[theMinIdx];
            data[theMinIdx] = tmp;
        }
    }

    for (int i = 0; i < len; i++) {
        //cout << data[i] << endl;
    }
}