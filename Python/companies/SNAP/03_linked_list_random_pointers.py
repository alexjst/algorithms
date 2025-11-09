#!/usr/bin/env python3
"""
Problem 3: Copy List with Random Pointers

SNAP frequently asks this problem for implementing complex data structures.
Clone a linked list where each node has a random pointer to another node.

Requirements:
- Deep copy of linked list with next and random pointers
- O(n) time complexity
- Handle cycles and null pointers

Example:
    # List: 1->2->3
    # Random: 1->3, 2->1, 3->2
    original = create_list()
    copier = LinkedListCopier()
    copied = copier.copy_with_random(original)
    # copied is independent deep copy

Time Complexity: O(n)
Space Complexity: O(n)
"""

try:
    import importlib.util
    spec = importlib.util.spec_from_file_location("solution_module",
                                                   "03_linked_list_random_pointers_solution.py")
    solution_module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(solution_module)
    Node = solution_module.Node
    LinkedListCopier = solution_module.LinkedListCopier
except Exception as e:
    print(f"❌ Error importing solution: {e}")
    exit(1)

def test_list_copier():
    print("Testing Linked List with Random Pointers...")
    print()

    # Test 1: Simple list
    print("Test 1: Simple 3-node list")
    node1, node2, node3 = Node(1), Node(2), Node(3)
    node1.next, node2.next = node2, node3
    node1.random, node2.random, node3.random = node3, node1, node2
    
    copier = LinkedListCopier()
    copied = copier.copy_with_random(node1)
    
    assert copied.val == 1, "Test 1 failed: wrong value"
    assert copied is not node1, "Test 1 failed: not a deep copy"
    assert copied.random.val == 3, "Test 1 failed: wrong random pointer"
    print("✓ Test 1 passed")
    print()

    # Test 2: Empty list
    print("Test 2: Empty list")
    result = copier.copy_with_random(None)
    assert result is None, "Test 2 failed"
    print("✓ Test 2 passed")
    print()

    print("All tests passed! ✓")

if __name__ == "__main__":
    test_list_copier()
