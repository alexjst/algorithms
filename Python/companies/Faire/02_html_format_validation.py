#!/usr/bin/env python3
"""
Problem 2: Tag Validator (Custom {{ }} Syntax)

🚨 ACTUAL FAIRE INTERVIEW PROBLEM - ASKED 5+ TIMES (2022-2025)

Validate if a string has properly matched and nested tags using CUSTOM syntax.

Tag Format (NOT standard HTML!):
- Opening tag: {{ #tagname }}
- Closing tag: {{ /tagname }}
- Single { or } is treated as NORMAL TEXT (not a tag)
- Tags must be properly nested
- All opening tags must have corresponding closing tags

Example 1 (Valid):
    Input: "{{ #abc }} {{ #cba }} hello world {{ /cba }} {{ /abc }}"
    Output: True
    Explanation: Properly nested - #abc opens, #cba opens, /cba closes, /abc closes

Example 2 (Valid - Single braces OK):
    Input: "{{ #abc }} {{ #cba }} hello { world {{ /cba }} {{ /abc }}"
    Output: True
    Explanation: Single { is treated as normal text

Example 3 (Invalid - Incomplete tag):
    Input: "{{ #abc }} hello world {{ /abc"
    Output: False
    Explanation: Missing closing }} for /abc tag

Example 4 (Invalid - Missing closing tag):
    Input: "{{ #abc }} {{ #cba }} hello world {{ /cba }}"
    Output: False
    Explanation: #abc was opened but never closed

Example 5 (Invalid - Wrong order):
    Input: "{{ #abc }} {{ #cba }} hello world {{ /abc }} {{ /cba }}"
    Output: False
    Explanation: Must close #cba before closing #abc (LIFO order)

🚨 CRITICAL Edge Cases from 1point3acres reports:
1. {{ without space (double brace) - check carefully!
2. Single { or } is normal text
3. Incomplete tags (missing }})
4. Empty string is valid
5. Nested tags must follow LIFO order (stack-based)

Key Implementation Details:
- Use STACK for tag matching
- Parse tags carefully: must have {{ and }} with # or / inside
- Tag name can contain letters, numbers, etc.
- Interviewers WILL ask: "What other edge cases?" - be ready!

Similar to: LC 591 (Tag Validator) but with DIFFERENT syntax

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
    is_valid_tags = solution_module.is_valid_tags
except Exception as e:
    print(f"❌ Error importing solution: {e}")
    print("   Make sure 02_html_format_validation_solution.py exists.")
    exit(1)


def run_tests():
    """Run test cases for tag validation."""

    # Test Case 1: Valid nested tags (from 1p3a)
    input1 = "{{ #abc }} {{ #cba }} hello world {{ /cba }} {{ /abc }}"
    assert is_valid_tags(input1) == True, "Test 1 failed: Valid nested tags"
    print("✓ Test 1 passed: Valid nested tags")

    # Test Case 2: Valid with single brace (from 1p3a)
    input2 = "{{ #abc }} {{ #cba }} hello { world {{ /cba }} {{ /abc }}"
    assert is_valid_tags(input2) == True, "Test 2 failed: Single brace should be OK"
    print("✓ Test 2 passed: Single brace treated as text")

    # Test Case 3: Incomplete tag (from 1p3a)
    input3 = "{{ #abc }} hello world {{ /abc"
    assert is_valid_tags(input3) == False, "Test 3 failed: Incomplete tag"
    print("✓ Test 3 passed: Incomplete tag detected")

    # Test Case 4: Missing closing tag (from 1p3a)
    input4 = "{{ #abc }} {{ #cba }} hello world {{ /cba }}"
    assert is_valid_tags(input4) == False, "Test 4 failed: Missing closing tag"
    print("✓ Test 4 passed: Missing closing tag detected")

    # Test Case 5: Wrong order (from 1p3a)
    input5 = "{{ #abc }} {{ #cba }} hello world {{ /abc }} {{ /cba }}"
    assert is_valid_tags(input5) == False, "Test 5 failed: Wrong closing order"
    print("✓ Test 5 passed: Wrong closing order detected")

    # Test Case 6: Empty string
    input6 = ""
    assert is_valid_tags(input6) == True, "Test 6 failed: Empty string should be valid"
    print("✓ Test 6 passed: Empty string")

    # Test Case 7: Just text, no tags
    input7 = "hello world { this } is text"
    assert is_valid_tags(input7) == True, "Test 7 failed: Text only"
    print("✓ Test 7 passed: Text without tags")

    # Test Case 8: Single tag pair
    input8 = "{{ #div }} content {{ /div }}"
    assert is_valid_tags(input8) == True, "Test 8 failed: Single tag pair"
    print("✓ Test 8 passed: Single tag pair")

    print("\n" + "="*50)
    print("All basic tests passed! ✓")
    print("="*50)


def run_edge_case_tests():
    """
    Additional edge cases that interviewers commonly ask about.
    Based on 1point3acres reports where candidates were asked:
    "What OTHER edge cases can you think of?"
    """
    print("\nRunning edge case tests...")

    # Edge case 1: Double {{ without space
    try:
        input1 = "{{#abc}}"  # No spaces
        result1 = is_valid_tags(input1)
        print(f"  Edge case 1: Double braces without space: {result1}")
    except:
        print("  Edge case 1: May need special handling")

    # Edge case 2: Only opening tag
    input2 = "{{ #abc }}"
    assert is_valid_tags(input2) == False, "Only opening tag should be invalid"
    print("✓ Edge case 2: Only opening tag detected")

    # Edge case 3: Only closing tag
    input3 = "{{ /abc }}"
    assert is_valid_tags(input3) == False, "Only closing tag should be invalid"
    print("✓ Edge case 3: Only closing tag detected")

    # Edge case 4: Extra closing tag
    input4 = "{{ #abc }} {{ /abc }} {{ /abc }}"
    assert is_valid_tags(input4) == False, "Extra closing tag should be invalid"
    print("✓ Edge case 4: Extra closing tag detected")

    # Edge case 5: Nested same name tags
    input5 = "{{ #div }} {{ #div }} {{ /div }} {{ /div }}"
    assert is_valid_tags(input5) == True, "Nested same-name tags should be valid"
    print("✓ Edge case 5: Nested same-name tags")

    # Edge case 6: Multiple single braces
    input6 = "{ { { } } }"
    assert is_valid_tags(input6) == True, "All single braces should be OK"
    print("✓ Edge case 6: Multiple single braces")

    # Edge case 7: Tag name with numbers/special chars
    input7 = "{{ #tag123 }} test {{ /tag123 }}"
    assert is_valid_tags(input7) == True, "Tag names with numbers should work"
    print("✓ Edge case 7: Tag names with numbers")

    print("\nEdge case tests completed.")


if __name__ == "__main__":
    print("🚨 ACTUAL FAIRE PROBLEM: Tag Validator (Custom {{ }} Syntax)")
    print("Source: 1point3acres.com - Asked 5+ times (2022-2025)")
    print("="*70 + "\n")

    try:
        run_tests()
        run_edge_case_tests()

        print("\n" + "="*70)
        print("💡 INTERVIEW TIPS:")
        print("1. Interviewers WILL ask: 'What other edge cases?'")
        print("2. Focus on: incomplete tags, single braces, wrong order")
        print("3. Use STACK for proper nesting validation")
        print("4. Run your code with test cases!")
        print("="*70)
    except AssertionError as e:
        print(f"\n❌ Test failed: {e}")
    except Exception as e:
        print(f"\n❌ Error: {e}")
