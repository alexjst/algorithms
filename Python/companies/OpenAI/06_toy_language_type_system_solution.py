#!/usr/bin/env python3
"""Solution for Problem 6: Toy Language Type System"""

import re
from typing import List

class TypeSystem:
    def __init__(self):
        """
        Initialize the type system.

        TODO: Implement initialization
        Hints:
        1. Define valid primitives: {"int", "char", "float"}
        2. Generic pattern: uppercase letter + digits (T1, T2, ...)
        3. May want to track seen types for deduplication
        """
        pass

    def is_valid_type(self, type_str: str) -> bool:
        """
        Check if a type string is valid.

        TODO: Implement type validation
        Hints:
        1. Check if it's a primitive: type_str in {"int", "char", "float"}
        2. Check if it's a generic: matches pattern [A-Z]\d+
        3. Check if it's a tuple: starts with '(' and ends with ')'
           - For tuples, recursively validate inner types
        4. Use regex for generic: r'^[A-Z]\d+$'
        5. For tuple parsing, track parentheses depth

        Args:
            type_str: Type string to validate

        Returns:
            True if valid type, False otherwise
        """
        pass

    def process_types(self, types: List[str]) -> List[str]:
        """
        Process list of types, removing duplicates while preserving order.

        TODO: Implement type processing
        Hints:
        1. Iterate through types list
        2. Use set or dict to track seen types (for O(1) lookup)
        3. Maintain order by appending to result list only if not seen
        4. Validate each type before processing (optional)
        5. Return deduplicated list in original order

        Example:
            ["int", "char", "int"] -> ["int", "char"]
            ["T1", "T2", "T1"] -> ["T1", "T2"]
            ["(int, char)", "(int, char)"] -> ["(int, char)"]

        Args:
            types: List of type strings

        Returns:
            Deduplicated list of types in original order
        """
        pass

    def parse_tuple(self, type_str: str) -> List[str]:
        """
        Parse a tuple type into its component types.

        TODO: Implement tuple parsing (optional helper method)
        Hints:
        1. Remove outer parentheses: type_str[1:-1]
        2. Split by comma, but respect nested parentheses
        3. Track parentheses depth while iterating
        4. When depth is 0 and see comma, that's a separator
        5. Strip whitespace from each component

        Example:
            "(int, char)" -> ["int", "char"]
            "(int, (char, float))" -> ["int", "(char, float)"]
            "((int, char), T1)" -> ["(int, char)", "T1"]

        Args:
            type_str: Tuple type string

        Returns:
            List of component types
        """
        pass

    def _is_primitive(self, type_str: str) -> bool:
        """
        Helper: Check if type is a primitive.

        TODO: Implement primitive check
        Hints:
        1. Return type_str in {"int", "char", "float"}
        """
        pass

    def _is_generic(self, type_str: str) -> bool:
        """
        Helper: Check if type is a generic (T1, T2, etc).

        TODO: Implement generic check
        Hints:
        1. Use regex: r'^[A-Z]\d+$'
        2. Pattern means: start with uppercase letter, followed by 1+ digits
        3. Use re.match() or re.fullmatch()
        """
        pass

    def _is_tuple(self, type_str: str) -> bool:
        """
        Helper: Check if type is a tuple.

        TODO: Implement tuple check
        Hints:
        1. Check if starts with '(' and ends with ')'
        2. Optionally validate parentheses are balanced
        """
        pass
