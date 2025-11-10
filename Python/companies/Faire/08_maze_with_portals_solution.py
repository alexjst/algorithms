#!/usr/bin/env python3
"""
Solution for Problem 8: Maze with Portals

🚨 Asked 2+ times at Faire

Problem: Find shortest path in a maze with teleportation portals.
- Grid with walls, open spaces, start, end
- Portals allow instant teleportation between two locations
- Find shortest path length (or -1 if impossible)

Similar to: BFS shortest path + state tracking

Key Approach:
- BFS with state = (row, col, portal_used)
- Portal usage tracking: can use each portal at most once per path
- Portal is bidirectional: A→B or B→A (but only once)
- Distance = number of moves (portal teleport counts as 1 move)
"""

from typing import List, Tuple, Set, Dict
from collections import deque


def shortest_path_with_portals(
    grid: List[List[str]],
    portals: List[Tuple[Tuple[int, int], Tuple[int, int]]]
) -> int:
    """
    Find shortest path in maze with portals.

    Args:
        grid: 2D grid where:
              'S' = start
              'E' = end
              '#' = wall
              '.' = open space
        portals: List of portal pairs [(from, to), ...]
                 Each portal is bidirectional
                 Format: [((r1, c1), (r2, c2)), ...]

    Returns:
        Shortest path length, or -1 if no path exists

    Examples:
        >>> grid = [
        ...     ['S', '.', '.', '#', 'E'],
        ...     ['#', '#', '.', '#', '.'],
        ...     ['.', '.', '.', '.', '.']
        ... ]
        >>> portals = [((0, 1), (2, 4))]  # Portal from (0,1) to (2,4)
        >>> shortest_path_with_portals(grid, portals)
        3  # S→(0,1)→portal→(2,4)→E

    Key Insight:
    - State = (row, col, portal_used_set)
    - Portal can be used in either direction
    - Each portal can only be used once per path
    - BFS ensures shortest path

    Time: O(R*C*2^P) where P = number of portals (worst case)
          In practice, much better due to pruning
    Space: O(R*C*2^P) for visited states
    """
    if not grid or not grid[0]:
        return -1

    rows, cols = len(grid), len(grid[0])

    # Find start and end positions
    start, end = None, None
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 'S':
                start = (r, c)
            elif grid[r][c] == 'E':
                end = (r, c)

    if not start or not end:
        return -1

    # Build portal lookup: position → list of connected portals
    portal_map = {}  # {(r, c): [(dest, portal_id), ...]}
    for portal_id, (pos1, pos2) in enumerate(portals):
        # Bidirectional
        if pos1 not in portal_map:
            portal_map[pos1] = []
        portal_map[pos1].append((pos2, portal_id))

        if pos2 not in portal_map:
            portal_map[pos2] = []
        portal_map[pos2].append((pos1, portal_id))

    # BFS with state = (row, col, used_portals_frozenset)
    # Using frozenset to make it hashable for visited tracking
    queue = deque([(start[0], start[1], frozenset(), 0)])  # (r, c, used_portals, distance)
    visited = set()
    visited.add((start[0], start[1], frozenset()))

    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # right, down, left, up

    while queue:
        r, c, used_portals, dist = queue.popleft()

        # Check if reached end
        if (r, c) == end:
            return dist

        # Try normal moves (4 directions)
        for dr, dc in directions:
            nr, nc = r + dr, c + dc

            # Check bounds and walls
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] != '#':
                state = (nr, nc, used_portals)
                if state not in visited:
                    visited.add(state)
                    queue.append((nr, nc, used_portals, dist + 1))

        # Try portal moves
        if (r, c) in portal_map:
            for dest, portal_id in portal_map[(r, c)]:
                # Check if portal not already used
                if portal_id not in used_portals:
                    dr, dc = dest
                    new_used = used_portals | {portal_id}  # Add portal to used set
                    state = (dr, dc, new_used)

                    if state not in visited:
                        visited.add(state)
                        queue.append((dr, dc, new_used, dist + 1))

    return -1  # No path found


def shortest_path_simple(grid: List[List[str]], portals: List[Tuple[Tuple[int, int], Tuple[int, int]]]) -> int:
    """
    Simplified version assuming each portal can be used unlimited times.
    This is easier to implement but may not match problem requirements.

    Use shortest_path_with_portals() for the correct solution where
    portals can only be used once per path.
    """
    if not grid or not grid[0]:
        return -1

    rows, cols = len(grid), len(grid[0])

    # Find start and end
    start, end = None, None
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 'S':
                start = (r, c)
            elif grid[r][c] == 'E':
                end = (r, c)

    if not start or not end:
        return -1

    # Build portal map
    portal_map = {}
    for pos1, pos2 in portals:
        if pos1 not in portal_map:
            portal_map[pos1] = []
        portal_map[pos1].append(pos2)

        if pos2 not in portal_map:
            portal_map[pos2] = []
        portal_map[pos2].append(pos1)

    # Simple BFS without portal usage tracking
    queue = deque([(start[0], start[1], 0)])
    visited = set()
    visited.add((start[0], start[1]))

    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    while queue:
        r, c, dist = queue.popleft()

        if (r, c) == end:
            return dist

        # Normal moves
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] != '#':
                if (nr, nc) not in visited:
                    visited.add((nr, nc))
                    queue.append((nr, nc, dist + 1))

        # Portal moves
        if (r, c) in portal_map:
            for dr, dc in portal_map[(r, c)]:
                if (dr, dc) not in visited:
                    visited.add((dr, dc))
                    queue.append((dr, dc, dist + 1))

    return -1


if __name__ == "__main__":
    print("=== Maze with Portals Examples ===\n")

    # Example 1: Simple portal shortcut
    print("Example 1: Simple portal shortcut")
    grid1 = [
        ['S', '.', '.', '#', 'E'],
        ['#', '#', '.', '#', '.'],
        ['.', '.', '.', '.', '.']
    ]
    portals1 = [((0, 1), (2, 4))]  # Portal near start to near end
    result1 = shortest_path_with_portals(grid1, portals1)
    print("Grid:")
    for row in grid1:
        print("  ", row)
    print(f"Portals: {portals1}")
    print(f"Shortest path: {result1}")
    print("Explanation: S→(0,1)→portal→(2,4)→E = 3 moves\n")

    # Example 2: No portal needed
    print("Example 2: Direct path is shorter")
    grid2 = [
        ['S', '.', 'E'],
        ['.', '.', '.'],
    ]
    portals2 = [((1, 0), (1, 2))]  # Portal doesn't help
    result2 = shortest_path_with_portals(grid2, portals2)
    print("Grid:")
    for row in grid2:
        print("  ", row)
    print(f"Portals: {portals2}")
    print(f"Shortest path: {result2}")
    print("Explanation: S→(0,1)→E = 2 moves (portal not needed)\n")

    # Example 3: Multiple portals
    print("Example 3: Multiple portals")
    grid3 = [
        ['S', '.', '#', '#', '#'],
        ['.', '.', '#', 'E', '#'],
        ['#', '#', '#', '.', '.']
    ]
    portals3 = [
        ((0, 1), (2, 4)),  # Portal 1
        ((2, 4), (1, 3))   # Portal 2
    ]
    result3 = shortest_path_with_portals(grid3, portals3)
    print("Grid:")
    for row in grid3:
        print("  ", row)
    print(f"Portals: {portals3}")
    print(f"Shortest path: {result3}")
    print("Explanation: S→(0,1)→portal1→(2,4)→portal2→(1,3) = 3 moves\n")

    # Example 4: No path
    print("Example 4: No path exists")
    grid4 = [
        ['S', '#', 'E'],
        ['#', '#', '#'],
    ]
    portals4 = []
    result4 = shortest_path_with_portals(grid4, portals4)
    print("Grid:")
    for row in grid4:
        print("  ", row)
    print(f"Portals: {portals4}")
    print(f"Shortest path: {result4}")
    print("Explanation: Completely blocked by walls\n")

    # Example 5: Portal vs normal path choice
    print("Example 5: Choose between portal and normal path")
    grid5 = [
        ['S', '.', '.', '.', 'E'],
        ['.', '.', '.', '.', '.'],
    ]
    portals5 = [((0, 1), (1, 4))]
    result5 = shortest_path_with_portals(grid5, portals5)
    print("Grid:")
    for row in grid5:
        print("  ", row)
    print(f"Portals: {portals5}")
    print(f"Shortest path: {result5}")
    print("Explanation:")
    print("  Normal path: S→(0,1)→(0,2)→(0,3)→E = 4 moves")
    print("  Portal path: S→(0,1)→portal→(1,4)→(0,4)=E = 3 moves")
    print("  BFS chooses portal path!\n")
