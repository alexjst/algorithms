# Backtracking Visual Explanation

## The Decision Tree

When generating permutations of [1,2,3], backtracking explores like this:

```
                    [] (start)
                   /  |  \
                  /   |   \
                 1    2    3
                / \   |   / \
               2   3  1 3  1  2
              /     \ |/   |\  \
             3       2 3   2 1  1
             |       | |   | |  |
          [1,2,3] [1,3,2] ... ... (6 total)
```

## Step-by-Step for First Solution [1,2,3]

| Step | Action | path | remaining | Explanation |
|------|--------|------|-----------|-------------|
| 1 | Start | [] | [1,2,3] | Beginning - nothing chosen |
| 2 | Choose 1 | [1] | [2,3] | Pick 1 first, remove from remaining |
| 3 | Choose 2 | [1,2] | [3] | Pick 2 next, remove from remaining |
| 4 | Choose 3 | [1,2,3] | [] | Pick 3 last, no more choices |
| 5 | **SOLUTION!** | [1,2,3] | [] | Path length = 3, save it! |
| 6 | Backtrack | [1,2] | [3] | Pop 3, try other options |
| 7 | No more options at [1,2] | | | |
| 8 | Backtrack | [1] | [2,3] | Pop 2, try next choice |
| 9 | Choose 3 | [1,3] | [2] | Now try 3 after 1 |
| 10 | Choose 2 | [1,3,2] | [] | Pick 2 last |
| 11 | **SOLUTION!** | [1,3,2] | [] | Save it! |

## Why Backtracking Works

### The Key Steps:
1. **Make a choice** (`path.append(choice)`) - try this option
2. **Explore** (`backtrack(...)`) - see where it leads
3. **Undo** (`path.pop()`) - remove choice to try next option

### The Magic:
- `path` is SHARED across all calls (same list)
- When you `pop()`, you undo for the next iteration
- Each `for` loop tries all possibilities at that level

### Example of the "Undo" Magic:
```python
path = [1]           # After choosing 1
path.append(2)       # Choose 2: path = [1,2]
backtrack(...)       # Explore [1,2,3] path
path.pop()           # Undo: path = [1] again!
path.append(3)       # Choose 3: path = [1,3]
backtrack(...)       # Explore [1,3,2] path
```

Without `path.pop()`, you'd get [1,2,3] then try to build [1,2,3] again!

## Why Copy the Path?

```python
result.append(path[:])  # COPY - creates [1,2,3] snapshot
```

Without the copy:
- You save a reference to the same `path` list
- When you `pop()` later, the saved solution changes too!
- Result: All solutions would be `[]` at the end

## Complexity
- **Time**: O(n! × n) - n! permutations, n work to copy each
- **Space**: O(n) - recursion depth (path length)
