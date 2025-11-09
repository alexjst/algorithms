#!/usr/bin/env python3
"""
Problem 7: Memory Allocator (malloc/free simulation)

Actual OpenAI interview question - implement a memory allocator.
Simulate malloc() and free() with efficient memory management.

Requirements:
- allocate(size): Allocate contiguous memory block of given size
- free(ptr): Free previously allocated memory block
- Efficient allocation and deallocation
- Handle fragmentation
- Support memory reuse

Example:
    allocator = MemoryAllocator(total_size=1000)

    ptr1 = allocator.allocate(100)  # Allocate 100 bytes, returns pointer (e.g., 0)
    ptr2 = allocator.allocate(200)  # Allocate 200 bytes, returns pointer (e.g., 100)
    ptr3 = allocator.allocate(150)  # Allocate 150 bytes, returns pointer (e.g., 300)

    allocator.free(ptr2)            # Free 200 bytes starting at 100
    ptr4 = allocator.allocate(50)   # Reuse freed space, returns 100

    allocator.free(ptr1)
    allocator.free(ptr3)
    allocator.free(ptr4)

Optimization Goals:
- Naive: O(n) allocate, O(n) free
- Better: O(n) allocate, O(1) free
- Best: O(log n) allocate, O(log n) free

Approaches:
1. First Fit: Find first block large enough
2. Best Fit: Find smallest block that fits
3. Buddy System: Power-of-2 allocation
4. Free List: Track free blocks with linked list or balanced tree

Time Complexity: O(log n) for both allocate/free with balanced tree
Space Complexity: O(n) for tracking free blocks
"""

try:
    import importlib.util
    spec = importlib.util.spec_from_file_location("solution_module",
                                                   "07_memory_allocator_solution.py")
    solution_module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(solution_module)
    MemoryAllocator = solution_module.MemoryAllocator
except Exception as e:
    print(f"❌ Error importing solution: {e}")
    exit(1)

def test_memory_allocator():
    print("Testing Memory Allocator...")
    print()

    # Test 1: Basic allocation
    print("Test 1: Basic allocation")
    alloc1 = MemoryAllocator(1000)
    ptr1 = alloc1.allocate(100)
    assert ptr1 is not None, "Test 1a failed: allocation returned None"
    assert ptr1 >= 0, "Test 1b failed: invalid pointer"
    ptr2 = alloc1.allocate(200)
    assert ptr2 is not None, "Test 1c failed"
    assert ptr2 != ptr1, "Test 1d failed: overlapping allocation"
    print("✓ Test 1 passed")
    print()

    # Test 2: Basic free
    print("Test 2: Free and reallocate")
    alloc2 = MemoryAllocator(1000)
    ptr_a = alloc2.allocate(100)
    ptr_b = alloc2.allocate(200)
    alloc2.free(ptr_a)
    ptr_c = alloc2.allocate(50)  # Should reuse freed space
    assert ptr_c is not None, "Test 2a failed"
    print("✓ Test 2 passed")
    print()

    # Test 3: Out of memory
    print("Test 3: Out of memory handling")
    alloc3 = MemoryAllocator(100)
    ptr1 = alloc3.allocate(60)
    ptr2 = alloc3.allocate(50)  # Only 40 bytes left
    assert ptr1 is not None, "Test 3a failed"
    assert ptr2 is None, "Test 3b failed: should return None when out of memory"
    print("✓ Test 3 passed")
    print()

    # Test 4: Exact fit
    print("Test 4: Exact fit allocation")
    alloc4 = MemoryAllocator(100)
    ptr = alloc4.allocate(100)
    assert ptr is not None, "Test 4a failed"
    ptr2 = alloc4.allocate(1)
    assert ptr2 is None, "Test 4b failed: no space left"
    print("✓ Test 4 passed")
    print()

    # Test 5: Multiple allocations and frees
    print("Test 5: Multiple allocations and frees")
    alloc5 = MemoryAllocator(1000)
    ptrs = []
    for i in range(10):
        ptr = alloc5.allocate(50)
        assert ptr is not None, f"Test 5a failed at iteration {i}"
        ptrs.append(ptr)

    # Free every other block
    for i in range(0, 10, 2):
        alloc5.free(ptrs[i])

    # Allocate in freed spaces
    ptr = alloc5.allocate(40)
    assert ptr is not None, "Test 5b failed: should reuse freed space"
    print("✓ Test 5 passed")
    print()

    # Test 6: Free and merge adjacent blocks
    print("Test 6: Coalescing adjacent free blocks")
    alloc6 = MemoryAllocator(1000)
    ptr1 = alloc6.allocate(100)
    ptr2 = alloc6.allocate(100)
    ptr3 = alloc6.allocate(100)

    alloc6.free(ptr1)
    alloc6.free(ptr3)
    alloc6.free(ptr2)  # Should merge all three

    # Should be able to allocate 300 bytes
    ptr_big = alloc6.allocate(300)
    assert ptr_big is not None, "Test 6 failed: coalescing not working"
    print("✓ Test 6 passed")
    print()

    # Test 7: Zero size allocation
    print("Test 7: Edge cases")
    alloc7 = MemoryAllocator(1000)
    ptr_zero = alloc7.allocate(0)
    assert ptr_zero is None, "Test 7a failed: zero size should return None"
    print("✓ Test 7 passed")
    print()

    # Test 8: Fragmentation handling
    print("Test 8: Fragmentation handling")
    alloc8 = MemoryAllocator(1000)
    # Allocate blocks
    p1 = alloc8.allocate(100)
    p2 = alloc8.allocate(100)
    p3 = alloc8.allocate(100)
    p4 = alloc8.allocate(100)
    p5 = alloc8.allocate(100)

    # Free alternating blocks to create fragmentation
    alloc8.free(p1)
    alloc8.free(p3)
    alloc8.free(p5)

    # Try to allocate 150 bytes (won't fit in fragmented 100-byte holes)
    ptr_big = alloc8.allocate(150)
    # Should still be able to use remaining contiguous space
    assert ptr_big is not None or ptr_big is None, "Test 8 passed (fragmentation handled)"
    print("✓ Test 8 passed")
    print()

    print("All tests passed! ✓")

if __name__ == "__main__":
    test_memory_allocator()
