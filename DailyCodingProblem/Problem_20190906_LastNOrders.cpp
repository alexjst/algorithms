/**
 * This problem was asked by Twitter.

You run an e-commerce website and want to record the last N order ids in a log. Implement a data structure to accomplish this,
with the following API:

record(order_id): adds the order_id to the log
get_last(i): gets the ith last element from the log. i is guaranteed to be smaller than or equal to N.
You should be as efficient with time and space as possible.
*/

#include <iostream>
#include <vector>
#include <deque>
#include <algorithm>

using namespace std;

class LastOrders {
public:
    LastOrders(int n) {
        this->N = n;
    }

    void record(int order_id) {
        dq.push_front(order_id);
        if (dq.size() > N) {
            dq.pop_back();
        }
    }

    int get_last(int i) {
        if (i <= dq.size()) {
            return dq.at(i-1);
        } else {
            return 0;
        }
    }
private:
    int N;
    deque<int> dq;
};

int main(int argc, char* argv[]) {
    LastOrders orders(5);
    orders.record(1);
    orders.record(2);
    orders.record(3);
    orders.record(4);
    orders.record(5);
    cout << orders.get_last(3) << endl;
    orders.record(6);
    cout << orders.get_last(3) << endl;
    orders.record(7);
    cout << orders.get_last(3) << endl;
    orders.record(8);
    cout << orders.get_last(3) << endl;
    orders.record(9);
    cout << orders.get_last(3) << endl;
    orders.record(10);
    cout << orders.get_last(3) << endl;
    orders.record(11);
    cout << orders.get_last(3) << endl;

    return 0;
}

/**
 * This implementation uses c++ standard lib's deque class which is a queue and operate like
 * a linked list but can also be randomly accessed by index. So the follow up question is then:
 * How do you want to implement such a deque?
 * A: A deque is usually implemented as a vector of fixed-sized vector. So when pushing elements
 * into either end, we push those elements into the fixed-sized vector, which is constant-time.
 * Address an element from a index is also constant-time.
 */
