#!/usr/bin/env python3
"""
Problem 10: TV Remote Keyboard Navigation

SNAP asks this for understanding of BFS shortest path in grids.
Navigate a TV keyboard grid to type a string using remote control buttons.

Requirements:
- TV remote has 5 buttons: UP, DOWN, LEFT, RIGHT, OK
- Keyboard is 2D grid of characters
- Cursor starts at top-left (0, 0)
- Find shortest sequence of button presses
- Return any shortest path if multiple exist

Example:
    keyboard = [
        ['A', 'B', 'C', 'D', 'E'],
        ['F', 'G', 'H', 'I', 'J'],
        ['K', 'L', 'M', 'N', 'O'],
        ['P', 'Q', 'R', 'S', 'T'],
        ['U', 'V', 'W', 'X', 'Y']
    ]

    input_str = "GAB"

    # To type 'G': Start at A(0,0) -> G(1,1)
    # Path: RIGHT, DOWN, OK
    # To type 'A' from G: G(1,1) -> A(0,0)
    # Path: UP, LEFT, OK
    # To type 'B' from A: A(0,0) -> B(0,1)
    # Path: RIGHT, OK

    # Full result: ["RIGHT", "DOWN", "OK", "UP", "LEFT", "OK", "RIGHT", "OK"]

Time Complexity: O(k * m * n) where k is string length, m*n is grid size
Space Complexity: O(m * n)
"""

try:
    import importlib.util
    spec = importlib.util.spec_from_file_location("solution_module",
                                                   "10_tv_remote_navigation_solution.py")
    solution_module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(solution_module)
    Solution = solution_module.Solution
except Exception as e:
    print(f"❌ Error importing solution: {e}")
    exit(1)

def test_tv_remote():
    print("Testing TV Remote Keyboard Navigation...")
    print()

    solution = Solution()
    keyboard = [
        ['A', 'B', 'C', 'D', 'E'],
        ['F', 'G', 'H', 'I', 'J'],
        ['K', 'L', 'M', 'N', 'O'],
        ['P', 'Q', 'R', 'S', 'T'],
        ['U', 'V', 'W', 'X', 'Y']
    ]

    # Test 1: Single character
    print("Test 1: Type single character 'G'")
    result1 = solution.typePath("G", keyboard)
    assert "OK" in result1, "Test 1 failed: must include OK"
    print(f"Path: {result1}")
    print("✓ Test 1 passed")
    print()

    # Test 2: Multiple characters
    print("Test 2: Type 'GAB'")
    result2 = solution.typePath("GAB", keyboard)
    assert result2.count("OK") == 3, "Test 2 failed: must have 3 OK presses"
    print(f"Path: {result2}")
    print("✓ Test 2 passed")
    print()

    # Test 3: Start character
    print("Test 3: Type 'A' (already at start)")
    result3 = solution.typePath("A", keyboard)
    assert result3 == ["OK"], f"Test 3 failed: expected ['OK'], got {result3}"
    print("✓ Test 3 passed")
    print()

    print("All tests passed! ✓")

if __name__ == "__main__":
    test_tv_remote()
