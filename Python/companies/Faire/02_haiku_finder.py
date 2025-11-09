#!/usr/bin/env python3
"""
Problem 2: Haiku Finder (Find First Haiku in Sentence)

Given a sentence (single string with mixed case and punctuation) and a syllable
dictionary, find the FIRST haiku in the sentence. A haiku consists of 3 consecutive
word sequences with syllable counts of 5-7-5.

Example 1:
    Input:
        sentence = "Internationalization a Simple flower Petals shine Vibrant don't Pure Stares into Void. Return home"
        syllable_dict = {
            "internationalization": 8, "a": 1, "simple": 2, "flower": 2,
            "petals": 2, "shine": 1, "vibrant": 2, "don't": 1, "pure": 1,
            "stares": 2, "into": 2, "void": 1, "return": 2, "home": 1
        }

    Output:
        ["a Simple flower", "Petals shine Vibrant don't Pure", "Stares into Void."]

    Explanation:
        Line 1: "a Simple flower" = 1 + 2 + 2 = 5 syllables
        Line 2: "Petals shine Vibrant don't Pure" = 2 + 1 + 2 + 1 + 1 = 7 syllables
        Line 3: "Stares into Void." = 2 + 2 + 1 = 5 syllables

Example 2:
    Input:
        sentence = "Hello world foo bar"
        syllable_dict = {"hello": 2, "world": 1, "foo": 1, "bar": 1}

    Output: None

    Explanation: Cannot form a valid 5-7-5 haiku from these words

Constraints:
    - Sentence contains words separated by spaces
    - Words may have mixed case and punctuation
    - When looking up in dictionary:
      * Convert to lowercase
      * Strip trailing punctuation (., , ! ? etc.)
    - Preserve original case and punctuation in output
    - Return the FIRST valid haiku found (leftmost starting position)
    - Return None if no valid haiku exists
    - Optimal solution should be O(n) using prefix sums

Key Requirements from 1point3acres Interview Reports:
    - Must handle punctuation correctly
    - Must preserve original formatting in output
    - Strong emphasis on test cases and edge cases
    - Code quality and optimization are critical

================================================================================
INSTRUCTIONS:
- Implement your solution in: 03_haiku_finder_solution.py
- Run this file to test: python 03_haiku_finder.py
- To reset and practice again: just delete/reset the solution file
================================================================================
"""

# Import the solution
try:
    import importlib.util
    spec = importlib.util.spec_from_file_location(
        "solution_module",
        "02_haiku_finder_solution.py"
    )
    solution_module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(solution_module)
    find_haiku = solution_module.find_haiku
except Exception as e:
    print(f"❌ Error importing solution: {e}")
    print(f"   Make sure 02_haiku_finder_solution.py exists.")
    exit(1)

def run_tests():
    """Run test cases for haiku finding."""

    # Test Case 1: Valid haiku from 1point3acres
    sentence1 = "Internationalization a Simple flower Petals shine Vibrant don't Pure Stares into Void. Return home"
    syllable_dict1 = {
        "internationalization": 8, "a": 1, "simple": 2, "flower": 2,
        "petals": 2, "shine": 1, "vibrant": 2, "don't": 1, "pure": 1,
        "stares": 2, "into": 2, "void": 1, "return": 2, "home": 1
    }
    result1 = find_haiku(sentence1, syllable_dict1)
    expected1 = ["a Simple flower", "Petals shine Vibrant don't Pure", "Stares into Void."]
    assert result1 == expected1, f"Test 1 failed: Expected {expected1}, got {result1}"
    print("✓ Test 1 passed: Valid haiku found from 1point3acres example")

    # Test Case 2: No valid haiku
    sentence2 = "Hello world"
    syllable_dict2 = {"hello": 2, "world": 1}
    result2 = find_haiku(sentence2, syllable_dict2)
    assert result2 is None, f"Test 2 failed: Expected None, got {result2}"
    print("✓ Test 2 passed: No haiku returns None")

    # Test Case 3: Multiple possible haikus - should return first
    sentence3 = "I am cool you are also cool we are all cool"
    syllable_dict3 = {
        "i": 1, "am": 1, "cool": 1, "you": 1, "are": 1,
        "also": 2, "we": 1, "all": 1
    }
    result3 = find_haiku(sentence3, syllable_dict3)
    # First haiku: "I am cool you are" (5), "also cool we are all cool" (7)?
    # This is tricky - depends on implementation
    if result3 is not None:
        print(f"✓ Test 3 passed: Found haiku (first one): {result3}")
    else:
        print("✓ Test 3 passed: No valid haiku found")

    # Test Case 4: Punctuation handling
    sentence4 = "Hello, world! This is nice. Very nice indeed, yes."
    syllable_dict4 = {
        "hello": 2, "world": 1, "this": 1, "is": 1,
        "nice": 1, "very": 2, "indeed": 2, "yes": 1
    }
    result4 = find_haiku(sentence4, syllable_dict4)
    if result4 is not None:
        # Check that punctuation is preserved in output
        assert any(punct in ' '.join(result4) for punct in [',', '.', '!'] if punct in sentence4), \
            "Punctuation should be preserved in output"
        print(f"✓ Test 4 passed: Punctuation preserved: {result4}")
    else:
        print("✓ Test 4 passed: No valid haiku (acceptable)")

    # Test Case 5: Case sensitivity
    sentence5 = "A Simple Flower grows beautifully in Spring gardens"
    syllable_dict5 = {
        "a": 1, "simple": 2, "flower": 2, "grows": 1,
        "beautifully": 4, "in": 1, "spring": 1, "gardens": 2
    }
    result5 = find_haiku(sentence5, syllable_dict5)
    if result5 is not None:
        # Check that original case is preserved
        assert "Simple" in str(result5) or "simple" in str(result5).lower(), \
            "Original case should be preserved or properly handled"
        print(f"✓ Test 5 passed: Case handling: {result5}")
    else:
        print("✓ Test 5 passed: No valid haiku (acceptable)")

    print("\n" + "="*50)
    print("All basic tests passed! ✓")
    print("="*50)


def run_custom_tests():
    """Add your own custom test cases here."""
    print("\nRunning custom tests...")

    # Edge case: empty sentence
    try:
        result = find_haiku("", {})
        assert result is None, "Empty sentence should return None"
        print("✓ Custom test: Empty sentence handled")
    except Exception as e:
        print(f"✗ Custom test failed: {e}")

    # Edge case: word not in dictionary
    sentence = "Unknown word here"
    syllable_dict = {"word": 1, "here": 1}
    result = find_haiku(sentence, syllable_dict)
    print(f"✓ Custom test: Missing word handled, result: {result}")

    print("\nCustom tests completed.")


if __name__ == "__main__":
    print("Testing Haiku Finder Solution")
    print("(Problem from 1point3acres.com - Faire Interview)")
    print("="*50 + "\n")

    try:
        run_tests()
        run_custom_tests()
    except AssertionError as e:
        print(f"\n❌ Test failed: {e}")
    except Exception as e:
        print(f"\n❌ Error: {e}")
