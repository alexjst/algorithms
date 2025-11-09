#!/usr/bin/env python3
"""
Solution for Problem 1: Metadata Lineage Graph

TODO: Implement the MetadataLineage class below.
"""

from typing import List, Dict, Set
from collections import defaultdict, deque

class MetadataLineage:
    """
    Track and query metadata lineage for datasets.
    """

    def __init__(self):
        """Initialize the lineage graph."""
        # TODO: Implement initialization
        # Hint: You'll need a graph structure to track dependencies
        pass

    def add_dependency(self, target: str, source: str) -> None:
        """
        Add a dependency relationship: target depends on source.

        Args:
            target: Dataset that depends on source
            source: Dataset that target depends on
        """
        # TODO: Implement adding dependency
        # Build adjacency list: source -> [targets that depend on source]
        pass

    def get_downstream(self, dataset: str) -> List[str]:
        """
        Get all datasets that transitively depend on the given dataset.

        Args:
            dataset: Source dataset name

        Returns:
            List of downstream dataset names
        """
        # TODO: Implement downstream traversal
        # Hints:
        # 1. Use BFS or DFS to traverse the graph
        # 2. Start from the given dataset
        # 3. Collect all reachable datasets
        # 4. Return in any order (or topological order for bonus)
        pass

    def has_circular_dependency(self) -> bool:
        """
        Check if there are any circular dependencies in the lineage graph.

        Returns:
            True if circular dependency exists, False otherwise
        """
        # TODO: Implement cycle detection
        # Hints:
        # 1. Use DFS with recursion stack
        # 2. Track visited nodes and nodes in current path
        # 3. If you revisit a node in current path, there's a cycle
        pass
