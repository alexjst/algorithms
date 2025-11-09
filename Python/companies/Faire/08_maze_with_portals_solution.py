#!/usr/bin/env python3
"""
Solution for Problem 8: Maze with Portals

Asked 1-2 times at Faire

Problem: Find shortest path in a maze where you can use ONE portal for teleportation.

Similar to: "Shortest Path in Binary Matrix" + teleportation

TODO: Implement the function below.

Approach:
- BFS with state = (row, col, used_portal)
- Track visited positions including portal usage state
- Portal can teleport to any location
"""

from typing import List


def shortest_path_with_portals(maze: List[List[int]], portal_locations: List[tuple]) -> int:
    """
    Find shortest path from top-left to bottom-right using BFS.
    Can use ONE portal to teleport to any location.

    Args:
        maze: 2D grid where 0 = walkable, 1 = wall
        portal_locations: List of (row, col) tuples where portals exist

    Returns:
        Shortest path length, or -1 if no path exists

    Examples:
        >>> maze = [[0, 1, 0], [0, 0, 0], [1, 1, 0]]
        >>> portals = [(0, 0), (2, 2)]  # Can portal from (0,0) to (2,2)
        >>> shortest_path_with_portals(maze, portals)
        # Returns shortest path using at most one portal
    """
    # TODO: Implement BFS with portal usage
    # Hint:
    #   1. State = (row, col, portal_used: bool)
    #   2. From each position, can move 4 directions or use portal (if not used)
    #   3. If at portal location and haven't used it, can teleport to any other portal
    #   4. Track visited as set of (row, col, portal_used) tuples
    pass
