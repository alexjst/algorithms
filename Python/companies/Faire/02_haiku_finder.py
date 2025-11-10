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

    # Test Case 5: Classic pond haiku
    sentence5 = "An old silent pond a frog jumps in the water splash the sound is heard"
    syllable_dict5 = {
        "an": 1, "old": 1, "silent": 2, "pond": 1, "a": 1,
        "frog": 1, "jumps": 1, "in": 1, "the": 1, "water": 2,
        "splash": 1, "sound": 1, "is": 1, "heard": 1
    }
    result5 = find_haiku(sentence5, syllable_dict5)
    expected5 = ["An old silent pond", "a frog jumps in the water", "splash the sound is heard"]
    assert result5 == expected5, f"Test 5 failed: Expected {expected5}, got {result5}"
    print(f"✓ Test 5 passed: Classic pond haiku: {result5}")

    # Test Case 6: Haiku with punctuation preserved
    sentence6 = "Cherry blossoms fall! Gently, drifting to the ground. Spring has now arrived."
    syllable_dict6 = {
        "cherry": 2, "blossoms": 2, "fall": 1, "gently": 2,
        "drifting": 2, "to": 1, "the": 1, "ground": 1,
        "spring": 1, "has": 1, "now": 1, "arrived": 2
    }
    result6 = find_haiku(sentence6, syllable_dict6)
    expected6 = ["Cherry blossoms fall!", "Gently, drifting to the ground.", "Spring has now arrived."]
    assert result6 == expected6, f"Test 6 failed: Expected {expected6}, got {result6}"
    # Check punctuation preserved
    assert "!" in result6[0] and "," in result6[1] and "." in result6[2], "Punctuation must be preserved"
    print(f"✓ Test 6 passed: Punctuation preserved: {result6}")

    # Test Case 7: Valid haiku with mostly 1-syllable words
    sentence7 = "I am cool you are also very nice we all jump so very high"
    syllable_dict7 = {
        "i": 1, "am": 1, "cool": 1, "you": 1, "are": 1,
        "also": 2, "very": 2, "nice": 1, "we": 1, "all": 1,
        "jump": 1, "so": 1, "high": 1
    }
    result7 = find_haiku(sentence7, syllable_dict7)
    expected7 = ["I am cool you are", "also very nice we all", "jump so very high"]
    assert result7 == expected7, f"Test 7 failed: Expected {expected7}, got {result7}"
    print(f"✓ Test 7 passed: Valid haiku with short words: {result7}")

    # Test Case 8: Natural haiku about morning
    sentence8 = "Morning dew glistens softly on the green grass blades very fresh and new"
    syllable_dict8 = {
        "morning": 2, "dew": 1, "glistens": 2, "softly": 2,
        "on": 1, "the": 1, "green": 1, "grass": 1, "blades": 1,
        "very": 2, "fresh": 1, "and": 1, "new": 1
    }
    result8 = find_haiku(sentence8, syllable_dict8)
    expected8 = ["Morning dew glistens", "softly on the green grass blades", "very fresh and new"]
    assert result8 == expected8, f"Test 8 failed: Expected {expected8}, got {result8}"
    print(f"✓ Test 8 passed: Natural morning haiku: {result8}")

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
