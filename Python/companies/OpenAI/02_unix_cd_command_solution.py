#!/usr/bin/env python3
"""Solution for Problem 2: Unix CD Command"""

from typing import Dict

class Solution:
    def __init__(self, symlinks: Dict[str, str]):
        """
        Initialize with symbolic link mappings.

        Args:
            symlinks: Dict mapping symlink paths to target paths
        """
        self.symlinks = symlinks

    def cd(self, pwd: str, path: str) -> str:
        """
        Simulate cd command with symbolic link support.

        TODO: Implement cd command
        Hints:
        1. If path starts with "/", it's absolute (ignore pwd)
        2. Otherwise, start from pwd
        3. Split path by "/" and process each component
        4. Use stack to track directory path:
           - "." : do nothing
           - ".." : pop from stack (if not at root)
           - else : push to stack
        5. After building path, check for symlinks
        6. Use DFS/visited set to detect cycles
        7. Join stack with "/" to form final path

        Args:
            pwd: Current working directory
            path: Path to change to (relative or absolute)

        Returns:
            New working directory path

        Raises:
            Exception: If symbolic link cycle detected
        """
        pass
