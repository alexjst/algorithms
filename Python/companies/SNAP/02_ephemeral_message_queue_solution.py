#!/usr/bin/env python3
"""
Solution for Problem 2: Ephemeral Message Queue

TODO: Implement the EphemeralMessageQueue class below.
"""

import time
from typing import List, Dict, Optional
from collections import defaultdict
import heapq

class EphemeralMessageQueue:
    """
    Message queue with TTL (time-to-live) for ephemeral messages.
    """

    def __init__(self):
        # TODO: Initialize data structures
        # Hints:
        # - Dict to store messages by recipient
        # - Counter for message IDs
        # - Heap for tracking expiration times
        pass

    def send_message(self, sender: str, recipient: str, content: str,
                     ttl_seconds: int) -> int:
        """
        Send a message with expiration time.

        Args:
            sender: Username of sender
            recipient: Username of recipient
            content: Message content
            ttl_seconds: Time-to-live in seconds

        Returns:
            Message ID
        """
        # TODO: Implement message sending
        # Hints:
        # 1. Generate unique message ID
        # 2. Calculate expiration timestamp: time.time() + ttl_seconds
        # 3. Store message with metadata
        # 4. Add to expiration heap
        pass

    def get_messages(self, recipient: str) -> List[Dict]:
        """
        Get all non-expired, unviewed messages for recipient.

        Args:
            recipient: Username of recipient

        Returns:
            List of message dictionaries
        """
        # TODO: Implement message retrieval
        # Hints:
        # 1. Clean up expired messages first
        # 2. Filter messages for recipient
        # 3. Check expiration time: message['expires_at'] > time.time()
        # 4. Return list of message dicts
        pass

    def mark_viewed(self, recipient: str, message_id: int) -> None:
        """
        Mark message as viewed and delete it (Snapchat behavior).

        Args:
            recipient: Username of recipient
            message_id: ID of message to mark as viewed
        """
        # TODO: Implement view and delete
        pass

    def _cleanup_expired(self) -> None:
        """Remove expired messages from queue."""
        # TODO: Implement cleanup using heap
        pass
