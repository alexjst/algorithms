/*
2.2.8 Swap Nodes in Pairs
ÃèÊö
Given a linked list, swap every two adjacent nodes and return its head.
For example, Given 1->2->3->4, you should return the list as 2->1->4->3.
Your algorithm should use only constant space. You may not modify the values in the list, only nodes
itself can be changed.

*/

/*
This is a very good detail oriented excercise for manipulating pointers in a singly-linked list,
It took me numerous time and efforts to get it correct. Lessons leaned:

1. For looping, make sure I define the start state and end state for each iteration, so that the variable
states is indeed in the same pattern with each iteration.
2. Draw a graph on the pointers to make sure I understand the starting and ending state of each loop iteration.
3. We may need multiple pointer variables for convenience. Working and clean and understandable code is more
important than anything else (that may involve some trick to make the code 'elegant'). As we know, some very tricky
algorithms can be written using very elegant code, it could be very difficult to construct elegant code, so in a
tight time bound, elegancy is far less important than correct and working code.

*/

#include "SwapNodesInPairs.h"
#include <iostream>

using namespace std;

// 1. define node
struct Node {
	int data;
	Node* next;
	Node(int d) :data(d), next(nullptr) { }
};

// 2. play with pointers to swap nodes
Node* swapEveryTwoInList(Node* head)
{
	// boundary
	if (!head || !head->next)
		return head;

	Node* newHead = head->next;
	// general
	Node* p = head;
	Node* q = p->next;
	while (p && q) {
		// change q¡¯s next pointers
		Node* tmp = p->next->next;
		q->next = p;

		// now what¡¯s p¡¯s next pointer?
		if (!tmp || !tmp->next) { p->next = tmp; break; }
		p->next = tmp->next;
		p = tmp;
		q = tmp->next;
	}

	return newHead;
}


void SwapNodesInPairs::run()
{
	Node n1(1);
	Node n2(2); n1.next = &n2;
	Node n3(3);	n2.next = &n3;
	Node n4(4); n3.next = &n4;
	Node n5(5); n4.next = &n5;
	Node n6(6); n5.next = &n6;
	Node n7(7); n6.next = &n7;
	Node n8(8); n7.next = &n8;

	Node* head = swapEveryTwoInList(&n1);
	while (head) {
		cout << head->data << endl;
		head = head->next;
	}

}