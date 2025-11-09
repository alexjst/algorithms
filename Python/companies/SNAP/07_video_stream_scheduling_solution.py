#!/usr/bin/env python3
"""Solution for Problem 7: Video Stream Scheduling"""

import heapq
from typing import List, Dict

class VideoScheduler:
    def __init__(self, bandwidth_limit: int):
        """
        TODO: Initialize video chunk scheduler
        Hints:
        1. Use max heap for priority (negate priorities)
        2. Track chunks and their metadata
        3. Store bandwidth limit
        """
        pass

    def add_chunk(self, chunk_id: str, quality: str, priority: int, size_kb: int) -> None:
        """
        Add video chunk to schedule.
        
        TODO: Implement chunk addition
        Hints:
        1. Store chunk with metadata
        2. Add to priority queue (higher priority first)
        3. Consider quality tier when equal priority
        """
        pass

    def get_next_batch(self, max_size_kb: int) -> List[Dict]:
        """
        Get next batch of chunks within size limit.
        
        TODO: Implement batch scheduling
        Hints:
        1. Pop chunks from heap by priority
        2. Track cumulative size
        3. Stop when size limit reached
        4. Return list of chunk dicts
        """
        pass
