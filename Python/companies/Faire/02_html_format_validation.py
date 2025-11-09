#!/usr/bin/env python3
"""
Problem 2: HTML Format Validation

Validate if an HTML string has properly matched and nested tags.

Rules:
- Opening tags: <tag>
- Closing tags: </tag>
- Self-closing tags: <tag/> (valid)
- Tags must be properly nested
- All opening tags must have corresponding closing tags

Example 1:
    Input: "<div><p>Hello</p></div>"
    Output: True

Example 2:
    Input: "<div><p>Hello</div></p>"
    Output: False (improper nesting)

Example 3:
    Input: "<img/>"
    Output: True (self-closing tag)

Constraints:
    - 1 <= html.length <= 10^4
    - Valid tag names contain only lowercase letters
    - No attributes in tags (simplified version)
"""

from typing import List


def is_valid_html(html: str) -> bool:
    """
    Validate if HTML string has properly matched and nested tags.

    Args:
        html: HTML string to validate

    Returns:
        True if valid, False otherwise
    """
    # TODO: Implement your solution here
    return False  # Placeholder - replace with your solution


def run_tests():
    """Run test cases for is_valid_html function."""

    # Test Case 1: Valid nested tags
    input1 = "<div><p>Hello</p></div>"
    assert is_valid_html(input1) == True, "Test 1 failed: Valid nested tags"
    print("✓ Test 1 passed: Valid nested tags")

    # Test Case 2: Improper nesting
    input2 = "<div><p>Hello</div></p>"
    assert is_valid_html(input2) == False, "Test 2 failed: Improper nesting"
    print("✓ Test 2 passed: Improper nesting detected")

    # Test Case 3: Self-closing tag
    input3 = "<img/>"
    assert is_valid_html(input3) == True, "Test 3 failed: Self-closing tag"
    print("✓ Test 3 passed: Self-closing tag")

    # Test Case 4: Missing closing tag
    input4 = "<div><p>Hello</p>"
    assert is_valid_html(input4) == False, "Test 4 failed: Missing closing tag"
    print("✓ Test 4 passed: Missing closing tag detected")

    # Test Case 5: Extra closing tag
    input5 = "<div></div></div>"
    assert is_valid_html(input5) == False, "Test 5 failed: Extra closing tag"
    print("✓ Test 5 passed: Extra closing tag detected")

    # Test Case 6: Empty string
    input6 = ""
    assert is_valid_html(input6) == True, "Test 6 failed: Empty string"
    print("✓ Test 6 passed: Empty string")

    print("\n" + "="*50)
    print("All basic tests passed! ✓")
    print("="*50)


def run_custom_tests():
    """Add your own custom test cases here."""
    print("\nRunning custom tests...")

    # Add your custom test cases here

    print("No custom tests defined yet.")


if __name__ == "__main__":
    print("Testing HTML Format Validation Solution")
    print("="*50 + "\n")

    try:
        run_tests()
        run_custom_tests()
    except AssertionError as e:
        print(f"\n❌ Test failed: {e}")
    except Exception as e:
        print(f"\n❌ Error: {e}")
