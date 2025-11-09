#!/usr/bin/env python3
"""
Solution for Problem 5: Number to Word Conversion

Asked 3+ times at Faire

Problem: Convert numbers 1-1000 to English words and calculate total character length.

TODO: Implement the functions below.

Key Requirements:
- Handle special cases: 11-19 (eleven, twelve, ..., nineteen)
- Handle tens: 20, 30, ..., 90 (twenty, thirty, ..., ninety)
- Handle hundreds: 100, 200, ..., 900
- Handle 1000
- Spaces between words DON'T count toward character length
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
    """
    # TODO: Implement number to words conversion
    # Hint: Create lookup tables for:
    #   - Ones: 1-9 ('one', 'two', ...)
    #   - Teens: 11-19 ('eleven', 'twelve', ...)
    #   - Tens: 20, 30, ..., 90 ('twenty', 'thirty', ...)
    pass


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
    """
    # TODO: Implement total length calculation
    # Hint: Use number_to_words and remove spaces, then sum lengths
    pass
