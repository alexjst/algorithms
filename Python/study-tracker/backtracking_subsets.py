"""
Simplest Subset Example: Generate All Subsets of [1,2,3]

Problem: Given [1,2,3], generate all possible subsets (the power set):
[[], [1], [2], [3], [1,2], [1,3], [2,3], [1,2,3]]

Total: 2^3 = 8 subsets

This also matches the backtracking template!
"""

def subsets(nums):
    result = []

    def backtrack(path, start):
        # path: Current subset being built (e.g., [1, 2])
        # start: Index to start considering elements from (to avoid duplicates)

        # KEY DIFFERENCE: Every path is a valid solution!
        # We don't wait until path is "complete"
        result.append(path[:])  # Save current subset (even if empty)

        # Try adding each remaining element
        for i in range(start, len(nums)):
            choice = nums[i]

            # No validity check needed - all choices are valid

            # Make the choice (include this element)
            path.append(choice)

            # Explore with this choice (start from i+1 to avoid duplicates)
            backtrack(path, i + 1)

            # Undo the choice (backtrack)
            path.pop()

    # Start with empty subset, consider all elements
    backtrack([], 0)
    return result


# Example execution
nums = [1, 2, 3]
result = subsets(nums)

print(f"Input: {nums}")
print(f"Output: {result}")
print(f"\nTotal subsets: {len(result)} (should be 2^{len(nums)} = {2**len(nums)})")

# Let's trace the execution manually:
print("\n--- Execution Trace (Decision Tree) ---")
print("Each level decides: include element or skip it")
print()
print("backtrack([], start=0)  -> Save []")
print("  ├─ Include 1:")
print("  │  backtrack([1], start=1)  -> Save [1]")
print("  │    ├─ Include 2:")
print("  │    │  backtrack([1,2], start=2)  -> Save [1,2]")
print("  │    │    ├─ Include 3:")
print("  │    │    │  backtrack([1,2,3], start=3)  -> Save [1,2,3]")
print("  │    │    │    (no more elements, return)")
print("  │    │    │  backtrack([1,2], start=2)  <- back")
print("  │    │    (no more elements, return)")
print("  │    │  backtrack([1], start=1)  <- back")
print("  │    ├─ Include 3 (skip 2):")
print("  │    │  backtrack([1,3], start=3)  -> Save [1,3]")
print("  │    │    (no more elements, return)")
print("  │    │  backtrack([1], start=1)  <- back")
print("  │  backtrack([], start=0)  <- back")
print("  ├─ Include 2 (skip 1):")
print("  │  backtrack([2], start=2)  -> Save [2]")
print("  │    ├─ Include 3:")
print("  │    │  backtrack([2,3], start=3)  -> Save [2,3]")
print("  │    │    (no more elements, return)")
print("  │  backtrack([], start=0)  <- back")
print("  ├─ Include 3 (skip 1,2):")
print("  │  backtrack([3], start=3)  -> Save [3]")
print("  │    (no more elements, return)")
print("  backtrack([], start=0)  <- back")
print("  (done)")
