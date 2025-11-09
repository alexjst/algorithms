#!/usr/bin/env python3
"""
Solution for Problem 2: Tag Validator (Custom {{ }} Syntax)

🚨 ACTUAL FAIRE INTERVIEW PROBLEM - Asked 5+ times

This is NOT standard HTML! Use {{ #tag }} for opening and {{ /tag }} for closing.

TODO: Implement the function below.

Approach:
1. Use a STACK to track opening tags
2. Parse the string character by character
3. When you find "{{", look for matching "}}" to extract tag
4. If tag starts with #, it's an opening tag - push to stack
5. If tag starts with /, it's a closing tag - must match top of stack
6. Single { or } is treated as normal text (ignore)
7. At the end, stack must be empty

Edge Cases to Handle:
- Single { or } (not part of a tag)
- Incomplete tags like "{{ #abc" (missing }})
- Empty string (valid)
- Text without any tags (valid)
- Wrong closing order
- Extra closing tags
- Only opening tags / only closing tags
"""

from typing import Optional
import re


def is_valid_tags(s: str) -> bool:
    """
    Validate if string has properly matched and nested tags.

    Tag format:
    - Opening: {{ #tagname }}
    - Closing: {{ /tagname }}

    Args:
        s: String to validate

    Returns:
        True if valid (all tags properly nested), False otherwise

    Time Complexity: O(n) where n is string length
    Space Complexity: O(n) for stack in worst case
    """
    # Edge case: empty string is valid (no tags to validate)
    if not s:
        return True

    stack = []
    i = 0

    while i < len(s):
        # Look for opening {{ (need at least 2 characters)
        if i < len(s) - 1 and s[i:i+2] == '{{':
            # Found opening {{, now find closing }}
            j = i + 2
            found_closing = False

            while j < len(s) - 1:
                if s[j:j+2] == '}}':
                    # Found complete tag {{ ... }}
                    tag_content = s[i+2:j].strip()

                    # Check if it's a valid tag (starts with # or /)
                    if tag_content and (tag_content[0] == '#' or tag_content[0] == '/'):
                        if tag_content[0] == '#':
                            # Opening tag: extract tag name and push to stack
                            tag_name = tag_content[1:].strip()
                            stack.append(tag_name)
                        else:  # tag_content[0] == '/'
                            # Closing tag: must match top of stack
                            tag_name = tag_content[1:].strip()
                            if not stack or stack[-1] != tag_name:
                                return False  # Mismatch or extra closing tag
                            stack.pop()

                    # Move past the closing }}
                    i = j + 2
                    found_closing = True
                    break
                j += 1

            # If we didn't find closing }}, this is an incomplete tag
            if not found_closing:
                return False
        else:
            # Regular character (including single { or })
            i += 1

    # All tags must be closed (stack should be empty)
    return len(stack) == 0


# Example implementation (commented out - try yourself first!)
"""
def is_valid_tags(s: str) -> bool:
    if not s:
        return True

    stack = []
    i = 0

    while i < len(s):
        # Look for opening {{
        if i < len(s) - 1 and s[i:i+2] == '{{':
            # Find closing }}
            j = i + 2
            while j < len(s) - 1:
                if s[j:j+2] == '}}':
                    # Extract tag content between {{ and }}
                    tag_content = s[i+2:j].strip()

                    # Check if it's a valid tag (starts with # or /)
                    if tag_content and (tag_content[0] == '#' or tag_content[0] == '/'):
                        if tag_content[0] == '#':
                            # Opening tag
                            tag_name = tag_content[1:].strip()
                            stack.append(tag_name)
                        else:  # tag_content[0] == '/'
                            # Closing tag
                            tag_name = tag_content[1:].strip()
                            if not stack or stack[-1] != tag_name:
                                return False
                            stack.pop()

                    i = j + 2  # Move past }}
                    break
                j += 1
            else:
                # No closing }} found - incomplete tag
                return False
        else:
            # Regular character or single {
            i += 1

    return len(stack) == 0


# Alternative: Using regex
import re

def is_valid_tags_regex(s: str) -> bool:
    if not s:
        return True

    # Find all tags with format {{ #tag }} or {{ /tag }}
    pattern = r'\{\{\s*([#/])(\w+)\s*\}\}'
    matches = re.finditer(pattern, s)

    stack = []
    for match in matches:
        tag_type = match.group(1)  # '#' or '/'
        tag_name = match.group(2)  # tag name

        if tag_type == '#':
            # Opening tag
            stack.append(tag_name)
        else:  # tag_type == '/'
            # Closing tag
            if not stack or stack[-1] != tag_name:
                return False
            stack.pop()

    return len(stack) == 0
"""
