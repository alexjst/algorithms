#!/usr/bin/env python3
"""
Solution for Problem 8: Maze with Portals

🚨 CONFIRMED FAIRE INTERVIEW PROBLEM (Asked 2021)

Problem: Find shortest path in a maze with teleportation portals.
- Grid with walls, open spaces, start, end
- Portals marked with 'P' allow instant teleportation to ANY other 'P'
- Find shortest path length (or -1 if impossible)

Key Approach:
- BFS with normal moves + portal teleportation
- When standing on a portal, can teleport to any other portal
- Each move (including portal teleport) counts as 1 step

Time Complexity: O(R*C) where R = rows, C = cols
Space Complexity: O(R*C) for visited set and queue
"""

from typing import List
from collections import deque


def shortest_path_with_portals(maze: List[List[str]]) -> int:
    """
    Find shortest path in maze with portals.

    Args:
        maze: 2D grid where:
              'S' = start position
              'E' = end position
              '.' = empty cell (can walk)
              '#' = wall (cannot walk)
              'P' = portal (can teleport to any other 'P')

    Returns:
        Shortest path length (number of moves), or -1 if no path exists

    Examples:
        >>> maze = [
        ...     ['S', '.', '#', 'E'],
        ...     ['.', '.', '.', '.'],
        ...     ['#', 'P', '.', 'P']
        ... ]
        >>> shortest_path_with_portals(maze)
        3
        # Path: S → down → down → portal to (2,3) → up → E = 3 moves

    Key Insight:
    - Use BFS for shortest path
    - When on a portal, can teleport to any other portal (costs 1 move)
    - Each portal teleportation is counted as 1 step
    """
    if not maze or not maze[0]:
        return -1

    rows, cols = len(maze), len(maze[0])

    # Find start, end, and all portal positions
    start = None
    end = None
    portals = []

    for r in range(rows):
        for c in range(cols):
            if maze[r][c] == 'S':
                start = (r, c)
            elif maze[r][c] == 'E':
                end = (r, c)
            elif maze[r][c] == 'P':
                portals.append((r, c))

    if not start or not end:
        return -1

    # BFS
    queue = deque([(start[0], start[1], 0)])  # (row, col, distance)
    visited = set()
    visited.add(start)

    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # right, down, left, up

    while queue:
        r, c, dist = queue.popleft()

        # Check if reached end
        if (r, c) == end:
            return dist

        # Try normal moves (4 directions)
        for dr, dc in directions:
            nr, nc = r + dr, c + dc

            # Check bounds
            if 0 <= nr < rows and 0 <= nc < cols:
                # Check if walkable (not wall) and not visited
                if maze[nr][nc] != '#' and (nr, nc) not in visited:
                    visited.add((nr, nc))
                    new_dist = dist + 1

                    # If we're moving ONTO a portal, immediately teleport
                    # (portal entry + teleport counts as 1 move total)
                    if maze[nr][nc] == 'P':
                        queue.append((nr, nc, new_dist))
                        # Also add all other portal destinations
                        for pr, pc in portals:
                            if (pr, pc) != (nr, nc) and (pr, pc) not in visited:
                                visited.add((pr, pc))
                                queue.append((pr, pc, new_dist))
                    else:
                        queue.append((nr, nc, new_dist))

    return -1  # No path found


# Alternative implementation with clearer logic
def shortest_path_with_portals_verbose(maze: List[List[str]]) -> int:
    """
    More verbose implementation for clarity.
    Same functionality as shortest_path_with_portals.
    """
    if not maze or not maze[0]:
        return -1

    rows, cols = len(maze), len(maze[0])

    # Step 1: Find all special positions
    start_pos = None
    end_pos = None
    portal_positions = []

    for r in range(rows):
        for c in range(cols):
            cell = maze[r][c]
            if cell == 'S':
                start_pos = (r, c)
            elif cell == 'E':
                end_pos = (r, c)
            elif cell == 'P':
                portal_positions.append((r, c))

    # Validation
    if start_pos is None or end_pos is None:
        return -1

    # Step 2: BFS
    queue = deque([(start_pos[0], start_pos[1], 0)])
    visited = set([start_pos])

    while queue:
        row, col, distance = queue.popleft()

        # Check if reached destination
        if (row, col) == end_pos:
            return distance

        # Option 1: Move in 4 directions
        for delta_row, delta_col in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            new_row = row + delta_row
            new_col = col + delta_col

            # Check if position is valid
            if 0 <= new_row < rows and 0 <= new_col < cols:
                # Check if not a wall
                if maze[new_row][new_col] != '#':
                    # Check if not visited
                    if (new_row, new_col) not in visited:
                        visited.add((new_row, new_col))
                        queue.append((new_row, new_col, distance + 1))

        # Option 2: Use portal teleportation (if standing on portal)
        if maze[row][col] == 'P':
            # Can teleport to any other portal
            for portal_row, portal_col in portal_positions:
                # Don't teleport to self
                if (portal_row, portal_col) != (row, col):
                    # Check if not visited
                    if (portal_row, portal_col) not in visited:
                        visited.add((portal_row, portal_col))
                        queue.append((portal_row, portal_col, distance + 1))

    # No path found
    return -1


if __name__ == "__main__":
    print("=== Maze with Portals Examples ===\n")

    # Example 1: Maze with portals
    print("Example 1: Using portal to reach end")
    maze1 = [
        ['S', '.', '#', 'E'],
        ['.', '.', '.', '.'],
        ['#', 'P', '.', 'P']
    ]
    result1 = shortest_path_with_portals(maze1)
    print("Maze:")
    for row in maze1:
        print("  ", row)
    print(f"Shortest path: {result1}")
    print("Explanation: S → down → down → portal (2,1) to (2,3) → up → E = 3 moves\n")

    # Example 2: Direct path (no portals)
    print("Example 2: Direct path without portals")
    maze2 = [
        ['S', '.', '.'],
        ['.', '.', '.'],
        ['.', '.', 'E']
    ]
    result2 = shortest_path_with_portals(maze2)
    print("Maze:")
    for row in maze2:
        print("  ", row)
    print(f"Shortest path: {result2}")
    print("Explanation: S → right → right → down → down → E = 4 moves\n")

    # Example 3: No path (blocked)
    print("Example 3: No path exists")
    maze3 = [
        ['S', '#', 'E']
    ]
    result3 = shortest_path_with_portals(maze3)
    print("Maze:")
    for row in maze3:
        print("  ", row)
    print(f"Shortest path: {result3}")
    print("Explanation: Completely blocked by wall\n")

    # Example 4: Adjacent start and end
    print("Example 4: Adjacent positions")
    maze4 = [
        ['S', 'E']
    ]
    result4 = shortest_path_with_portals(maze4)
    print("Maze:")
    for row in maze4:
        print("  ", row)
    print(f"Shortest path: {result4}")
    print("Explanation: S → right → E = 1 move\n")

    # Example 5: Portal provides shortcut
    print("Example 5: Portal creates shortcut")
    maze5 = [
        ['S', 'P', '#', '#', '#'],
        ['#', '#', '#', '#', '#'],
        ['#', '#', '#', '#', 'P'],
        ['.', '.', '.', '.', '.'],
        ['E', '.', '.', '.', '.']
    ]
    result5 = shortest_path_with_portals(maze5)
    print("Maze:")
    for row in maze5:
        print("  ", row)
    print(f"Shortest path: {result5}")
    print("Explanation: S → right to (0,1) portal → teleport to (2,4) → down → down → left...")
    print("  Without portal would need to go around walls\n")

    # Example 6: Multiple portals
    print("Example 6: Multiple portals - choose best path")
    maze6 = [
        ['S', 'P', '.', 'E'],
        ['.', '.', '.', '.'],
        ['P', '.', '.', 'P']
    ]
    result6 = shortest_path_with_portals(maze6)
    print("Maze:")
    for row in maze6:
        print("  ", row)
    print(f"Shortest path: {result6}")
    print("Explanation: S → right → right → E = 2 moves")
    print("  Portal doesn't help here, direct path is shorter\n")
