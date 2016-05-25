/*
This is a thorough review of CPP STL <algorithm> methods that we can use for convenience.
It is important to remember and reheasal well on these basic algorithms so that when we
need to use them we can just pick up the right tool for the job, instead of re-inventing
the wheels in pain!
*/
#include "StlAlgorithms.h"

#include <iostream>
#include <vector>
#include <list>
#include <queue>
#include <algorithm>

using namespace std;

void StlAlgorithms::run()
{
	/*
	Many stl algorithms use predicate.
	A unary predicate returns a boolean value, which itself can be a function pointer, function object or lambda

	*/
	/* part 1: Non-modifying sequence operations:*/
	
	// "std::all_of" - returns true if all elements in a range returns true on the predicate
	vector<int> data1 = { 0, 2, 8, 4, 52 };
	if (all_of(data1.begin(), data1.end(), [](int i) {return i % 2 == 0; }))
		cout << "all are even" << endl;
	else
		cout << "not all are even" << endl;

	// "std::any_of" - returns true if any element in a range returns true on the predicate
	vector<int> data2 = { 0, 2, 36, 6, 10 };
	if (any_of(data2.begin(), data2.end(), [](int i) {return i % 2 == 1; }))
		cout << "some element are odd" << endl;
	else
		cout << "all are not odd" << endl;

	// "std::any_of" - returns true if any element in a range returns true on the predicate
	vector<int> data3 = { 0, 2, 36, 6, 10 };
	if (none_of(data3.begin(), data3.end(), [](int i) {return i == 36; }))
		cout << "none is 36" << endl;
	else
		cout << "data contains 36" << endl;

	// for_each - run a lambda on a range
	char sep = ',';
	for_each(data3.begin(), data3.end(), [&sep](int i) { cout << i << sep; });

	// find - returns the iterator when finding a value in range. we can use std::distance to return its index
	cout << "\n36 is at index: " << distance(data3.begin(), find(data3.begin(), data3.end(), 36)) << endl;

	// find_if - returns the first matching iterator in a range, when giving a range and a predicate
	cout << "the first positive number divisable by 9 is at index: " << distance(data3.begin(), find_if(data3.begin(), data3.end(), [](int d){return d>0 && d % 9 == 0; })) << endl;

	// find_if_not returns the first non-maching iterator in a range, when giving a range and a predicate
	cout << "the first odd number's index is: " << distance(data3.begin(), find_if_not(data3.begin(), data3.end(), [](int i) {return i % 2 == 0; }));
	
	//adjacent_find
	vector<int> data4 = { 0, 2, 36, 6, 6 };
	cout << "the first adjacent member appears at index " << distance(data4.begin(), adjacent_find(data4.begin(), data4.end()));

	//count
	cout << "the appearances of 6 is " << count(data4.begin(), data4.end(), 6);

	//count_if
	cout << "the number of elemens that are greater than 10 are " << count_if(data4.begin(), data4.end(), [](int i){ return i > 10;  });

	//search
}