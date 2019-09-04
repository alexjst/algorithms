/*
This problem was asked by Google.

An XOR linked list is a more memory efficient doubly linked list.
Instead of each node holding next and prev fields, it holds a field named both,
which is an XOR of the next node and the previous node. Implement an XOR linked list;
it has an add(element) which adds the element to the end, and a get(index)
which returns the node at index.

If using a language that has no pointers (such as Python), you can assume you
have access to get_pointer and dereference_pointer functions that converts
between nodes and memory addresses.
*/

class XorNode {
    int val;
    XorNode* both;
public:
    XorNode(int value) {
        this->val = value;
        this->both = nullptr;
    }
};

class XorLinkedList {
private:
    XorNode* prev = nullptr;
    XorNode* curr = nullptr;
    XorNode* next = nullptr;
public:
    void add(XorNode* node) {

    }

    XorNode* get(int idx) {
        return nullptr;
    }
};

int main(int argc, char* argv[]) {
    XorNode * n1 = new XorNode(1);
    XorNode * n2 = new XorNode(2);
    XorNode * n3 = new XorNode(3);
    XorNode * n4 = new XorNode(4);
    XorNode * n5 = new XorNode(5);

    return 0;
}
