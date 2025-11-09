#!/usr/bin/env python3
"""
Problem 7: Video Stream Scheduling

SNAP's Stories and Spotlight features require efficient video chunk scheduling.
Implement a scheduler for prioritizing video chunks for streaming.

Requirements:
- Schedule video chunks based on priority and bandwidth
- Handle different quality levels (480p, 720p, 1080p)
- Optimize for minimal buffering
- Track bandwidth usage

Example:
    scheduler = VideoScheduler(bandwidth_limit=1000)
    
    scheduler.add_chunk("story1", quality="720p", priority=5, size_kb=200)
    scheduler.add_chunk("story2", quality="1080p", priority=8, size_kb=400)
    scheduler.add_chunk("story3", quality="480p", priority=3, size_kb=100)
    
    next_chunks = scheduler.get_next_batch(max_size_kb=600)
    # Returns highest priority chunks within bandwidth limit
    # Result: [story2 (1080p), story1 (720p)]

Time Complexity: O(n log n) for scheduling with priority queue
Space Complexity: O(n)
"""

try:
    import importlib.util
    spec = importlib.util.spec_from_file_location("solution_module",
                                                   "07_video_stream_scheduling_solution.py")
    solution_module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(solution_module)
    VideoScheduler = solution_module.VideoScheduler
except Exception as e:
    print(f"❌ Error importing solution: {e}")
    exit(1)

def test_video_scheduler():
    print("Testing Video Stream Scheduling...")
    print()

    # Test 1: Priority-based scheduling
    print("Test 1: Priority-based scheduling")
    scheduler1 = VideoScheduler(bandwidth_limit=1000)
    scheduler1.add_chunk("chunk1", quality="720p", priority=5, size_kb=200)
    scheduler1.add_chunk("chunk2", quality="1080p", priority=8, size_kb=300)
    scheduler1.add_chunk("chunk3", quality="480p", priority=3, size_kb=100)
    
    batch1 = scheduler1.get_next_batch(max_size_kb=400)
    assert len(batch1) >= 1, "Test 1 failed: should return chunks"
    assert batch1[0]["chunk_id"] == "chunk2", "Test 1 failed: should prioritize chunk2"
    print("✓ Test 1 passed")
    print()

    # Test 2: Bandwidth limit
    print("Test 2: Respect bandwidth limit")
    scheduler2 = VideoScheduler(bandwidth_limit=500)
    scheduler2.add_chunk("c1", quality="1080p", priority=10, size_kb=600)
    scheduler2.add_chunk("c2", quality="480p", priority=5, size_kb=100)
    
    batch2 = scheduler2.get_next_batch(max_size_kb=500)
    total_size = sum(c["size_kb"] for c in batch2)
    assert total_size <= 500, f"Test 2 failed: exceeded bandwidth ({total_size})"
    print("✓ Test 2 passed")
    print()

    # Test 3: Quality adaptation
    print("Test 3: Quality level prioritization")
    scheduler3 = VideoScheduler(bandwidth_limit=1000)
    scheduler3.add_chunk("hq", quality="1080p", priority=7, size_kb=500)
    scheduler3.add_chunk("mq", quality="720p", priority=7, size_kb=300)
    scheduler3.add_chunk("lq", quality="480p", priority=7, size_kb=150)
    
    batch3 = scheduler3.get_next_batch(max_size_kb=1000)
    assert len(batch3) > 0, "Test 3 failed: should return chunks"
    print("✓ Test 3 passed")
    print()

    print("All tests passed! ✓")

if __name__ == "__main__":
    test_video_scheduler()
