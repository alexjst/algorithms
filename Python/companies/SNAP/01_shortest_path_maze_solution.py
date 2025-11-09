#!/usr/bin/env python3
"""
Solution for Problem 1: Shortest Path in Maze

TODO: Implement the MazeSolver class below.
"""

from typing import List, Tuple
from collections import deque
import heapq

class MazeSolver:
    """
    Solve shortest path problems in 2D grids with obstacles.
    """

    def shortest_path(self, grid: List[List[int]], start: Tuple[int, int],
                      end: Tuple[int, int]) -> int:
        """
        Find shortest path from start to end without breaking walls.

        Args:
            grid: 2D grid where 0=walkable, 1=wall
            start: Starting position (row, col)
            end: Ending position (row, col)

        Returns:
            Minimum distance from start to end, or -1 if no path exists
        """
        # TODO: Implement BFS shortest path
        # Hints:
        # 1. Use BFS with deque for level-order traversal
        # 2. Track visited cells to avoid cycles
        # 3. Move in 4 directions: up, down, left, right
        # 4. Return distance when reaching end
        # 5. Return -1 if queue empties without finding path
        pass

    def shortest_path_with_breaking(self, grid: List[List[int]],
                                     start: Tuple[int, int],
                                     end: Tuple[int, int]) -> int:
        """
        Find shortest path with ability to break walls (cost=1 per wall).

        Args:
            grid: 2D grid where 0=walkable, 1=wall
            start: Starting position (row, col)
            end: Ending position (row, col)

        Returns:
            Minimum cost from start to end
        """
        # TODO: Implement Dijkstra's algorithm for minimum cost path
        # Hints:
        # 1. Use min-heap with (cost, row, col) tuples
        # 2. Track minimum cost to reach each cell
        # 3. Walking on 0 costs 1, walking on 1 (breaking) costs 1
        # 4. Total cost = distance + walls broken
        # 5. Use dictionary to track best cost to each cell
        #
        # Example structure:
        # heap = [(0, start[0], start[1])]  # (cost, row, col)
        # visited = {}
        # while heap:
        #     cost, r, c = heapq.heappop(heap)
        #     if (r, c) == end:
        #         return cost
        #     ...
        pass
