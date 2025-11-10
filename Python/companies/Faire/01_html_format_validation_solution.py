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


def is_valid_tags(s: str) -> bool:
    """
    Validate if string has properly matched and nested tags.

    Tag format:
    - Opening: {{ #tagname }}
    - Closing: {{ /tagname }}
    - Single { or } is treated as normal text (not a tag)

    Args:
        s: String to validate

    Returns:
        True if valid (all tags properly nested), False otherwise

    Time Complexity: O(n) where n is string length
    Space Complexity: O(t) where t is number of tags (for the stack)

    Examples:
        >>> is_valid_tags("{{ #abc }} {{ #cba }} hello {{ /cba }} {{ /abc }}")
        True
        >>> is_valid_tags("{{ #abc }} hello { world {{ /abc }}")
        True
        >>> is_valid_tags("{{ #abc }} hello world {{ /abc")
        False
        >>> is_valid_tags("{{ #abc }} {{ #cba }} {{ /abc }} {{ /cba }}")
        False
    """
    # TODO: Implement your solution here
    # Hint: Use a stack to track opening tags
    # Remember to handle:
    #   - Single { or } (not part of tags)
    #   - Incomplete tags (missing }})
    #   - Empty string (should return True)
    #   - LIFO order for closing tags

    # invalid input (None)
    if s is None:
        return False

    # empty string
    if not s:
        return True

    stack = []
    n, i = len(s), 0

    # print(f"input s={s}")
    while i < n:
        if i < n-1 and s[i:i+2] == "{{":
            # print(f"open tag at {i}")
            close_tag_found = False
            j = i+2
            while j < n:
                if j < n-1 and s[j:j+2] == "}}":
                    # print(f"close tag at {j}")
                    tag = s[i+2:j].strip()
                    # print(f"tag is {tag}")
                    if len(tag) >= 2 and tag[0] in ("#", "/"):
                        if tag[0] == "#":
                            stack.append(tag)
                            # print(f"insert: stack={stack}")
                        else:
                            if len(stack) and stack[-1][1:] == tag[1:]:
                                stack.pop()
                                # print(f"pop: stack={stack}")
                            else:
                                # print(f"return False on stack")
                                return False
                    else:
                        # print(f"return False on invalid tag")
                        return False
                    close_tag_found = True
                    # print(f"breaking on close_tag_found")
                    break
                # print(f"j is now {j}")
                j += 1
            if not close_tag_found:
                # print(f"return False on missing close tag")
                return False
            else:
                i = j + 2
                # print(f"i is now {i}")
        i += 1

    # print(f"final stack={stack}")
    return len(stack) == 0

if __name__ == "__main__":
    assert is_valid_tags("") == True, "empty string should be valid"
    assert is_valid_tags("{{}}") == False, "{{}} should be invalid tag"
    assert is_valid_tags("{{ abc }}") == False, "{{ abc }} should be invalid tag"
    assert is_valid_tags("{{ #   abc }}xxx{xxx}xxx{{ /   abc}}") == True, "{{ #  abc }} should be valid tag"
