// This is a C++ playground I use when watching a youtube video regarding a C++ competiative programmer from India talking about STL

#include <iostream>
#include <vector>
#include <list>
#include <set>
#include <map>
#include <functional>
#include <numeric>
#include <algorithm>

using namespace std;

bool f (int x, int y) {
    return x > y;
}

void vectorDemo() {
    // C++ STL

    vector<int> A = {11, 2, 3, 14};

    cout << A[1] << endl;

    sort(A.begin(), A.end());

    // binary search in O(logN)
    bool present = binary_search(A.begin(), A.end(), 3);
    cout << present << endl;
    present = binary_search(A.begin(), A.end(), 4);
    cout << present << endl;

    A.push_back(100);
    present = binary_search(A.begin(), A.end(), 100);

    A.push_back(100);
    A.push_back(100);
    A.push_back(100);
    A.push_back(100);
    A.push_back(100);
    A.push_back(123);

    // lower_bound returns iterator pointing to first element >= value, or we can define our own comp function
    // upper_bound returns iterator pointing to first element > value, or we can define our own comp function
    // both lower_bound and upper_bound use binary search so the time taken is log(N), super!
    // important: the elements should ALREAYD be sorted to make them work.
    auto it = lower_bound(A.begin(), A.end(), 100);
    vector<int>::iterator it2 =
        upper_bound(A.begin(), A.end(), 100);
    cout << *it << " " << *it2 << endl;

    // so this is the count number of the selected element
    cout << "Number of 100 occurances: " << it2 - it << endl;

    // sort(A.begin(), A.end(), f);
    sort(A.begin(), A.end(), [] (int& l, int& r){ return l<r;});
    for (auto& x : A) {
        x++;
        cout << x << endl;
    }

    for (auto& x : A) {
        cout << x << endl;
    }
}

void setDemo() {
    set<int> S;
    S.insert(1);
    S.insert(2);
    S.insert(-1);
    S.insert(-10);

    for (auto x : S) {
        cout << x << endl;
    }

    auto it = S.find(-1);
    if (it == S.end()) {
        cout << "Not found" << endl;
    } else {
        cout << "Found" << endl;
        cout << *it << endl;
    }

    auto it2 = S.upper_bound(-1);
    auto it3 = S.upper_bound(0);
    cout << *it2 << " " << *it3 << endl;

    auto it4 = S.upper_bound(2);
    if (it4 == S.end()) {
        cout << "cannot find it" << endl;
    }
}

void mapDemo() {
    map<int, int> A;
    A[1] = 100;
    A[2] = -1;
    A[3] = 200;
    A[10000232] = 1;

    map<char, int> cnt;
    string x = "rachit jain";

    for (char c : x) {
        cnt[c]++;
    }

    cout << cnt['a'] << " " << cnt['z'] << endl;
}

void PowerOfStl() {
    // [x, y]
    // add [2,3], [10,20], [30, 400], give me the interval that contains 13
    set<pair<int, int>> S;
    S.insert({401, 450});
    S.insert({10, 20});
    S.insert({2, 3});
    S.insert({30, 400});
    
    int point = 50;

    auto it = S.upper_bound({point, INT_MAX});
    if (it == S.begin()) {
        cout << "nope" << endl;
        return; 
    }
    --it;
    pair<int, int> current = *it;
    if (current.first <= point && point <= current.second) {
        cout << "yes its present: " << current.first << " " << current.second << endl;
    } else {
        cout << "The given point is not found" << endl;
    }
}

int main(int argc, char* argv[]) {
    PowerOfStl();
}
