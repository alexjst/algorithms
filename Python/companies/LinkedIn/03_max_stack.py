"""
Problem 3: Max Stack (Easy/Medium)

**LinkedIn-Tagged Premium Problem - Design Pattern**

Design a max stack data structure that supports the stack operations and supports finding
the stack's maximum element.

Implement the MaxStack class:
- MaxStack() Initializes the stack object.
- void push(int x) Pushes element x onto the stack.
- int pop() Removes the element on top of the stack and returns it.
- int top() Gets the element on the top of the stack without removing it.
- int peekMax() Retrieves the maximum element in the stack without removing it.
- int popMax() Retrieves the maximum element in the stack and removes it.
  If there is more than one maximum element, only remove the top-most one.

Example:
Input:
["MaxStack", "push", "push", "push", "top", "popMax", "top", "peekMax", "pop", "top"]
[[], [5], [1], [5], [], [], [], [], [], []]

Output:
[null, null, null, null, 5, 5, 1, 5, 1, 5]

Explanation:
MaxStack stk = new MaxStack();
stk.push(5);   // [5] - max is 5
stk.push(1);   // [5, 1] - max is 5
stk.push(5);   // [5, 1, 5] - max is 5
stk.top();     // return 5 - [5, 1, 5] - stack did not change
stk.popMax();  // return 5 - [5, 1] - pop the top-most max (second 5)
stk.top();     // return 1 - [5, 1]
stk.peekMax(); // return 5 - [5, 1]
stk.pop();     // return 1 - [5]
stk.top();     // return 5 - [5]

Constraints:
- -10^7 <= x <= 10^7
- At most 10^4 calls will be made to push, pop, top, peekMax, and popMax.
- There will be at least one element in the stack when pop, top, peekMax, or popMax is called.

Approaches:
1. Two Stacks: One for values, one for tracking max (simpler, but popMax is O(n))
2. Stack + TreeMap/Heap: For O(log n) popMax

Time Complexity:
- Approach 1: push O(1), pop O(1), top O(1), peekMax O(1), popMax O(n)
- Approach 2: push O(log n), pop O(log n), top O(1), peekMax O(1), popMax O(log n)

Implement your solution in 03_max_stack_solution.py
"""

# Import the solution
try:
    from importlib import import_module
    solution = import_module('03_max_stack_solution')
    MaxStack = solution.MaxStack
except (ImportError, AttributeError):
    class MaxStack:
        def __init__(self):
            raise NotImplementedError("Implement MaxStack in 03_max_stack_solution.py")


def test_max_stack():
    print("Testing Max Stack...\n")

    # Test 1: Basic operations
    print("Test 1: Basic operations from example")
    stk = MaxStack()
    stk.push(5)
    stk.push(1)
    stk.push(5)
    assert stk.top() == 5, "Test 1a failed"
    assert stk.popMax() == 5, "Test 1b failed"
    assert stk.top() == 1, "Test 1c failed"
    assert stk.peekMax() == 5, "Test 1d failed"
    assert stk.pop() == 1, "Test 1e failed"
    assert stk.top() == 5, "Test 1f failed"
    print("✓ Test 1 passed\n")

    # Test 2: Multiple same max values
    print("Test 2: Multiple same max values")
    stk2 = MaxStack()
    stk2.push(5)
    stk2.push(5)
    stk2.push(5)
    assert stk2.peekMax() == 5, "Test 2a failed"
    assert stk2.popMax() == 5, "Test 2b failed"  # Remove top-most
    assert stk2.peekMax() == 5, "Test 2c failed"  # Still have 5s
    print("✓ Test 2 passed\n")

    # Test 3: Negative numbers
    print("Test 3: Negative numbers")
    stk3 = MaxStack()
    stk3.push(-1)
    stk3.push(-2)
    stk3.push(-3)
    assert stk3.peekMax() == -1, "Test 3a failed"
    assert stk3.top() == -3, "Test 3b failed"
    print("✓ Test 3 passed\n")

    # Test 4: Pop and popMax interaction
    print("Test 4: Pop and popMax interaction")
    stk4 = MaxStack()
    stk4.push(1)
    stk4.push(2)
    stk4.push(3)
    assert stk4.popMax() == 3, "Test 4a failed"
    assert stk4.peekMax() == 2, "Test 4b failed"
    assert stk4.pop() == 2, "Test 4c failed"
    assert stk4.top() == 1, "Test 4d failed"
    print("✓ Test 4 passed\n")

    # Test 5: Single element
    print("Test 5: Single element")
    stk5 = MaxStack()
    stk5.push(100)
    assert stk5.peekMax() == 100, "Test 5a failed"
    assert stk5.top() == 100, "Test 5b failed"
    assert stk5.popMax() == 100, "Test 5c failed"
    print("✓ Test 5 passed\n")

    print("All tests passed! ✓")


if __name__ == "__main__":
    test_max_stack()
