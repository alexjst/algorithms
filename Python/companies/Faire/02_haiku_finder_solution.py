#!/usr/bin/env python3
"""
Solution for Problem 2: Haiku Finder (Find First Haiku in Sentence)

🚨 ACTUAL FAIRE INTERVIEW PROBLEM - Asked 5+ times (2021-2025)

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

        Example: ["a Simple flower", "Petals shine Vibrant don't Pure", "Stares into Void."]

    Time Complexity: O(n) with prefix sums and hash map
    Space Complexity: O(n) for storing words and prefix sums

    Examples:
        >>> sentence = "a Simple flower Petals shine Vibrant"
        >>> syllable_dict = {"a": 1, "simple": 2, "flower": 2, "petals": 2, "shine": 1, "vibrant": 2}
        >>> find_haiku(sentence, syllable_dict)
        # Should return 3-line haiku if pattern exists
    """
    # TODO: Implement your solution here
    # Hint: Use prefix sums + hash map for O(n) solution
    # Remember to:
    #   - Strip punctuation before lookup (word.strip(string.punctuation))
    #   - Lowercase for lookup (.lower())
    #   - Preserve original formatting in output
    #   - Return None if no haiku found
    #   - Find positions where sum = start + 5, start + 12, start + 17
    
    """
    Assumptions:
        - dictionary is comprehensive (not missing entries to handle every word)
        - case-insensitive
        - input sentence can be 'noisy' -> upper and lower cases, punctuations 
        - only need to find the first solution

    How:
        - split the sentence, normalize words: lowercase, strip punctuations
            - get original word array ['Hello', 'World!'] for building the final result
            - get normlized word array ["hello', 'world', ..]
            - get syllable count array [2, 1, 1, 3, ....]
                - prefix sum array ([0]) [2, 3, 4, 7, ....]
                - build a hashmap from prefix sum to index {0:0,       2:1, 3:2, 4:3, 7:4, ...}

        - scan the syllable count array, staring from prefix sum = 0, find sum+5, sum+12, sum+17.
            - if all are found: can find range of each part.
                - map back to original word array, join to build the result
    """
    if not sentence:
        return None

    original_words = sentence.split(" ")
    normalized_words = [w.strip(string.punctuation).lower() for w in original_words if w]

    # here we assume the dictionary is comprehensive
    syllable_counts = [syllable_dict.get(w) for w in normalized_words]
    if None in syllable_counts:
        return None

    prefix_sum = [0]
    for count in syllable_counts:
        prefix_sum.append(prefix_sum[-1] + count)

    prefix_sum_to_index = {}
    for i, sum in enumerate(prefix_sum):
        prefix_sum_to_index[sum] = i

    n = len(prefix_sum)
    for i in range(n-3):
        if prefix_sum[i] + 5 in prefix_sum_to_index and prefix_sum[i] + 12 in prefix_sum_to_index and prefix_sum[i] + 17 in prefix_sum_to_index:
            first = prefix_sum_to_index[prefix_sum[i] + 5]
            sentence1 = " ".join(original_words[i:first])
            second = prefix_sum_to_index[prefix_sum[i] + 12]
            sentence2 = " ".join(original_words[first:second])
            third = prefix_sum_to_index[prefix_sum[i] + 17]
            sentence3 = " ".join(original_words[second:third])
            return [sentence1, sentence2, sentence3]
    return None

