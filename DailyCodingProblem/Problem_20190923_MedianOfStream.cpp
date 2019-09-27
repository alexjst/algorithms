/**
 * This problem was asked by Microsoft.

Compute the running median of a sequence of numbers. That is, given a stream of numbers, print out the median of the list so far on each new element.

Recall that the median of an even-numbered list is the average of the two middle numbers.

For example, given the sequence [2, 1, 5, 7, 2, 0, 5], your algorithm should print out:

2
1.5
2
3.5
2
2
2

*/

/*
Keep 2 priority queues. One is a max heap for lower half of the stream. One is a min heap for the upper half of stream.
*/

#include <iostream>
#include <queue>

using namespace std;

class StreamMedian{
public:
    void add(int element) {
        int lowerCount = maxHeap.size();
        int higherCount = minHeap.size();
        if (lowerCount==0 && higherCount==0) maxHeap.push(element);
        else if (lowerCount > higherCount) {
            if (element >= maxHeap.top()) minHeap.push(element);
            else {
                minHeap.push(maxHeap.top());
                maxHeap.pop();
                maxHeap.push(element);
            }
        } else {// lowerCount==higherCount
            if (element > maxHeap.top()) {
                minHeap.push(element);
                maxHeap.push(minHeap.top());
                minHeap.pop();
            } else {
                maxHeap.push(element);
            }
        }
    }
    double getMedian() {
        int lowerCount = maxHeap.size();
        int higherCount = minHeap.size();
        if (lowerCount==0 && higherCount==0) return 0; // should be an error
        else if (lowerCount > higherCount) return maxHeap.top();
        else return (maxHeap.top() + minHeap.top()) / 2.0;
    }
private:
    priority_queue<int, vector<int>, less<int>> maxHeap;
    priority_queue<int, vector<int>, greater<int>> minHeap;
};

int main(int argc, char* argv[]) {
    StreamMedian inst;
    inst.add(2);
    cout << inst.getMedian() << endl;
    inst.add(1);
    cout << inst.getMedian() << endl;
    inst.add(5);
    cout << inst.getMedian() << endl;
    inst.add(7);
    cout << inst.getMedian() << endl;
    inst.add(2);
    cout << inst.getMedian() << endl;
    inst.add(0);
    cout << inst.getMedian() << endl;
    inst.add(5);
    cout << inst.getMedian() << endl;
}

/**
 * Insertion efficiency: log(n) - 
 * Get median efficiency: O(1) - constant
 */