#!/usr/bin/env python3
"""Solution for Problem 7: Memory Allocator"""

from typing import Optional

class MemoryAllocator:
    def __init__(self, total_size: int):
        """
        Initialize memory allocator with total memory size.

        TODO: Implement initialization
        Hints:
        1. Store total_size
        2. Track free blocks: list of (start, size) tuples
        3. Initially, entire memory is one free block: [(0, total_size)]
        4. Track allocated blocks (optional, for validation)
        5. Consider using sorted list or balanced tree for free blocks

        Approaches:
        - Simple: List of free blocks
        - Better: Sorted list by address (for coalescing)
        - Best: Balanced tree (e.g., using sortedcontainers.SortedList)

        Args:
            total_size: Total memory size available
        """
        pass

    def allocate(self, size: int) -> Optional[int]:
        """
        Allocate contiguous memory block of given size.

        TODO: Implement allocation
        Hints:
        1. Validate size > 0
        2. Find suitable free block (First Fit or Best Fit)
           - First Fit: First block with size >= requested size
           - Best Fit: Smallest block with size >= requested size
        3. Split free block if larger than needed:
           - Remove block from free list
           - If block_size > size: add (block_start + size, block_size - size) back
        4. Return block_start address
        5. Return None if no suitable block found

        First Fit Algorithm:
        for (start, block_size) in free_blocks:
            if block_size >= size:
                remove (start, block_size) from free_blocks
                if block_size > size:
                    add (start + size, block_size - size) to free_blocks
                return start
        return None

        Args:
            size: Size of memory to allocate

        Returns:
            Starting address of allocated block, or None if allocation fails
        """
        pass

    def free(self, ptr: int) -> None:
        """
        Free previously allocated memory block.

        TODO: Implement deallocation
        Hints:
        1. Find the allocated block starting at ptr
           - Need to track allocated blocks: dict {ptr: size}
        2. Add block back to free list
        3. Coalesce (merge) with adjacent free blocks:
           - Sort free blocks by address
           - Check if previous block ends at ptr
           - Check if next block starts at ptr + size
           - Merge adjacent blocks into one larger block
        4. Keep free blocks sorted for efficient coalescing

        Coalescing Logic:
        1. Insert (ptr, size) into free_blocks
        2. Sort free_blocks by address
        3. Merge adjacent blocks:
           for i in range(len(free_blocks) - 1):
               (start1, size1), (start2, size2) = free_blocks[i], free_blocks[i+1]
               if start1 + size1 == start2:
                   merge into (start1, size1 + size2)

        Args:
            ptr: Starting address of block to free
        """
        pass

    def _find_best_fit(self, size: int) -> Optional[tuple]:
        """
        Helper: Find best fitting free block (optional).

        TODO: Implement best fit search
        Hints:
        1. Iterate through free_blocks
        2. Find smallest block where block_size >= size
        3. Return (start, block_size, index) or None
        """
        pass

    def _coalesce(self) -> None:
        """
        Helper: Merge adjacent free blocks (optional).

        TODO: Implement coalescing
        Hints:
        1. Sort free_blocks by start address
        2. Merge adjacent blocks:
           - If block[i].end == block[i+1].start: merge them
        3. Update free_blocks list
        """
        pass

    def get_free_memory(self) -> int:
        """
        Get total free memory (optional, for debugging).

        Returns:
            Total bytes of free memory
        """
        pass
