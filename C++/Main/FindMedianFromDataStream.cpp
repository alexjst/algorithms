#include "FindMedianFromDataStream.h"

#include <queue>
#include <functional>
#include <algorithm>
#include <iostream>

using namespace std;

class MedianFinder {
public:

    // Adds a number into the data structure.
    void addNum(int num) {
        int leftSize = left.size();
        int rightSize = right.size();

        if (leftSize == 0) {
            if (rightSize == 0) right.push(num);
            else {
                int rightTop = right.top();
                if (num <= rightTop) left.push(num);
                else {
                    right.pop();
                    left.push(rightTop);
                    right.push(num);
                }
            }
        }
        else {
            int leftTop = left.top();
            int rightTop = right.top();
            if (leftSize == rightSize) {
                if (leftTop <= num) right.push(num);
                else {
                    left.pop(); left.push(num); right.push(leftTop);
                }
            }
            else {
                if (num <= rightTop) left.push(num);
                else {
                    right.pop(); right.push(num); left.push(rightTop);
                }
            }
        }
    }

    // Returns the median of current data stream
    double findMedian() {
        if (left.size() == right.size()) return (left.top() + right.top()) / 2.0;
        else return (double)right.top();
    }
private:
    priority_queue<int> left;
    priority_queue<int, vector<int>, greater<int> > right;
};

void FindMedianFromDataStream::run() {
    MedianFinder inst;
    inst.addNum(2);
    inst.addNum(1);
    inst.addNum(3);
    cout << inst.findMedian() << endl;
}