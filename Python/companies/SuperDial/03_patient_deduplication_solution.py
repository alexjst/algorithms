#!/usr/bin/env python3
"""
Solution for Problem 3: Patient Data Deduplication

TODO: Implement the PatientDeduplicator class below.
"""

from typing import List, Dict, Set

class PatientDeduplicator:
    """
    Detect duplicate patient records using fuzzy matching.

    Args:
        name_threshold: Maximum Levenshtein distance for name matching (default: 3)
    """

    def __init__(self, name_threshold: int = 3):
        """Initialize the deduplicator."""
        # TODO: Implement initialization
        pass

    def find_duplicates(self, patients: List[Dict[str, str]]) -> List[List[int]]:
        """
        Find groups of duplicate patient records.

        Args:
            patients: List of patient dictionaries with 'id', 'name', 'phone' keys

        Returns:
            List of lists, where each inner list contains indices of duplicate patients
        """
        # TODO: Implement duplicate detection
        # Hints:
        # 1. Use Union-Find or grouping to track duplicate groups
        # 2. Compare each pair of patients
        # 3. Mark as duplicate if:
        #    - Same patient ID, OR
        #    - Same phone number, OR
        #    - Similar names (use levenshtein_distance helper)
        # 4. Return groups of duplicate indices
        pass

    def levenshtein_distance(self, s1: str, s2: str) -> int:
        """
        Calculate Levenshtein distance between two strings.

        Args:
            s1: First string
            s2: Second string

        Returns:
            Edit distance between strings
        """
        # TODO: Implement Levenshtein distance
        # Hint: Use dynamic programming
        # dp[i][j] = min edit distance between s1[:i] and s2[:j]
        pass
