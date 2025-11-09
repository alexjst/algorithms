#!/usr/bin/env python3
"""
Problem 12: Digit Frequency Counter

Given a range [start, end], count frequency of each digit (0-9) across all numbers.

Example 1:
    Input: start = 1, end = 13
    Output: {0: 1, 1: 6, 2: 2, 3: 2, 4: 1, 5: 1, 6: 1, 7: 1, 8: 1, 9: 1}
    Explanation:
        1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13
        Digit 1 appears: 1, 10, 11, 11, 12, 13 = 6 times
        Digit 0 appears: 10 = 1 time
        ...

Example 2:
    Input: start = 10, end = 12
    Output: {0: 1, 1: 4, 2: 1, ...}
    Numbers: 10, 11, 12

Constraints:
    - 0 <= start <= end <= 10^9
    - Return dictionary with all digits 0-9
    - Count each digit occurrence across all numbers - TEST SCAFFOLDING (DO NOT EDIT)

================================================================================
INSTRUCTIONS:
- Implement your solution in: 12_digit_frequency_counter_solution.py
- Run this file to test: python 12_digit_frequency_counter.py
- To reset and practice again: just delete/reset the solution file
================================================================================
"""

# Import the solution
try:
    import importlib.util
    spec = importlib.util.spec_from_file_location(
        "solution_module",
        "12_digit_frequency_counter_solution.py"
    )
    solution_module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(solution_module)
    count_digit_frequency = solution_module.count_digit_frequency
except Exception as e:
    print(f"❌ Error importing solution: {e}")
    print(f"   Make sure 12_digit_frequency_counter_solution.py exists.")
    exit(1)

def run_tests():
    """Run test cases for digit frequency counter."""

    # Test Case 1: Basic example
    result1 = count_digit_frequency(1, 13)
    assert result1[1] == 6, f"Test 1 failed: digit 1 should appear 6 times, got {result1[1]}"
    assert result1[0] == 1, f"Test 1 failed: digit 0 should appear 1 time, got {result1[0]}"
    print("✓ Test 1 passed: Numbers 1-13")

    # Test Case 2: Small range
    result2 = count_digit_frequency(10, 12)
    # 10: 1, 0
    # 11: 1, 1
    # 12: 1, 2
    # Total: 0->1, 1->4, 2->1
    assert result2[0] == 1, f"Test 2 failed: digit 0 count {result2[0]}"
    assert result2[1] == 4, f"Test 2 failed: digit 1 count {result2[1]}"
    assert result2[2] == 1, f"Test 2 failed: digit 2 count {result2[2]}"
    print("✓ Test 2 passed: Numbers 10-12")

    # Test Case 3: Single number
    result3 = count_digit_frequency(5, 5)
    assert result3[5] == 1, f"Test 3 failed: digit 5 should be 1"
    assert sum(result3.values()) == 1, "Test 3 failed: total count should be 1"
    print("✓ Test 3 passed: Single number")

    # Test Case 4: Number with repeated digits
    result4 = count_digit_frequency(11, 11)
    assert result4[1] == 2, f"Test 4 failed: digit 1 should appear 2 times in 11"
    print("✓ Test 4 passed: Repeated digits")

    print("\n" + "="*50)
    print("All basic tests passed! ✓")
    print("="*50)



def run_custom_tests():
    """Add your own custom test cases here."""
    print("\nRunning custom tests...")

    # Show digit frequency for a range
    print("\nDigit frequency for 1-20:")
    result = count_digit_frequency(1, 20)
    for digit in range(10):
        if result[digit] > 0:
            print(f"  Digit {digit}: {result[digit]} times")

    print("\nNo custom tests defined yet.")



if __name__ == "__main__":
    print("Testing Digit Frequency Counter Solution")
    print("="*50 + "\n")

    try:
        run_tests()
        run_custom_tests()
    except AssertionError as e:
        print(f"\n❌ Test failed: {e}")
    except Exception as e:
        print(f"\n❌ Error: {e}")
