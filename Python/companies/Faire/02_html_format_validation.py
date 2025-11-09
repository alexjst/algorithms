#!/usr/bin/env python3
"""
Problem 2: HTML Format Validation - TEST SCAFFOLDING (DO NOT EDIT)

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

================================================================================
INSTRUCTIONS:
- Implement your solution in: 02_html_format_validation_solution.py
- Run this file to test: python 02_html_format_validation.py
- To reset and practice again: just delete/reset the solution file
================================================================================
"""

# Import the solution
try:
    import importlib.util
    spec = importlib.util.spec_from_file_location(
        "solution_module",
        "02_html_format_validation_solution.py"
    )
    solution_module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(solution_module)
    is_valid_html = solution_module.is_valid_html
except Exception as e:
    print(f"❌ Error importing solution: {e}")
    print("   Make sure 02_html_format_validation_solution.py exists.")
    exit(1)


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
