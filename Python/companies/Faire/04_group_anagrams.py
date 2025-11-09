#!/usr/bin/env python3
"""
Problem 4: Group Anagrams - TEST SCAFFOLDING (DO NOT EDIT)

Given an array of strings, group anagrams together.

Example 1:
    Input: ["eat", "tea", "tan", "ate", "nat", "bat"]
    Output: [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]

Example 2:
    Input: [""]
    Output: [[""]]

Example 3:
    Input: ["a"]
    Output: [["a"]]

Constraints:
    - 1 <= strs.length <= 10^4
    - 0 <= strs[i].length <= 100
    - strs[i] consists of lowercase English letters

================================================================================
INSTRUCTIONS:
- Implement your solution in: 01_group_anagrams_solution.py
- Run this file to test: python 01_group_anagrams.py
- To reset and practice again: just delete/reset the solution file
================================================================================
"""

# Import the solution
try:
    import importlib.util
    spec = importlib.util.spec_from_file_location(
        "solution_module",
        "04_group_anagrams_solution.py"
    )
    solution_module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(solution_module)
    group_anagrams = solution_module.group_anagrams
except Exception as e:
    print(f"❌ Error importing solution: {e}")
    print(f"   Make sure 04_group_anagrams_solution.py exists.")
    exit(1)


def run_tests():
    """Run test cases for group_anagrams function."""

    # Test Case 1: Basic example
    input1 = ["eat", "tea", "tan", "ate", "nat", "bat"]
    expected1 = [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]
    result1 = group_anagrams(input1)
    # Sort for comparison (order doesn't matter)
    result1_sorted = [sorted(group) for group in result1]
    expected1_sorted = [sorted(group) for group in expected1]
    assert sorted(result1_sorted) == sorted(expected1_sorted), f"Test 1 failed: {result1}"
    print("✓ Test 1 passed: Basic grouping")

    # Test Case 2: Empty string
    input2 = [""]
    expected2 = [[""]]
    result2 = group_anagrams(input2)
    assert result2 == expected2, f"Test 2 failed: {result2}"
    print("✓ Test 2 passed: Empty string")

    # Test Case 3: Single character
    input3 = ["a"]
    expected3 = [["a"]]
    result3 = group_anagrams(input3)
    assert result3 == expected3, f"Test 3 failed: {result3}"
    print("✓ Test 3 passed: Single character")

    # Test Case 4: No anagrams
    input4 = ["abc", "def", "ghi"]
    result4 = group_anagrams(input4)
    assert len(result4) == 3, f"Test 4 failed: {result4}"
    print("✓ Test 4 passed: No anagrams")

    # Test Case 5: All anagrams
    input5 = ["abc", "bca", "cab"]
    result5 = group_anagrams(input5)
    assert len(result5) == 1 and len(result5[0]) == 3, f"Test 5 failed: {result5}"
    print("✓ Test 5 passed: All anagrams")

    print("\n" + "="*50)
    print("All basic tests passed! ✓")
    print("="*50)


def run_custom_tests():
    """Add your own custom test cases here."""
    print("\nRunning custom tests...")

    # Add your custom test cases here
    # Example:
    # custom_input = ["your", "test", "case"]
    # custom_result = group_anagrams(custom_input)
    # print(f"Custom test result: {custom_result}")

    print("No custom tests defined yet.")


if __name__ == "__main__":
    print("Testing Group Anagrams Solution")
    print("="*50 + "\n")

    try:
        run_tests()
        run_custom_tests()
    except AssertionError as e:
        print(f"\n❌ Test failed: {e}")
    except NotImplementedError:
        print("\n⚠️  Solution not implemented yet. Please implement group_anagrams().")
    except Exception as e:
        print(f"\n❌ Error: {e}")
