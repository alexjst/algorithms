#!/usr/bin/env python3
"""
Problem 2: Unix CD Command with Symbolic Links

Frequently asked OpenAI problem - simulate the Unix cd command.
Handle relative paths, absolute paths, symbolic links, and cycle detection.

Requirements:
- Implement cd(pwd, path) that returns new working directory
- Handle "." (current dir) and ".." (parent dir)
- Handle absolute paths (starting with "/")
- Handle symbolic links and detect cycles
- Return error/exception for invalid paths

Example:
    # File system with symbolic links
    symlinks = {
        "/a/link": "/b",
        "/c/link": "/a",
        "/cycle1": "/cycle2",
        "/cycle2": "/cycle1"
    }

    # Test cases
    cd("/a/b", "..")           # "/a"
    cd("/a/b", "../c")         # "/a/c"
    cd("/a/b", "/x/y")         # "/x/y" (absolute path)
    cd("/a", "link")           # "/b" (follow symlink)
    cd("/", "cycle1")          # Error (cycle detected)
    cd("/a/b", "../../..")     # "/" (root)
    cd("/a/b", "../../../..")  # "/" (can't go above root)

Time Complexity: O(n) where n is path length
Space Complexity: O(n) for path resolution and cycle detection
"""

try:
    import importlib.util
    spec = importlib.util.spec_from_file_location("solution_module",
                                                   "02_unix_cd_command_solution.py")
    solution_module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(solution_module)
    Solution = solution_module.Solution
except Exception as e:
    print(f"❌ Error importing solution: {e}")
    exit(1)

def test_cd_command():
    print("Testing Unix CD Command...")
    print()

    # Test 1: Basic relative paths
    print("Test 1: Relative paths with . and ..")
    solution1 = Solution({})
    assert solution1.cd("/a/b/c", "..") == "/a/b", "Test 1a failed"
    assert solution1.cd("/a/b/c", ".") == "/a/b/c", "Test 1b failed"
    assert solution1.cd("/a/b/c", "../..") == "/a", "Test 1c failed"
    print("✓ Test 1 passed")
    print()

    # Test 2: Absolute paths
    print("Test 2: Absolute paths")
    solution2 = Solution({})
    assert solution2.cd("/a/b/c", "/x/y/z") == "/x/y/z", "Test 2a failed"
    assert solution2.cd("/a/b", "/") == "/", "Test 2b failed"
    print("✓ Test 2 passed")
    print()

    # Test 3: Going above root
    print("Test 3: Cannot go above root")
    solution3 = Solution({})
    assert solution3.cd("/", "..") == "/", "Test 3a failed"
    assert solution3.cd("/a", "../../../..") == "/", "Test 3b failed"
    print("✓ Test 3 passed")
    print()

    # Test 4: Symbolic links
    print("Test 4: Symbolic link resolution")
    symlinks4 = {
        "/a/link": "/b/c",
        "/x/y": "/a"
    }
    solution4 = Solution(symlinks4)
    assert solution4.cd("/a", "link") == "/b/c", "Test 4a failed"
    assert solution4.cd("/x", "y/link") == "/b/c", "Test 4b failed"
    print("✓ Test 4 passed")
    print()

    # Test 5: Cycle detection
    print("Test 5: Detect symbolic link cycles")
    symlinks5 = {
        "/cycle1": "/cycle2",
        "/cycle2": "/cycle1"
    }
    solution5 = Solution(symlinks5)
    try:
        solution5.cd("/", "cycle1")
        assert False, "Test 5 failed: should detect cycle"
    except Exception as e:
        assert "cycle" in str(e).lower() or "error" in str(e).lower()
    print("✓ Test 5 passed")
    print()

    # Test 6: Mixed paths
    print("Test 6: Complex path resolution")
    symlinks6 = {"/a/link": "/b"}
    solution6 = Solution(symlinks6)
    assert solution6.cd("/a/x", "../link/../y") == "/b/y", "Test 6 failed"
    print("✓ Test 6 passed")
    print()

    print("All tests passed! ✓")

if __name__ == "__main__":
    test_cd_command()
