"""
Solution for Max Stack

Implement your solution below.
"""

class MaxStack:
    """
    Design a max stack that supports push, pop, top, peekMax, and popMax operations.

    Approach 1 (Simpler): Two Stacks
    - stack: stores all values
    - max_stack: tracks maximum at each position
    - popMax requires O(n) to rebuild stack

    Approach 2 (Optimal): Stack + Ordered Data Structure
    - Use stack for LIFO operations
    - Use TreeMap/SortedList for tracking max values
    - All operations O(log n) or better

    Implement Approach 1 for simplicity unless asked for optimal solution.
    """

    def __init__(self):
        """
        Initialize your data structure here.
        """
        # TODO: Initialize your data structures
        # Hint for Approach 1:
        # self.stack = []  # Main stack
        # self.max_stack = []  # Track max at each position
        raise NotImplementedError("Implement __init__")

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        # TODO: Implement push
        # Hint: Push to main stack, and push max(x, current_max) to max_stack
        raise NotImplementedError("Implement push")

    def pop(self) -> int:
        """
        Remove the element on top of the stack and return it.
        """
        # TODO: Implement pop
        # Hint: Pop from both stacks and return main stack value
        raise NotImplementedError("Implement pop")

    def top(self) -> int:
        """
        Get the element on top of the stack.
        """
        # TODO: Implement top
        # Hint: Return last element of main stack without removing
        raise NotImplementedError("Implement top")

    def peekMax(self) -> int:
        """
        Retrieve the maximum element in the stack.
        """
        # TODO: Implement peekMax
        # Hint: Return last element of max_stack
        raise NotImplementedError("Implement peekMax")

    def popMax(self) -> int:
        """
        Retrieve the maximum element in the stack and remove it.
        If there is more than one maximum, remove the top-most one.
        """
        # TODO: Implement popMax
        # Hint:
        # 1. Find the maximum value (from max_stack)
        # 2. Use a temporary stack to pop elements until you find the max
        # 3. Remove the max
        # 4. Push back the temporary elements
        # 5. Rebuild max_stack accordingly
        raise NotImplementedError("Implement popMax")
