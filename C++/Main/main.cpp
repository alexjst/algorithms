#include "SelectionSort.h"
#include "InsertionSort.h"
#include "MergeSort.h"
#include "BuySell.h"
#include "CountOnesFromSequence.h"
#include "SimpleExpressionEval.h"
#include "FirstMissingPositive.h"
#include "SortColors.h"
#include "SearchRangeFromSortedArray.h"
#include "Search2DMatrix.h"
#include "TreePreorderIteratively.h"
#include "ReverseLinkedList.h"
#include "ParlindromePartitioning.h"

int main()
{
    //SelectionSort algo1 = SelectionSort();
    //InsertionSort algo = InsertionSort();
    //MergeSort algo3 = MergeSort();
	//SimpleExpressionEval algo = SimpleExpressionEval();
    //FirstMissingPositive algo = FirstMissingPositive();
	//SortColors algo = SortColors();
	//SearchRangeFromSortedArray algo = SearchRangeFromSortedArray();
    //Search2DMatrix algo = Search2DMatrix();
	//TreePreorderIteratively algo = TreePreorderIteratively();
	//ReverseLinkedList algo = ReverseLinkedList();
    ParlindromePartitioning algo = ParlindromePartitioning();
    algo.run();

    system("pause");
    return 0;
}