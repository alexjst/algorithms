#include "MergeTwoSortedList.h"

#include <iostream>
#include <algorithm>

using namespace std;

struct Node {
    int data;
    Node* next;
    Node(int d) { data = d; next = nullptr; }
};

Node* mergeSortedList(Node* la, Node* lb)
{
    Node* dummy = new Node(0); // so I can add nodes to it
    Node* ptr = dummy;
    while (la || lb) {
        if (!la || (lb && la->data > lb->data)) swap(la, lb);
        ptr->next = new Node(la->data);
        la = la->next;
        ptr = ptr->next;
    }
    Node* result = dummy->next;
    dummy->next = nullptr; delete dummy;
    return result;
}

void MergeTwoSortedList::run()
{
    Node* la1 = new Node(1);
    Node* la2 = new Node(2); la1->next = la2;
    Node* la3 = new Node(3); la2->next = la3;

    Node* lb1 = new Node(2);
    Node* lb2 = new Node(3);  lb1->next = lb2;
    Node* lb3 = new Node(4);  lb2->next = lb3;

    Node* head = mergeSortedList(la1, 0);
    while (head) {
        cout << head->data << ",";
        head = head->next;
    }

    cout << endl;
    
    head = mergeSortedList(0, lb1);
    while (head) {
        cout << head->data << ",";
        head = head->next;
    }

    cout << endl;

    head = mergeSortedList(la1, lb1);
    while (head) {
        cout << head->data << ",";
        head = head->next;
    }

    cout << endl;
}