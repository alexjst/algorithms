/*
2.2.13 Reorder List
ÃèÊö
Given a singly linked list L : L0 -> L1 -> ......  -> Ln-1  -> Ln, reorder it to : L0 -> Ln -> L1 ->
Ln-1 -> L2 -> Ln-2 -> ......
You must do this in - place without altering the nodes¡¯ values.
For example, Given{ 1, 2, 3, 4 }, reorder it to{ 1, 4, 2, 3 }.
*/

#include "ReorderList.h"
#include <iostream>
#include <vector>

using namespace std;

struct Node
{
    int data;
    Node* next;
    Node(int d) :data(d), next(nullptr) {}
};

// manipulating the pointers seems too hard, I'll just use an auxiliary array
void reorderList(Node* head)
{
    // boundary
    if (!head || !head->next) return;

    // 1. create a vector of 'Node*' of the same length
    vector<Node*> aux;
    Node* p = head;
    while (p) { aux.push_back(p); p = p->next; }

    // 2. rearrange the array into a another array
    vector<Node*> aux2;
    size_t len = aux.size();
    for (int i = 0, j = len - 1; i <= j; i++, j--) {
        if (i<j) { aux2.push_back(aux[i]); aux2.push_back(aux[j]); }
        else { aux2.push_back(aux[i]); }
    }

    // 3. rearrange the list accordingly
    for (int i = 0; i<len; i++) {
        if (i == len - 1) aux2[i]->next = nullptr;
        else {
            aux2[i]->next = aux2[i + 1];
        }
    }
}



void ReorderList::run()
{
    Node n1(1);
    Node n2(2); n1.next = &n2;
    Node n3(3); n2.next = &n3;
    Node n4(4); n3.next = &n4;
    Node n5(5); n4.next = &n5;
    Node n6(6); n5.next = &n6;
    Node n7(7); n6.next = &n7;
    Node n8(8); n7.next = &n8;
    Node n9(9); n8.next = &n9;

    Node* head = &n1;
    reorderList(head);
    Node* p = head;
    while (p) { cout << p->data << endl; p = p->next; }
}