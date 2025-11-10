#!/usr/bin/env python3
"""
Pytest test file for Problem 1: HTML Format Validation

Run with: pytest test_01_html_format_validation.py -v
"""

import pytest
import importlib.util

# Import the solution
spec = importlib.util.spec_from_file_location(
    "solution_module",
    "01_html_format_validation_solution.py"
)
solution_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(solution_module)
is_valid_tags = solution_module.is_valid_tags


class TestBasicCases:
    """Basic functionality tests"""

    def test_empty_string(self):
        """Empty string should be valid"""
        assert is_valid_tags("") == True

    def test_no_tags(self):
        """Plain text with no tags should be valid"""
        assert is_valid_tags("hello world") == True

    def test_single_matching_pair(self):
        """Simple matching open/close tags"""
        assert is_valid_tags("{{ #abc }} {{ /abc }}") == True

    def test_nested_tags(self):
        """Properly nested tags"""
        assert is_valid_tags("{{ #abc }} {{ #cba }} hello {{ /cba }} {{ /abc }}") == True

    def test_text_with_tags(self):
        """Tags with text content"""
        assert is_valid_tags("{{ #div }} hello world {{ /div }}") == True


class TestInvalidCases:
    """Test cases that should return False"""

    def test_wrong_closing_order(self):
        """Closing tags in wrong order"""
        assert is_valid_tags("{{ #abc }} {{ #cba }} {{ /abc }} {{ /cba }}") == False

    def test_missing_closing_tag(self):
        """Opening tag without closing"""
        assert is_valid_tags("{{ #abc }} hello") == False

    def test_missing_opening_tag(self):
        """Closing tag without opening"""
        assert is_valid_tags("hello {{ /abc }}") == False

    def test_incomplete_tag_missing_closing_braces(self):
        """Tag missing closing braces"""
        assert is_valid_tags("{{ #abc }} hello world {{ /abc") == False

    def test_mismatched_tag_names(self):
        """Opening and closing tags don't match"""
        assert is_valid_tags("{{ #abc }} {{ /xyz }}") == False


class TestEdgeCases:
    """Edge cases and tricky scenarios"""

    def test_single_brace_ignored(self):
        """Single { or } should be treated as normal text"""
        assert is_valid_tags("{{ #abc }} hello { world {{ /abc }}") == True
        assert is_valid_tags("{{ #abc }} hello } world {{ /abc }}") == True

    def test_single_opening_brace_only(self):
        """Single { without matching }"""
        assert is_valid_tags("hello { world") == True

    def test_whitespace_variations(self):
        """Tags with different whitespace"""
        assert is_valid_tags("{{#abc}} {{/abc}}") == True
        assert is_valid_tags("{{  #abc  }} {{  /abc  }}") == True

    def test_tag_with_content(self):
        """Tag wrapping content"""
        assert is_valid_tags("{{ #p }} some text {{ /p }}") == True

    def test_multiple_tags_same_level(self):
        """Multiple tags at same nesting level"""
        assert is_valid_tags("{{ #a }} {{ /a }} {{ #b }} {{ /b }}") == True

    def test_deeply_nested(self):
        """Multiple levels of nesting"""
        assert is_valid_tags("{{ #a }} {{ #b }} {{ #c }} {{ /c }} {{ /b }} {{ /a }}") == True


class TestAmbiguousCases:
    """Cases where problem statement is ambiguous - clarify with interviewer!"""

    def test_tag_without_hash_or_slash(self):
        """{{ abc }} - no # or / prefix

        This is AMBIGUOUS in the problem statement!
        Ask interviewer: Should this be invalid or ignored as text?
        """
        result = is_valid_tags("{{ abc }}")
        # Uncomment based on interviewer's answer:
        # assert result == False  # If they say it should be invalid
        # assert result == True   # If they say it should be ignored
        print(f"{{ abc }} returned: {result}")

    def test_nested_braces(self):
        """{{ {{ #abc }} }} - nested braces

        Should outer {{ be treated as text or cause error?
        """
        result = is_valid_tags("{{ {{ #abc }} }}")
        print(f"{{ {{ #abc }} }} returned: {result}")


# Parametrized tests for efficiency
@pytest.mark.parametrize("input_str,expected", [
    ("", True),
    ("hello", True),
    ("{{ #a }} {{ /a }}", True),
    ("{{ #a }} {{ #b }} {{ /b }} {{ /a }}", True),
    ("{{ #a }} {{ #b }} {{ /a }} {{ /b }}", False),
    ("{{ #a }}", False),
    ("{{ /a }}", False),
])
def test_parametrized(input_str, expected):
    """Parametrized tests for common cases"""
    assert is_valid_tags(input_str) == expected


if __name__ == "__main__":
    pytest.main([__file__, "-v", "--tb=short"])
