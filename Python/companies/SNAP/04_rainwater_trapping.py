#!/usr/bin/env python3
"""
Problem 4: Rainwater Trapping

Classic problem asked at SNAP for array/stack manipulation.
Calculate how much rainwater can be trapped after raining.

Requirements:
- Given elevation map as array of heights
- Calculate total water trapped between bars
- O(n) time complexity

Example:
    heights = [0,1,0,2,1,0,1,3,2,1,2,1]
    calculator = RainwaterCalculator()
    water = calculator.trap(heights)
    # Returns: 6 units of water

Time Complexity: O(n)
Space Complexity: O(1) for two-pointer, O(n) for DP
"""

try:
    import importlib.util
    spec = importlib.util.spec_from_file_location("solution_module",
                                                   "04_rainwater_trapping_solution.py")
    solution_module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(solution_module)
    RainwaterCalculator = solution_module.RainwaterCalculator
except Exception as e:
    print(f"❌ Error importing solution: {e}")
    exit(1)

def test_rainwater():
    print("Testing Rainwater Trapping...")
    print()

    calc = RainwaterCalculator()

    # Test 1: Example from problem
    print("Test 1: Standard example")
    result1 = calc.trap([0,1,0,2,1,0,1,3,2,1,2,1])
    assert result1 == 6, f"Test 1 failed: expected 6, got {result1}"
    print("✓ Test 1 passed")
    print()

    # Test 2: No water can be trapped
    print("Test 2: No water trapped")
    result2 = calc.trap([1,2,3,4,5])
    assert result2 == 0, f"Test 2 failed: expected 0, got {result2}"
    print("✓ Test 2 passed")
    print()

    # Test 3: Simple valley
    print("Test 3: Simple valley")
    result3 = calc.trap([3,0,2,0,4])
    assert result3 == 7, f"Test 3 failed: expected 7, got {result3}"
    print("✓ Test 3 passed")
    print()

    print("All tests passed! ✓")

if __name__ == "__main__":
    test_rainwater()
