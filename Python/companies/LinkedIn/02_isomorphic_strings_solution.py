"""
Solution for Isomorphic Strings

Implement your solution below.
"""

def isIsomorphic(s: str, t: str) -> bool:
    """
    Determine if two strings are isomorphic.

    Args:
        s: First string
        t: Second string

    Returns:
        True if strings are isomorphic, False otherwise

    Approach:
        Use two hash maps to maintain bidirectional mapping.
        - Map s[i] -> t[i]: Ensure each char in s maps to exactly one char in t
        - Map t[i] -> s[i]: Ensure each char in t maps to exactly one char in s

    Time: O(n) where n is length of string
    Space: O(1) - at most 256 ASCII characters
    """
    # TODO: Implement your solution
    # Hint: Create two dictionaries: map_s_to_t and map_t_to_s
    # For each character pair (s[i], t[i]):
    #   - Check if s[i] already mapped and if mapping is consistent
    #   - Check if t[i] already mapped and if mapping is consistent
    #   - If not mapped, add both mappings

    raise NotImplementedError("Implement this function")
