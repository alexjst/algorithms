#include <iostream>

#include "LeetCodeShuffle.h" // this will generate 10 random problem to solve

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
#include "NonDivisableSubset.h"
#include "BfsShortestReach.h"
#include "StlAlgorithms.h"
#include "DijkstraShortestReach.h"
#include "mysqrt.h"
#include "SynchronousShopping.h"
#include "MergeTwoSortedList.h"
#include "NextPermutation.h"

int main()
{
    //LeetCodeShuffle algo = LeetCodeShuffle();

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
    //ParlindromePartitioning algo = ParlindromePartitioning();
    //NonDivisableSubset algo = NonDivisableSubset();
    //BfsShortestReach algo = BfsShortestReach();
    //DijkstraShortestReach algo = DijkstraShortestReach();
	//StlAlgorithms algo = StlAlgorithms();
	//mysqrt algo = mysqrt();
	//SynchronousShopping algo = SynchronousShopping();
    //MergeTwoSortedList algo = MergeTwoSortedList();
    NextPermutation algo = NextPermutation();
	algo.run();

	std::cout << std::endl;
	system("pause");
    return 0;
}