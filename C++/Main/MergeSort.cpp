#include "MergeSort.h"

#include <iostream>

using namespace std;

void msort(int* data, int* aux, int low, int high)
{
    if (low >= high) return;
    if ((low + 1) == high) {
        if (data[low] > data[high]) {
            int swp = data[low];
            data[low] = data[high];
            data[high] = swp;
        }
        return;
    }

    int mid = (low + high) / 2;
    msort(data, aux, low, mid);
    msort(data, aux, mid + 1, high);

    for (int i = low; i <= high; i++) {
        aux[i] = data[i];
    }
    int j = low;
    int k = mid + 1;
    for (int i = low; i <= high; i++) {
        if (j > mid)   data[i] = aux[k++];
        else if (k > high)  data[i] = aux[j++];
        else if (aux[j] > aux[k])    data[i] = aux[k++];
        else data[i] = aux[j++];
    }

}

void MergeSort::run()
{
    const int len = 50000;
    int data[len] = { 0 };

    srand((unsigned)time(NULL));
    for (int i = 0; i < len; i++) {
        data[i] = rand();
        // cout << data[i] << endl;
    }

    PerfTimer pt = PerfTimer();
    int low = 0;
    int high = len - 1;
    int mid = (low + high) / 2;
    int* aux = new int[len];
    msort(data, aux, low, high);
    delete[] aux;

    for (int i = 0; i < len; i++) {
        //cout << data[i] << endl;
    }
}
