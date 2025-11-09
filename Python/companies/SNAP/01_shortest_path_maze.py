#!/usr/bin/env python3
"""
Problem 1: Shortest Path in Maze

SNAP commonly asks graph/maze problems for video game features and AR navigation.
Implement a system to find shortest paths in grids with obstacles and wall-breaking.

Requirements:
- Find shortest path from start to end in a 0/1 grid
- 0 = walkable road, 1 = wall/obstacle
- Support wall-breaking with additional cost
- Return minimum cost/distance

Example 1 - Basic shortest path:
    grid = [
        [0, 0, 1, 0],
        [0, 1, 0, 0],
        [0, 0, 0, 1],
        [1, 0, 0, 0]
    ]
    solver = MazeSolver()
    distance = solver.shortest_path(grid, start=(0,0), end=(3,3))
    # Returns: 6 (minimum steps)

Example 2 - With wall breaking:
    Same grid as above
    distance = solver.shortest_path_with_breaking(grid, start=(0,0), end=(3,3))
    # Returns: 5 (can break through one wall for shorter path)
    # Walk cost=1, Break cost=1

Time Complexity: O(R × C) for BFS, O(R × C × log(R × C)) for Dijkstra
Space Complexity: O(R × C)
"""

# Import the solution
try:
    import importlib.util
    spec = importlib.util.spec_from_file_location(
        "solution_module",
        "01_shortest_path_maze_solution.py"
    )
    solution_module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(solution_module)
    MazeSolver = solution_module.MazeSolver
except Exception as e:
    print(f"❌ Error importing solution: {e}")
    print(f"   Make sure 01_shortest_path_maze_solution.py exists.")
    exit(1)

def test_maze_solver():
    """Test the maze solver implementation."""

    print("Testing Shortest Path in Maze...")
    print()

    # Test 1: Basic shortest path without obstacles
    print("Test 1: Basic shortest path without obstacles")
    solver1 = MazeSolver()
    grid1 = [
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0]
    ]
    result1 = solver1.shortest_path(grid1, start=(0,0), end=(2,3))
    assert result1 == 5, f"Test 1 failed: expected 5, got {result1}"
    print("✓ Test 1 passed: Basic shortest path works")
    print()

    # Test 2: Path blocked by walls
    print("Test 2: Path with obstacles")
    solver2 = MazeSolver()
    grid2 = [
        [0, 0, 1, 0],
        [0, 1, 0, 0],
        [0, 0, 0, 1],
        [1, 0, 0, 0]
    ]
    result2 = solver2.shortest_path(grid2, start=(0,0), end=(3,3))
    assert result2 == 6, f"Test 2 failed: expected 6, got {result2}"
    print("✓ Test 2 passed: Navigates around obstacles")
    print()

    # Test 3: No path exists
    print("Test 3: No path exists")
    solver3 = MazeSolver()
    grid3 = [
        [0, 1, 0],
        [1, 1, 1],
        [0, 1, 0]
    ]
    result3 = solver3.shortest_path(grid3, start=(0,0), end=(2,2))
    assert result3 == -1, f"Test 3 failed: expected -1, got {result3}"
    print("✓ Test 3 passed: Returns -1 when no path exists")
    print()

    # Test 4: Wall breaking - shorter path available
    print("Test 4: Wall breaking allows shorter path")
    solver4 = MazeSolver()
    grid4 = [
        [0, 1, 0],
        [0, 1, 0],
        [0, 0, 0]
    ]
    result4_no_break = solver4.shortest_path(grid4, start=(0,0), end=(0,2))
    result4_with_break = solver4.shortest_path_with_breaking(grid4, start=(0,0), end=(0,2))
    assert result4_no_break == 4, f"Test 4a failed: expected 4 without breaking, got {result4_no_break}"
    assert result4_with_break == 3, f"Test 4b failed: expected 3 with breaking, got {result4_with_break}"
    print("✓ Test 4 passed: Wall breaking finds shorter path")
    print()

    # Test 5: Large grid performance
    print("Test 5: Large grid performance")
    solver5 = MazeSolver()
    n = 50
    grid5 = [[0 for _ in range(n)] for _ in range(n)]
    # Add some obstacles
    for i in range(10, 40):
        grid5[i][25] = 1
    result5 = solver5.shortest_path(grid5, start=(0,0), end=(n-1,n-1))
    assert result5 > 0, f"Test 5 failed: should find a path in large grid"
    print(f"  Path length in {n}x{n} grid: {result5}")
    print("✓ Test 5 passed: Handles large grids efficiently")
    print()

    # Test 6: Wall breaking with cost optimization
    print("Test 6: Minimum cost with wall breaking")
    solver6 = MazeSolver()
    grid6 = [
        [0, 1, 1, 0],
        [0, 1, 1, 0],
        [0, 0, 0, 0]
    ]
    result6 = solver6.shortest_path_with_breaking(grid6, start=(0,0), end=(0,3))
    # Breaking 1 wall: cost = 2 (walk) + 1 (break) = 3
    # Going around: cost = 6 (walk only)
    assert result6 == 3, f"Test 6 failed: expected minimum cost 3, got {result6}"
    print("✓ Test 6 passed: Optimizes cost with wall breaking")
    print()

    print("All tests passed! ✓")

if __name__ == "__main__":
    test_maze_solver()
