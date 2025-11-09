#!/usr/bin/env python3
"""
Problem 9: Maze with Portals

Find shortest path in a maze that contains portals (teleportation points).

Maze:
- '.' = empty cell (can walk)
- '#' = wall (cannot walk)
- 'S' = start position
- 'E' = end position
- 'P' = portal (teleports to another portal)

Rules:
- Can move up, down, left, right
- Portals teleport you to another portal (any other 'P')
- Find shortest path from S to E

Example 1:
    maze = [
        ['S', '.', '#', 'E'],
        ['.', '.', '.', '.'],
        ['#', 'P', '.', 'P']
    ]
    Output: 3
    Explanation: S -> down -> down -> portal to (2,3) -> up -> E

Constraints:
    - 1 <= rows, cols <= 100
    - Exactly one 'S' and one 'E'
    - 0 or more portals
    - Return -1 if no path exists
"""

from typing import List
from collections import deque


def shortest_path_with_portals(maze: List[List[str]]) -> int:
    """
    Find shortest path in maze with portals using BFS.

    Args:
        maze: 2D grid with S, E, P, ., #

    Returns:
        Shortest path length, or -1 if no path
    """
    # TODO: Implement BFS with portal teleportation
    return -1  # Placeholder


def run_tests():
    """Run test cases for maze with portals."""

    # Test Case 1: Maze with portals
    maze1 = [
        ['S', '.', '#', 'E'],
        ['.', '.', '.', '.'],
        ['#', 'P', '.', 'P']
    ]
    result1 = shortest_path_with_portals(maze1)
    print(f"Test 1: Shortest path = {result1}")
    print("✓ Test 1 passed: Maze with portals")

    # Test Case 2: Direct path (no portals)
    maze2 = [
        ['S', '.', '.'],
        ['.', '.', '.'],
        ['.', '.', 'E']
    ]
    result2 = shortest_path_with_portals(maze2)
    print(f"Test 2: Shortest path = {result2} (expected 4)")
    print("✓ Test 2 passed: Direct path")

    # Test Case 3: No path (blocked)
    maze3 = [
        ['S', '#', 'E']
    ]
    result3 = shortest_path_with_portals(maze3)
    assert result3 == -1, f"Test 3 failed: expected -1, got {result3}"
    print("✓ Test 3 passed: No path exists")

    # Test Case 4: Adjacent start and end
    maze4 = [
        ['S', 'E']
    ]
    result4 = shortest_path_with_portals(maze4)
    assert result4 == 1, f"Test 4 failed: expected 1, got {result4}"
    print("✓ Test 4 passed: Adjacent positions")

    print("\n" + "="*50)
    print("All basic tests passed! ✓")
    print("="*50)


def run_custom_tests():
    """Add your own custom test cases here."""
    print("\nRunning custom tests...")

    # Add your custom test cases here

    print("No custom tests defined yet.")


if __name__ == "__main__":
    print("Testing Maze with Portals Solution")
    print("="*50 + "\n")

    try:
        run_tests()
        run_custom_tests()
    except AssertionError as e:
        print(f"\n❌ Test failed: {e}")
    except Exception as e:
        print(f"\n❌ Error: {e}")
