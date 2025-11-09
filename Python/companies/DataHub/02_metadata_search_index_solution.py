#!/usr/bin/env python3
"""
Solution for Problem 2: Metadata Search Index

TODO: Implement the MetadataSearchIndex class below.
"""

from typing import List, Dict, Set

class MetadataSearchIndex:
    """
    Search index for dataset metadata with prefix matching and relevance ranking.
    """

    def __init__(self):
        """Initialize the search index."""
        # TODO: Implement initialization
        # You'll need to store:
        # - Dataset metadata (name, description, tags)
        # - Index structures for efficient search
        pass

    def add_dataset(self, name: str, description: str, tags: List[str]) -> None:
        """
        Add a dataset to the search index.

        Args:
            name: Dataset name
            description: Dataset description
            tags: List of tags associated with the dataset
        """
        # TODO: Implement dataset indexing
        # Store the dataset and build search index
        pass

    def search(self, query: str, k: int) -> List[str]:
        """
        Search for datasets matching the query prefix.

        Args:
            query: Search query (prefix)
            k: Maximum number of results to return

        Returns:
            List of dataset names, ranked by relevance
        """
        # TODO: Implement search
        # Hints:
        # 1. Find all datasets where name/tags/description contains the query
        # 2. Rank by relevance:
        #    - Exact name match = highest score
        #    - Name prefix match = high score
        #    - Tag match = medium score
        #    - Description match = lower score
        # 3. Return top K results
        pass
