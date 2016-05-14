#include "SelectionSort.h"
#include "InsertionSort.h"
#include "MergeSort.h"

int main()
{
    SelectionSort algo1 = SelectionSort();
    InsertionSort algo2 = InsertionSort();
    MergeSort algo3 = MergeSort();
    algo1.run();
    algo2.run();
    algo3.run();

    system("pause");
    return 0;
}