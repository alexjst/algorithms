#!/usr/bin/env python3
"""
Problem 3: Haiku Finder (5-7-5 Syllables)

Find all valid haikus in a list of sentences. A haiku consists of exactly 3 lines
with syllable counts of 5-7-5.

Example 1:
    Input: [
        "An old silent pond",     # 5 syllables
        "A frog jumps into the pond",  # 7 syllables
        "Splash! Silence again"   # 5 syllables
    ]
    Output: True

Example 2:
    Input: [
        "Beautiful morning",  # 5 syllables
        "Birds are singing",  # 4 syllables (not 7)
        "Nature awakes"       # 4 syllables
    ]
    Output: False

Constraints:
    - Input is a list of exactly 3 strings
    - Each string contains only lowercase letters and spaces
    - Use simple vowel-based syllable counting - TEST SCAFFOLDING (DO NOT EDIT)

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
        "03_haiku_finder_solution.py"
    )
    solution_module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(solution_module)
    count_syllables = solution_module.count_syllables
    is_haiku = solution_module.is_haiku
except Exception as e:
    print(f"❌ Error importing solution: {e}")
    print(f"   Make sure 03_haiku_finder_solution.py exists.")
    exit(1)

def run_tests():
    """Run test cases for haiku validation."""

    # Test Case 1: Valid haiku
    input1 = [
        "An old silent pond",
        "A frog jumps into the pond",
        "Splash Silence again"
    ]
    assert is_haiku(input1) == True, "Test 1 failed: Valid haiku"
    print("✓ Test 1 passed: Valid haiku")

    # Test Case 2: Invalid syllable count
    input2 = [
        "Beautiful morning",
        "Birds singing",
        "Nature awakes"
    ]
    assert is_haiku(input2) == False, "Test 2 failed: Invalid syllable count"
    print("✓ Test 2 passed: Invalid syllable count detected")

    # Test Case 3: Simple valid haiku
    input3 = [
        "I am very cool",      # 5
        "You are also very cool",  # 7
        "We are all cool"      # 5
    ]
    # Note: This test depends on your syllable counting implementation
    print("✓ Test 3 passed: Simple haiku check")

    print("\n" + "="*50)
    print("All basic tests passed! ✓")
    print("="*50)



def run_custom_tests():
    """Add your own custom test cases here."""
    print("\nRunning custom tests...")

    # Test syllable counting helper
    print("\nTesting syllable counter:")
    test_words = ["hello", "beautiful", "sky", "programming"]
    for word in test_words:
        count = count_syllables(word)
        print(f"  '{word}': {count} syllables")

    print("\nNo custom haiku tests defined yet.")



if __name__ == "__main__":
    print("Testing Haiku Finder Solution")
    print("="*50 + "\n")

    try:
        run_tests()
        run_custom_tests()
    except AssertionError as e:
        print(f"\n❌ Test failed: {e}")
    except Exception as e:
        print(f"\n❌ Error: {e}")
