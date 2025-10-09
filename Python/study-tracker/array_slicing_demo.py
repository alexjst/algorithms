"""
Demo: How removing an element works with list slicing
"""

remaining = [1, 2, 3]

print("Original list:", remaining)
print()

# Remove element at index 0 (the '1')
i = 0
before = remaining[:i]   # Everything before index 0 -> []
after = remaining[i+1:]  # Everything after index 0  -> [2, 3]
new_list = before + after
print(f"Remove index {i} (value {remaining[i]}):")
print(f"  before = remaining[:{i}] = {before}")
print(f"  after  = remaining[{i+1}:] = {after}")
print(f"  result = {before} + {after} = {new_list}")
print()

# Remove element at index 1 (the '2')
i = 1
before = remaining[:i]   # Everything before index 1 -> [1]
after = remaining[i+1:]  # Everything after index 1  -> [3]
new_list = before + after
print(f"Remove index {i} (value {remaining[i]}):")
print(f"  before = remaining[:{i}] = {before}")
print(f"  after  = remaining[{i+1}:] = {after}")
print(f"  result = {before} + {after} = {new_list}")
print()

# Remove element at index 2 (the '3')
i = 2
before = remaining[:i]   # Everything before index 2 -> [1, 2]
after = remaining[i+1:]  # Everything after index 2  -> []
new_list = before + after
print(f"Remove index {i} (value {remaining[i]}):")
print(f"  before = remaining[:{i}] = {before}")
print(f"  after  = remaining[{i+1}:] = {after}")
print(f"  result = {before} + {after} = {new_list}")
print()

print("=" * 50)
print("Visual representation:")
print()
print("remaining = [1, 2, 3]")
print("             0  1  2  <- indices")
print()
print("To remove index 1:")
print("  [:1]  = [1]       (elements before index 1)")
print("  [2:]  = [3]       (elements after index 1)")
print("  [1] + [3] = [1, 3]")
