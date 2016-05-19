// check if one tree is a sub-tree of another (not memory location, but contents of the tree nodes)
//
#include <iostream>
#include <vector>

using namespace std;

/*
struct Node{
    int data;
    Node* left;
    Node* right;

    Node(int d) { data = d; left = nullptr; right = nullptr; }
};

bool isIdentical(Node* t1, Node* t2)
{
    if (t1 == nullptr && t2 == nullptr)
        return true;
    if (t1 == nullptr || t2 == nullptr)
        return false;

    if (t1->data == t2->data && isIdentical(t1->left, t2->left) && isIdentical(t2->right, t2->right))
        return true;
    else
        return false;
}

bool isSubTree(Node* A, Node* B) // returns true if A is a subtree of B
{
    if (isIdentical(A, B))
        return true;
    else if (!B)
        return false;
    else if (isSubTree(A, B->left))
        return true;
    else if (isSubTree(A, B->right))
        return true;
    else
        return false;
}

int main()
{
    Node* B = new Node(1);
    Node* b1 = new Node(2);
    Node* b2 = new Node(3);
    Node* b3 = new Node(4);
    Node* b4 = new Node(5);
    B->left = b1; B->right = b2;
    b1->left = b3; b1->right = b4;

    Node* A = new Node(2);
    Node* a1 = new Node(4);
    Node* a2 = new Node(5);
    A->left = a1; A->right = a2;

    //YES
    if (isSubTree(A, B))
        cout << "YES" << endl;
    else
        cout << "NO" << endl;

    //NO
    if (isSubTree(B, A))
        cout << "YES" << endl;
    else
        cout << "NO" << endl;

    //NO
    if (isSubTree(A, nullptr))
        cout << "YES" << endl;
    else
        cout << "NO" << endl;

    //YES
    if (isSubTree(nullptr, B))
        cout << "YES" << endl;
    else
        cout << "NO" << endl;
    system("pause");
    return 0;
}
*/
int main()
{
	int data[] = {1,6,1,3,6};
	int len = sizeof(data) / sizeof(int);

	int val = 0;
	for (int i = 0; i < len; i++) {
		val ^= data[i];
	}

	cout << val << endl;

	system("pause");
	return 0;
}