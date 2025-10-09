"""
Word Search - Backtracking in a 2D Grid

Problem: Given a 2D board and a word, find if the word exists in the grid.
The word can be constructed from letters of sequentially adjacent cells,
where "adjacent" cells are horizontally or vertically neighboring.
The same letter cell may not be used more than once.

Example:
board = [
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

word = "ABCCED" -> True
word = "SEE" -> True
word = "ABCB" -> False (can't reuse 'B')

This matches the backtracking template!
"""

def word_search(board, word):
    if not board or not board[0]:
        return False

    rows, cols = len(board), len(board[0])

    def backtrack(row, col, index):
        # row, col: Current position in grid
        # index: Current position in word we're matching
        # Returns True if we can find word[index:] starting from (row, col)

        # BASE CASE: Found complete word!
        if index == len(word):
            return True

        # VALIDITY CHECKS (is_valid in template)
        # Check boundaries
        if row < 0 or row >= rows or col < 0 or col >= cols:
            return False

        # Check if current cell matches current letter
        if board[row][col] != word[index]:
            return False

        # Check if already used (marked with '#')
        if board[row][col] == '#':
            return False

        # MAKE CHOICE: Mark this cell as used
        temp = board[row][col]
        board[row][col] = '#'  # Mark as visited

        # EXPLORE: Try all 4 directions (up, down, left, right)
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # right, down, left, up

        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            # Try to find rest of word from this direction
            if backtrack(new_row, new_col, index + 1):
                # Found it! Restore and return True
                board[row][col] = temp
                return True

        # BACKTRACK: Restore the cell (undo choice)
        board[row][col] = temp
        return False

    # Try starting from each cell in the grid
    for i in range(rows):
        for j in range(cols):
            if board[i][j] == word[0]:  # Optimization: only start if first letter matches
                if backtrack(i, j, 0):
                    return True

    return False


# Example 1: Simple grid
print("=" * 60)
print("Example 1: Simple Grid")
print("=" * 60)
board1 = [
    ['A', 'B', 'C', 'E'],
    ['S', 'F', 'C', 'S'],
    ['A', 'D', 'E', 'E']
]

print("\nBoard:")
for row in board1:
    print(" ".join(row))

test_words = ["ABCCED", "SEE", "ABCB", "ASADB"]
for word in test_words:
    result = word_search(board1, word)
    print(f"\nWord: '{word}' -> {result}")
    if result:
        print(f"  Path exists in grid!")

# Example 2: Trace execution for "SEE"
print("\n" + "=" * 60)
print("Example 2: Execution Trace for 'SEE'")
print("=" * 60)
print("\nBoard:")
for row in board1:
    print(" ".join(row))

print("\nSearching for 'SEE':")
print("""
Step-by-step:
1. Start at (1,0) = 'S' (index=0, matches 'S')
   Mark (1,0) as visited '#'

2. Try neighbors of (1,0):
   - Right (1,1) = 'F' (doesn't match 'E') ✗
   - Down (2,0) = 'A' (doesn't match 'E') ✗
   - Left: out of bounds ✗
   - Up (0,0) = 'A' (doesn't match 'E') ✗
   Backtrack: restore (1,0) = 'S'

3. Continue scanning... Find 'S' at (1,3)
   Mark (1,3) as visited '#'

4. Try neighbors of (1,3):
   - Right: out of bounds ✗
   - Down (2,3) = 'E' (matches 'E'!) ✓ (index=1)
     Mark (2,3) as visited '#'

5. From (2,3), looking for 'E' (index=2):
   - Right: out of bounds ✗
   - Down: out of bounds ✗
   - Left (2,2) = 'E' (matches 'E'!) ✓ (index=2)

6. index=3 == len('SEE') -> SUCCESS!

Path found: S(1,3) -> E(2,3) -> E(2,2)
""")

# Example 3: Visual representation
print("=" * 60)
print("Example 3: Visual Path for 'ABCCED'")
print("=" * 60)
print("""
Board:        Path:
A B C E       1 2 3 4
S F C S         6 5
A D E E

Path: A(0,0) -> B(0,1) -> C(0,2) -> C(1,2) -> E(2,2) -> D(2,1)
""")
