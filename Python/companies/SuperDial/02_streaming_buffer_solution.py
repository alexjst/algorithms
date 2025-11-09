#!/usr/bin/env python3
"""
Solution for Problem 2: Streaming Data Buffer Management

TODO: Implement the StreamingBuffer class below.
"""

class StreamingBuffer:
    """
    Circular buffer for managing streaming voice transcription data.

    Args:
        capacity: Maximum number of bytes the buffer can hold
    """

    def __init__(self, capacity: int):
        """Initialize the buffer."""
        # TODO: Implement initialization
        pass

    def write(self, data: str) -> int:
        """
        Write data to the buffer.

        Args:
            data: String data to write

        Returns:
            Number of bytes written
        """
        # TODO: Implement write operation
        # Hints:
        # 1. Handle buffer overflow (circular behavior)
        # 2. Keep track of the current position
        # 3. Update the buffer with new data
        # 4. Return number of bytes written
        pass

    def read(self) -> str:
        """
        Read all available data from buffer.

        Returns:
            String containing all buffered data
        """
        # TODO: Implement read operation
        # Hint: Return the current content of the buffer
        pass

    def available(self) -> int:
        """
        Get number of bytes available in buffer.

        Returns:
            Number of bytes currently stored
        """
        # TODO: Implement available bytes count
        pass
