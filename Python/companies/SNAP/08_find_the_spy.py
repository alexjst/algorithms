#!/usr/bin/env python3
"""
Problem 8: Find the Spy

SNAP asks this graph problem for organizational trust relationships.
Similar to LeetCode 277 "Find the Celebrity" - find person accused by majority.

Requirements:
- Process trust relationships in O(n) time
- Find person accused by everyone else
- Return -1 if no spy exists
- Handle edge cases (cycles, no majority)

Example:
    n = 3
    trust = [[1, 3], [2, 3]]
    # Person 3 is accused by both 1 and 2
    # Result: 3

    n = 3
    trust = [[1, 3], [2, 3], [3, 1]]
    # No one is accused by everyone (3 accuses 1)
    # Result: -1

Time Complexity: O(n) for optimal solution
Space Complexity: O(n)
"""

try:
    import importlib.util
    spec = importlib.util.spec_from_file_location("solution_module",
                                                   "08_find_the_spy_solution.py")
    solution_module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(solution_module)
    Solution = solution_module.Solution
except Exception as e:
    print(f"❌ Error importing solution: {e}")
    exit(1)

def test_find_spy():
    print("Testing Find the Spy...")
    print()

    solution = Solution()

    # Test 1: Basic spy case
    print("Test 1: Basic spy identification")
    result1 = solution.findSpy(3, [[1, 3], [2, 3]])
    assert result1 == 3, f"Test 1 failed: expected 3, got {result1}"
    print("✓ Test 1 passed")
    print()

    # Test 2: No spy (cycle)
    print("Test 2: No spy exists (cycle)")
    result2 = solution.findSpy(3, [[1, 3], [2, 3], [3, 1]])
    assert result2 == -1, f"Test 2 failed: expected -1, got {result2}"
    print("✓ Test 2 passed")
    print()

    # Test 3: Single person
    print("Test 3: Single person (spy by default)")
    result3 = solution.findSpy(1, [])
    assert result3 == 1, f"Test 3 failed: expected 1, got {result3}"
    print("✓ Test 3 passed")
    print()

    # Test 4: Larger organization
    print("Test 4: Larger organization")
    result4 = solution.findSpy(4, [[1, 2], [3, 2], [4, 2]])
    assert result4 == 2, f"Test 4 failed: expected 2, got {result4}"
    print("✓ Test 4 passed")
    print()

    print("All tests passed! ✓")

if __name__ == "__main__":
    test_find_spy()
