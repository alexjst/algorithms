#!/usr/bin/env python3
"""Solution for Problem 5: Text Editor with Undo/Redo"""

from typing import List, Tuple

class TextEditor:
    def __init__(self):
        """
        Initialize text editor with undo/redo support.

        TODO: Implement initialization
        Hints:
        1. Store current text (string or list of chars)
        2. Create undo stack: list of operations
        3. Create redo stack: list of operations
        4. Each operation can be tuple: (type, data)
           - For insert: ("insert", position, text)
           - For delete: ("delete", start, end, deleted_text)
        5. Store deleted_text in delete operations for undo
        """
        pass

    def insert(self, text: str, position: int) -> None:
        """
        Insert text at given position.

        TODO: Implement insert operation
        Hints:
        1. Validate position (0 <= position <= len(current_text))
        2. Insert text: current_text[:position] + text + current_text[position:]
        3. Push operation to undo stack: ("insert", position, text)
        4. Clear redo stack (new operation invalidates redo)
        5. Update current text

        Args:
            text: Text to insert
            position: Position to insert at (0-indexed)
        """
        pass

    def delete(self, start: int, end: int) -> None:
        """
        Delete text from start to end (exclusive).

        TODO: Implement delete operation
        Hints:
        1. Validate range (0 <= start < end <= len(current_text))
        2. Save deleted text for undo: current_text[start:end]
        3. Delete: current_text[:start] + current_text[end:]
        4. Push operation to undo stack: ("delete", start, end, deleted_text)
        5. Clear redo stack
        6. Update current text

        Args:
            start: Start position (inclusive)
            end: End position (exclusive)
        """
        pass

    def undo(self) -> bool:
        """
        Undo last operation.

        TODO: Implement undo
        Hints:
        1. If undo stack is empty: return False
        2. Pop operation from undo stack
        3. Reverse the operation:
           - If was insert: delete the inserted text
           - If was delete: insert the deleted text back
        4. Push original operation to redo stack
        5. Update current text
        6. Return True

        Returns:
            True if undo performed, False if nothing to undo
        """
        pass

    def redo(self) -> bool:
        """
        Redo previously undone operation.

        TODO: Implement redo
        Hints:
        1. If redo stack is empty: return False
        2. Pop operation from redo stack
        3. Reapply the operation:
           - If was insert: insert the text again
           - If was delete: delete the text again
        4. Push operation to undo stack
        5. Update current text
        6. Return True

        Returns:
            True if redo performed, False if nothing to redo
        """
        pass

    def get_text(self) -> str:
        """
        Get current text content.

        TODO: Implement get_text
        Hints:
        1. Return current text as string
        2. If storing as list, join into string

        Returns:
            Current text content
        """
        pass
