"""
Simplest Backtracking Example: Generate All Permutations

Problem: Given [1,2,3], generate all possible orderings:
[[1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], [3,2,1]]

This perfectly matches the backtracking template!
"""

def permutations(nums):
    result = []

    def backtrack(path, remaining_choices):
        # path: Current permutation being built (e.g., [1, 2])
        # remaining_choices: Numbers not yet used (e.g., [3])

        # Base case: Is this a complete solution?
        if len(path) == len(nums):  # All numbers used
            result.append(path[:])   # Save a COPY
            return

        # Try each remaining choice
        for i, choice in enumerate(remaining_choices):
            # No validity check needed - all choices are valid

            # Make the choice
            path.append(choice)

            # Create new remaining list (all except current choice)
            new_remaining = remaining_choices[:i] + remaining_choices[i+1:]

            # Explore with this choice
            backtrack(path, new_remaining)

            # Undo the choice (backtrack)
            path.pop()

    # Start with empty path, all numbers available
    backtrack([], nums)
    return result


# Example execution
nums = [1, 2, 3]
result = permutations(nums)

print(f"Input: {nums}")
print(f"Output: {result}")
print(f"\nTotal permutations: {len(result)}")

# Let's trace the first few calls manually:
print("\n--- Execution Trace ---")
print("Start: backtrack([], [1,2,3])")
print("  Choose 1: backtrack([1], [2,3])")
print("    Choose 2: backtrack([1,2], [3])")
print("      Choose 3: backtrack([1,2,3], [])")
print("        ✓ Complete! Save [1,2,3]")
print("      Backtrack: path=[1,2]")
print("    Backtrack: path=[1]")
print("    Choose 3: backtrack([1,3], [2])")
print("      Choose 2: backtrack([1,3,2], [])")
print("        ✓ Complete! Save [1,3,2]")
print("      Backtrack: path=[1,3]")
print("    Backtrack: path=[1]")
print("  Backtrack: path=[]")
print("  Choose 2: ... (similar pattern)")
print("  ...")
