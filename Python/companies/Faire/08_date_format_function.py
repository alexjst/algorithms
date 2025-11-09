#!/usr/bin/env python3
"""
Problem 8: Date Format Function

Convert dates between different formats and validate them.

Supported formats:
- "MM/DD/YYYY" (e.g., "03/15/2024")
- "YYYY-MM-DD" (e.g., "2024-03-15")
- "DD.MM.YYYY" (e.g., "15.03.2024")
- "Month DD, YYYY" (e.g., "March 15, 2024")

Example 1:
    Input: date = "03/15/2024", from_format = "MM/DD/YYYY", to_format = "YYYY-MM-DD"
    Output: "2024-03-15"

Example 2:
    Input: date = "2024-02-30", from_format = "YYYY-MM-DD", to_format = "MM/DD/YYYY"
    Output: None (invalid date - Feb 30 doesn't exist)

Constraints:
    - Validate dates (check for invalid dates like Feb 30, Apr 31)
    - Handle leap years correctly
    - Year range: 1900-2100
"""

from typing import Optional


def is_leap_year(year: int) -> bool:
    """
    Check if a year is a leap year.

    Args:
        year: Year to check

    Returns:
        True if leap year, False otherwise
    """
    # TODO: Implement leap year check
    return False  # Placeholder


def convert_date_format(date: str, from_format: str, to_format: str) -> Optional[str]:
    """
    Convert date from one format to another with validation.

    Args:
        date: Date string to convert
        from_format: Source format
        to_format: Target format

    Returns:
        Converted date string, or None if invalid
    """
    # TODO: Implement date conversion with validation
    return None  # Placeholder


def run_tests():
    """Run test cases for date format conversion."""

    # Test Case 1: Basic conversion
    result1 = convert_date_format("03/15/2024", "MM/DD/YYYY", "YYYY-MM-DD")
    assert result1 == "2024-03-15", f"Test 1 failed: {result1}"
    print("✓ Test 1 passed: MM/DD/YYYY to YYYY-MM-DD")

    # Test Case 2: Invalid date (Feb 30)
    result2 = convert_date_format("02/30/2024", "MM/DD/YYYY", "YYYY-MM-DD")
    assert result2 is None, f"Test 2 failed: should be None, got {result2}"
    print("✓ Test 2 passed: Invalid date detected (Feb 30)")

    # Test Case 3: Leap year (Feb 29, 2024)
    result3 = convert_date_format("02/29/2024", "MM/DD/YYYY", "YYYY-MM-DD")
    assert result3 == "2024-02-29", f"Test 3 failed: {result3}"
    print("✓ Test 3 passed: Leap year date")

    # Test Case 4: Non-leap year (Feb 29, 2023)
    result4 = convert_date_format("02/29/2023", "MM/DD/YYYY", "YYYY-MM-DD")
    assert result4 is None, f"Test 4 failed: should be None, got {result4}"
    print("✓ Test 4 passed: Invalid leap year date detected")

    # Test Case 5: Dot format conversion
    result5 = convert_date_format("15.03.2024", "DD.MM.YYYY", "MM/DD/YYYY")
    assert result5 == "03/15/2024", f"Test 5 failed: {result5}"
    print("✓ Test 5 passed: DD.MM.YYYY to MM/DD/YYYY")

    print("\n" + "="*50)
    print("All basic tests passed! ✓")
    print("="*50)


def run_custom_tests():
    """Add your own custom test cases here."""
    print("\nRunning custom tests...")

    # Test leap year function
    print("\nTesting leap year:")
    test_years = [2000, 2020, 2024, 1900, 2023, 2100]
    for year in test_years:
        is_leap = is_leap_year(year)
        print(f"  {year}: {'Leap' if is_leap else 'Not leap'}")

    print("\nNo custom date conversion tests defined yet.")


if __name__ == "__main__":
    print("Testing Date Format Conversion Solution")
    print("="*50 + "\n")

    try:
        run_tests()
        run_custom_tests()
    except AssertionError as e:
        print(f"\n❌ Test failed: {e}")
    except Exception as e:
        print(f"\n❌ Error: {e}")
