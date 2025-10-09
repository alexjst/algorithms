# Word Search - Template Mapping

## How Word Search Maps to Backtracking Template

### Original Template
```python
def backtrack(path, remaining_choices):
    if is_solution(path):
        result.append(path[:])
        return

    for choice in remaining_choices:
        if is_valid(choice, path):
            path.append(choice)
            backtrack(path, new_remaining)
            path.pop()
```

### Word Search Implementation
```python
def backtrack(row, col, index):
    # is_solution: Have we matched the entire word?
    if index == len(word):
        return True

    # is_valid: Multiple checks
    if row < 0 or row >= rows or col < 0 or col >= cols:
        return False
    if board[row][col] != word[index]:
        return False
    if board[row][col] == '#':  # Already used
        return False

    # Make choice: Mark cell as used
    temp = board[row][col]
    board[row][col] = '#'

    # Explore choices: Try all 4 directions
    for dr, dc in [(0,1), (1,0), (0,-1), (-1,0)]:
        if backtrack(row + dr, col + dc, index + 1):
            board[row][col] = temp  # Restore before success
            return True

    # Backtrack: Restore cell
    board[row][col] = temp
    return False
```

## Variable Mapping

| Template Variable | Word Search Equivalent | Example Value |
|------------------|------------------------|---------------|
| `path` | Not explicit (implicit in recursion) | Letters matched so far |
| `remaining_choices` | 4 directions: up/down/left/right | [(0,1), (1,0), (0,-1), (-1,0)] |
| `is_solution()` | `index == len(word)` | Found all letters |
| `is_valid()` | Multiple checks | Bounds, letter match, not visited |
| `path.append()` | `board[row][col] = '#'` | Mark as visited |
| `path.pop()` | `board[row][col] = temp` | Restore original value |

## Key Differences from Permutations/Subsets

### 1. **State is in the Grid**
- Permutations: `path = [1, 2]`
- Word Search: `board[row][col] = '#'` (modify in-place)

### 2. **Choices are Directions**
- Permutations: Choose from remaining numbers
- Word Search: Choose from 4 directions (up/down/left/right)

### 3. **Multiple is_valid Checks**
```python
# Boundary check
if row < 0 or row >= rows or col < 0 or col >= cols:
    return False

# Letter match check
if board[row][col] != word[index]:
    return False

# Already visited check
if board[row][col] == '#':
    return False
```

### 4. **Early Return on Success**
- Permutations: Collect all solutions
- Word Search: Return True as soon as one path found

## Visual Example: Finding "CAT"

```
Board:
C A R
A T S
B E D

Looking for: "CAT"

Step 1: Start at C(0,0), index=0
  Mark: # A R
        A T S
        B E D

Step 2: Try neighbors for 'A' (index=1)
  - Right: A(0,1) ✓ matches!
  Mark: # # R
        A T S
        B E D

Step 3: Try neighbors for 'T' (index=2)
  - Down: T(1,1) ✓ matches!
  Mark: # # R
        A # S
        B E D

Step 4: index=3 == len("CAT") -> SUCCESS!

Path: C(0,0) -> A(0,1) -> T(1,1)
```

## Common Gotchas

### 1. **Forgetting to Restore on Success**
```python
# WRONG
if backtrack(new_row, new_col, index + 1):
    return True  # Forgot to restore!

# CORRECT
if backtrack(new_row, new_col, index + 1):
    board[row][col] = temp  # Restore before returning
    return True
```

### 2. **Using the Same Cell Twice**
```python
# Mark as visited BEFORE recursing
board[row][col] = '#'

# Try neighbors
if backtrack(...):
    # ...

# Restore AFTER all attempts
board[row][col] = temp
```

### 3. **Direction Array Format**
```python
# (row_delta, col_delta)
directions = [
    (0, 1),   # Right: same row, col+1
    (1, 0),   # Down: row+1, same col
    (0, -1),  # Left: same row, col-1
    (-1, 0)   # Up: row-1, same col
]
```

## Complexity

- **Time**: O(N × 4^L)
  - N = number of cells in grid
  - L = length of word
  - Each cell tries 4 directions, up to L times

- **Space**: O(L)
  - Recursion depth = word length
