#include "SimpleExpressionEval.h"

#include <string>
#include <iostream>
#include <stack>
#include <cctype>

using namespace std;

int eval(const string& input)
{
	int len = input.length();
	stack<int> valStack;
	stack<char> opStack;

	for (int i = 0; i<len; ++i) {
		if (isdigit(input[i])) {
			// push to stack
			int val = input[i] + 1 - '1';
			valStack.push(val);
		}
		else if (input[i] == '+' || input[i] == '-' || input[i] == '*' || input[i] == '/') {
			opStack.push(input[i]);
		}
		else if (input[i] == ')') {
			int second = valStack.top(); valStack.pop();
			int first = valStack.top(); valStack.pop();            char op = opStack.top(); opStack.pop();
			int val = 0;
			switch (op) {
			case '+': val = first + second; break;
			case '-':  val = first - second; break;
			case '*':  val = first * second; break;
			case '/':  val = first / second; break;
			default:;
			}
			// push val to stack
			valStack.push(val);
		}
	}
	return valStack.top();
}

void SimpleExpressionEval::run()
{
	string input("5-(2*3)+(4/2)");

	cout << eval(input) << endl;
}
