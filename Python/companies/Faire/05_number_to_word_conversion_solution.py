#!/usr/bin/env python3
"""
Solution for Problem 5: Number to Word Conversion

🚨 ACTUAL FAIRE INTERVIEW PROBLEM - Asked 3+ times

Problem: Convert numbers 1-1000 to English words and calculate total character length.

Key Approach:
- Use lookup tables for ones, teens, tens
- Build words compositionally: "twenty" + "three" = "twenty three"
- Count characters (spaces don't count!)

Edge Cases:
- Special cases: 11-19 (eleven, twelve, thirteen, etc.)
- Tens: 20, 30, 40, ..., 90
- Hundreds: 100, 200, ..., 900
- 1000 is special case
"""


def number_to_words(n: int) -> str:
    """
    Convert a number (1-1000) to its English word representation.

    Args:
        n: Integer from 1 to 1000

    Returns:
        English word representation (lowercase, with spaces)

    Examples:
        >>> number_to_words(1)
        'one'
        >>> number_to_words(11)
        'eleven'
        >>> number_to_words(23)
        'twenty three'
        >>> number_to_words(100)
        'one hundred'
        >>> number_to_words(1000)
        'one thousand'

    Time: O(1) - constant number of operations
    Space: O(1) - constant size lookup tables
    """
    # Edge case
    if n == 1000:
        return "one thousand"

    # Lookup tables
    ones = {
        1: "one", 2: "two", 3: "three", 4: "four", 5: "five",
        6: "six", 7: "seven", 8: "eight", 9: "nine"
    }

    teens = {
        10: "ten", 11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen",
        15: "fifteen", 16: "sixteen", 17: "seventeen", 18: "eighteen", 19: "nineteen"
    }

    tens = {
        20: "twenty", 30: "thirty", 40: "forty", 50: "fifty",
        60: "sixty", 70: "seventy", 80: "eighty", 90: "ninety"
    }

    result = []

    # Handle hundreds place
    if n >= 100:
        hundreds_digit = n // 100
        result.append(ones[hundreds_digit])
        result.append("hundred")
        n = n % 100

    # Handle tens and ones
    if n >= 20:
        # 20-99 (not including teens)
        tens_digit = (n // 10) * 10
        result.append(tens[tens_digit])
        n = n % 10

        if n > 0:
            # Add ones place
            result.append(ones[n])

    elif n >= 10:
        # 10-19 (teens)
        result.append(teens[n])

    elif n > 0:
        # 1-9
        result.append(ones[n])

    return " ".join(result)


def total_word_length(start: int, end: int) -> int:
    """
    Calculate total character length (excluding spaces) for numbers in range.

    Args:
        start: Starting number (inclusive)
        end: Ending number (inclusive)

    Returns:
        Total number of characters (spaces don't count)

    Examples:
        >>> total_word_length(1, 1)  # "one"
        3
        >>> total_word_length(1, 3)  # "one" + "two" + "three"
        11
        >>> total_word_length(1, 5)  # "one" + "two" + "three" + "four" + "five"
        19

    Time: O(n) where n = end - start + 1
    Space: O(1)
    """
    total = 0

    for num in range(start, end + 1):
        word = number_to_words(num)
        # Remove spaces and count characters
        char_count = len(word.replace(" ", ""))
        total += char_count

    return total


if __name__ == "__main__":
    # Test basic conversions
    print("=== Number to Word Examples ===")
    test_numbers = [1, 5, 11, 15, 20, 23, 99, 100, 342, 999, 1000]

    for num in test_numbers:
        word = number_to_words(num)
        char_count = len(word.replace(" ", ""))
        print(f"{num:4d} -> {word:30s} ({char_count} chars)")

    # Test total length calculation
    print("\n=== Total Length Examples ===")
    print(f"1-5:   {total_word_length(1, 5)} characters")
    print(f"1-10:  {total_word_length(1, 10)} characters")
    print(f"1-100: {total_word_length(1, 100)} characters")

    # Typical interview question: sum for 1-1000
    print(f"\n1-1000: {total_word_length(1, 1000)} characters")
