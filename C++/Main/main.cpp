#include "SelectionSort.h"
#include "InsertionSort.h"
#include "MergeSort.h"
#include "BuySell.h"
#include "CountOnesFromSequence.h"
#include "SimpleExpressionEval.h"
#include "FirstMissingPositive.h"

int main()
{
    //SelectionSort algo1 = SelectionSort();
    //InsertionSort algo = InsertionSort();
    //MergeSort algo3 = MergeSort();
	//SimpleExpressionEval algo = SimpleExpressionEval();
    FirstMissingPositive algo = FirstMissingPositive();
    algo.run();

    system("pause");
    return 0;
}