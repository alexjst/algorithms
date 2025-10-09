# Subsets vs Permutations: Template Comparison

## Key Differences

| Aspect | Permutations | Subsets |
|--------|--------------|---------|
| **Goal** | All orderings of elements | All possible combinations |
| **When to save** | When path.length == n | **Every step** (all paths valid) |
| **Tracking** | `remaining_choices` list | `start` index |
| **Size** | Always n elements | 0 to n elements |
| **Count** | n! solutions | 2^n solutions |
| **Example [1,2,3]** | 6 permutations | 8 subsets |

## Side-by-Side Code

### Permutations Template
```python
def backtrack(path, remaining_choices):
    # Only save when complete
    if len(path) == len(nums):
        result.append(path[:])
        return

    # Try each remaining element
    for i, choice in enumerate(remaining_choices):
        path.append(choice)
        # Pass remaining without current choice
        new_remaining = remaining_choices[:i] + remaining_choices[i+1:]
        backtrack(path, new_remaining)
        path.pop()
```

### Subsets Template
```python
def backtrack(path, start):
    # Save at EVERY step
    result.append(path[:])

    # Try including each element from start onwards
    for i in range(start, len(nums)):
        path.append(nums[i])
        # Move start forward to avoid duplicates
        backtrack(path, i + 1)
        path.pop()
```

## Why `start` instead of `remaining_choices`?

For subsets, we use `start` index to avoid duplicates:

**With `start` (correct):**
```
start=0: Try [1,2,3]
  Include 1, start=1: Try [2,3]
    Include 2, start=2: Try [3]
      Include 3 -> [1,2,3] ✓
    Skip 2, start=3: Try [3]
      Include 3 -> [1,3] ✓
```

**Without `start` (wrong - would generate duplicates):**
```
Try all elements each time
  Include 1: Try [1,2,3]
    Include 2 -> [1,2] ✓
    Include 3 -> [1,3] ✓
  Include 2: Try [1,2,3]
    Include 1 -> [2,1] ✗ DUPLICATE of [1,2]!
```

## Decision Tree Visualization

### Permutations of [1,2]
```
                []
               / \
              1   2
             /     \
            2       1
           |         |
         [1,2]     [2,1]
```
Result: `[[1,2], [2,1]]` - 2! = 2 permutations

### Subsets of [1,2]
```
                [] ← Save!
               / \
        (add 1)   (skip 1)
             /     \
           [1]      [] ← continue from index 1
            |         \
    (add 2)/ \(skip)   (add 2)
          /   \          \
       [1,2]  [1]        [2]
        ↓      ↓          ↓
      Save   Save       Save
```
Result: `[[], [1], [1,2], [2]]` - 2^2 = 4 subsets

## Why Save at Every Step?

**Permutations:** Only complete arrangements count
- [1] is not a permutation of [1,2,3]
- [1,2] is not a permutation of [1,2,3]
- Only [1,2,3] is valid ✓

**Subsets:** Every combination counts
- [] is a subset ✓
- [1] is a subset ✓
- [1,2] is a subset ✓
- [1,2,3] is a subset ✓

## Practice: What if we want subsets of size k?

```python
def k_subsets(nums, k):
    result = []

    def backtrack(path, start):
        # Only save when we have k elements
        if len(path) == k:
            result.append(path[:])
            return

        for i in range(start, len(nums)):
            path.append(nums[i])
            backtrack(path, i + 1)
            path.pop()

    backtrack([], 0)
    return result

# k_subsets([1,2,3], 2) -> [[1,2], [1,3], [2,3]]
```

Now it's a hybrid: save when `len(path) == k` like permutations, but use `start` like subsets!
