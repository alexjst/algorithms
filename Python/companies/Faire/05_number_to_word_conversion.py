#!/usr/bin/env python3
"""
Problem 5: Number to Word Conversion

Convert numbers in range [start, end] to English words and calculate total character length.

Example 1:
    Input: start = 1, end = 3
    Output: 11
    Explanation:
        1 -> "one" (3 chars)
        2 -> "two" (3 chars)
        3 -> "three" (5 chars)
        Total: 3 + 3 + 5 = 11

Example 2:
    Input: start = 10, end = 12
    Output: 15
    Explanation:
        10 -> "ten" (3 chars)
        11 -> "eleven" (6 chars)
        12 -> "twelve" (6 chars)
        Total: 15 (without spaces)

Constraints:
    - 1 <= start <= end <= 10000
    - Count characters excluding spaces
    - Handle numbers like 23 -> "twenty three"
"""

def number_to_words(num: int) -> str:
    """
    Convert a number to its English word representation.

    Args:
        num: Number to convert (1 to 10000)

    Returns:
        English word representation (with spaces)
    """
    # TODO: Implement number to words conversion
    return ""  # Placeholder


def total_word_length(start: int, end: int) -> int:
    """
    Calculate total character length of all numbers in range [start, end].

    Args:
        start: Starting number
        end: Ending number

    Returns:
        Total character count (excluding spaces)
    """
    # TODO: Implement your solution here
    return 0  # Placeholder


def run_tests():
    """Run test cases for number to word conversion."""

    # Test Case 1: Basic example
    result1 = total_word_length(1, 3)
    assert result1 == 11, f"Test 1 failed: expected 11, got {result1}"
    print("✓ Test 1 passed: Numbers 1-3")

    # Test Case 2: Teens
    result2 = total_word_length(10, 12)
    expected2 = len("ten") + len("eleven") + len("twelve")
    assert result2 == expected2, f"Test 2 failed: expected {expected2}, got {result2}"
    print("✓ Test 2 passed: Numbers 10-12")

    # Test Case 3: Single number
    result3 = total_word_length(5, 5)
    assert result3 == 4, f"Test 3 failed: expected 4, got {result3}"  # "five"
    print("✓ Test 3 passed: Single number")

    # Test Case 4: Number with space (e.g., 21 = "twenty one")
    # 21 -> "twenty one" = 9 chars without space
    result4 = number_to_words(21)
    print(f"  21 -> '{result4}'")
    print("✓ Test 4 passed: Number with space")

    print("\n" + "="*50)
    print("All basic tests passed! ✓")
    print("="*50)


def run_custom_tests():
    """Add your own custom test cases here."""
    print("\nRunning custom tests...")

    # Test individual number conversions
    print("\nTesting individual conversions:")
    test_numbers = [1, 10, 15, 20, 23, 100, 123]
    for num in test_numbers:
        word = number_to_words(num)
        print(f"  {num} -> '{word}'")

    print("\nNo custom range tests defined yet.")


if __name__ == "__main__":
    print("Testing Number to Word Conversion Solution")
    print("="*50 + "\n")

    try:
        run_tests()
        run_custom_tests()
    except AssertionError as e:
        print(f"\n❌ Test failed: {e}")
    except Exception as e:
        print(f"\n❌ Error: {e}")
