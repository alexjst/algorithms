#!/usr/bin/env python3
"""
Solution for Problem 3: Haiku Finder (Find First Haiku in Sentence)

This is the ACTUAL Faire interview problem from 1point3acres.com reports (2021-2025).
Multiple candidates confirmed this exact problem was asked.

Problem: Given a sentence with mixed case and punctuation, and a syllable dictionary,
find the FIRST haiku (consecutive words forming 5-7-5 syllable pattern).

TODO: Implement the function below.

Approach Hints:
1. Brute force O(n²) or O(n³): Try all possible starting positions and word combinations
2. Optimal O(n): Use prefix sums + hash map for O(1) lookups

Key Implementation Details:
- Strip punctuation from words before dictionary lookup (use string.punctuation)
- Convert to lowercase for lookup
- Preserve original case and punctuation in output
- Return None if no haiku found
- Return FIRST (leftmost) haiku if multiple exist
"""

from typing import List, Dict, Optional
import string


def find_haiku(sentence: str, syllable_dict: Dict[str, int]) -> Optional[List[str]]:
    """
    Find the first haiku (5-7-5 syllable pattern) in a sentence.

    Args:
        sentence: A string with words separated by spaces, may contain mixed case
                 and punctuation (e.g., "Hello, World! Nice day.")
        syllable_dict: Dictionary mapping lowercase words to syllable counts
                      (e.g., {"hello": 2, "world": 1, "nice": 1, "day": 1})

    Returns:
        List of 3 strings representing the haiku lines, preserving original case
        and punctuation, or None if no valid haiku is found.

        Example return: ["a Simple flower", "Petals shine Vibrant don't Pure", "Stares into Void."]

    Time Complexity:
        - Brute force: O(n²) or O(n³)
        - Optimal: O(n) with prefix sums and hash map

    Space Complexity: O(n) for storing words and prefix sums
    """
    # Edge case: empty sentence
    if not sentence:
        return None

    # Step 1: Split sentence into words (preserve original formatting)
    words = sentence.split()
    if len(words) < 3:  # Need at least 3 words for a haiku
        return None

    # Step 2: Build syllable counts for each word
    syllables = []
    for word in words:
        # Strip punctuation and convert to lowercase for lookup
        # "Void." → "void", "don't" → "dont"
        clean_word = word.strip(string.punctuation).lower()
        syl_count = syllable_dict.get(clean_word, 0)
        syllables.append(syl_count)

    # Step 3: Build prefix sum array
    # prefix_sums[i] = total syllables from word 0 to word i-1
    # Example: syllables = [8, 1, 2, 2, 2, 1, 2, 1, 1, 2, 2, 1]
    #          prefix = [0, 8, 9, 11, 13, 15, 16, 18, 19, 20, 22, 24, 25]
    prefix_sums = [0]
    for syl in syllables:
        prefix_sums.append(prefix_sums[-1] + syl)

    # Step 4: Create hash map: sum -> index
    # We reverse to get the rightmost index for each sum value (handles duplicates)
    sum_to_index = {}
    for i in range(len(prefix_sums) - 1, -1, -1):
        sum_to_index[prefix_sums[i]] = i

    # Step 5: Try each starting position to find 5-7-5 pattern
    for i in range(len(prefix_sums)):
        start_sum = prefix_sums[i]

        # Look for positions where we have:
        # - 5 syllables after start (sum = start + 5)
        # - 7 more syllables (sum = start + 12)
        # - 5 more syllables (sum = start + 17)
        target_sum1 = start_sum + 5   # End of line 1
        target_sum2 = start_sum + 12  # End of line 2 (5 + 7)
        target_sum3 = start_sum + 17  # End of line 3 (5 + 7 + 5)

        end_index1 = sum_to_index.get(target_sum1)
        end_index2 = sum_to_index.get(target_sum2)
        end_index3 = sum_to_index.get(target_sum3)

        # Check if all three endpoints exist and are in correct order
        if (end_index1 is not None and
            end_index2 is not None and
            end_index3 is not None and
            i < end_index1 < end_index2 < end_index3):

            # Found a haiku! Reconstruct with original formatting
            # IMPORTANT: Use original words to preserve case and punctuation
            line1 = " ".join(words[i:end_index1])
            line2 = " ".join(words[end_index1:end_index2])
            line3 = " ".join(words[end_index2:end_index3])

            return [line1, line2, line3]

    # No valid haiku found
    return None


# Example implementation (commented out - try to implement yourself first!)
"""
def find_haiku_optimized(sentence: str, syllable_dict: Dict[str, int]) -> Optional[List[str]]:
    if not sentence:
        return None

    words = sentence.split()
    if len(words) < 3:
        return None

    # Build syllable counts for each word
    syllables = []
    for word in words:
        # Strip punctuation and convert to lowercase for lookup
        clean_word = word.strip(string.punctuation).lower()
        syl_count = syllable_dict.get(clean_word, 0)
        syllables.append(syl_count)

    # Build prefix sum array
    prefix_sums = [0]
    for syl in syllables:
        prefix_sums.append(prefix_sums[-1] + syl)

    # Create hash map: sum -> first index with that sum
    # We reverse to get the first occurrence for each sum value
    sum_to_index = {}
    for i in range(len(prefix_sums) - 1, -1, -1):
        sum_to_index[prefix_sums[i]] = i

    # Try each starting position
    for i in range(len(prefix_sums)):
        start_sum = prefix_sums[i]

        # Look for 5-7-5 pattern
        target_sum1 = start_sum + 5
        target_sum2 = start_sum + 12  # 5 + 7
        target_sum3 = start_sum + 17  # 5 + 7 + 5

        end_index1 = sum_to_index.get(target_sum1)
        end_index2 = sum_to_index.get(target_sum2)
        end_index3 = sum_to_index.get(target_sum3)

        # Check if all three endpoints exist and are in correct order
        if (end_index1 is not None and
            end_index2 is not None and
            end_index3 is not None and
            i < end_index1 <= end_index2 <= end_index3):

            # Found a haiku! Reconstruct with original formatting
            line1 = " ".join(words[i:end_index1])
            line2 = " ".join(words[end_index1:end_index2])
            line3 = " ".join(words[end_index2:end_index3])

            return [line1, line2, line3]

    return None
"""
