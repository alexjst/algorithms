#include "ReverseLinkedList.h"

#include <iostream>
#include <stack>

using namespace std;

class node {
public:
	node(int d) { data = d; next = nullptr; }

	int data;
	node* next;
};

node* reverse_with_stack(node* head)
{
	if (!head) return nullptr;

	stack<node*> mystack;
	mystack.push(nullptr);
	node* p = head;
	while (p) {
		mystack.push(p); p = p->next;
	}

	node* newHead = mystack.top();
	mystack.pop();
	p = newHead;
	while (!mystack.empty()) {
		node* n = mystack.top();
		mystack.pop();
		p->next = n; p = n;
	}
	return newHead;
}

void ReverseLinkedList::run()
{
		node a(1), b(2), c(3);
		a.next = &b; b.next = &c;

		node* newhead = reverse_with_stack(&a);
		node* p = newhead;
		while (p != nullptr) {
			cout << p->data << endl;
			p = p->next;
		}
}
