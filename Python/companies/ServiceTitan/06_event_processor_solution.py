#!/usr/bin/env python3
"""Solution for Problem 6: Event Processing System"""

from typing import Callable, Dict, List, Any, Set
from collections import defaultdict
import traceback

class EventProcessor:
    def __init__(self):
        """
        Initialize event processor.

        TODO: Implement initialization
        Hints:
        1. Need to store event_type -> list of handlers mapping
        2. Use defaultdict(list) for automatic list creation
        3. Or use regular dict and check if key exists
        4. Consider using set to avoid duplicate handlers

        Using defaultdict with list:
        self.handlers = defaultdict(list)

        Using defaultdict with set (to avoid duplicates):
        self.handlers = defaultdict(set)

        Args:
            None
        """
        pass

    def subscribe(self, event_type: str, handler: Callable) -> None:
        """
        Subscribe handler to event type.

        TODO: Implement subscription
        Hints:
        1. Add handler to list/set for this event_type
        2. Check if handler already subscribed (avoid duplicates)
        3. If using list: check if handler in list before appending
        4. If using set: set automatically handles duplicates

        Using list (with duplicate check):
        if handler not in self.handlers[event_type]:
            self.handlers[event_type].append(handler)

        Using set:
        self.handlers[event_type].add(handler)

        Args:
            event_type: Type of event to subscribe to
            handler: Callback function to handle event
        """
        pass

    def unsubscribe(self, event_type: str, handler: Callable) -> None:
        """
        Unsubscribe handler from event type.

        TODO: Implement unsubscription
        Hints:
        1. Remove handler from list/set for this event_type
        2. Check if event_type exists before removing
        3. Check if handler exists before removing
        4. Use discard() for sets, remove() for lists (with try/except)

        Using list:
        if event_type in self.handlers:
            try:
                self.handlers[event_type].remove(handler)
            except ValueError:
                pass  # Handler not in list

        Using set:
        if event_type in self.handlers:
            self.handlers[event_type].discard(handler)

        Args:
            event_type: Type of event to unsubscribe from
            handler: Callback function to remove
        """
        pass

    def publish(self, event: Dict[str, Any]) -> None:
        """
        Publish event to all subscribed handlers.

        TODO: Implement publishing
        Hints:
        1. Get event type from event dict (event["type"])
        2. Get all handlers for this event type
        3. Call each handler with event data
        4. Wrap handler calls in try/except to handle errors gracefully
        5. One handler error shouldn't stop other handlers from executing

        Implementation:
        event_type = event.get("type")
        if not event_type or event_type not in self.handlers:
            return

        for handler in self.handlers[event_type]:
            try:
                handler(event)
            except Exception as e:
                # Log error but continue with other handlers
                print(f"Error in handler {handler.__name__}: {e}")
                # In production, use proper logging
                # traceback.print_exc()

        Args:
            event: Event data dictionary (must contain "type" key)
        """
        pass
