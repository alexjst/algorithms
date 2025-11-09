#!/usr/bin/env python3
"""Solution for Problem 9: Nested Transaction KV Store"""

from typing import Optional, Dict

class TransactionStore:
    def __init__(self):
        """
        TODO: Initialize transaction store
        Hints:
        1. Use stack to maintain transaction levels
        2. Each level is a dictionary of key-value pairs
        3. Start with empty stack (or base transaction)
        """
        pass

    def start_transaction(self) -> None:
        """
        Start a new transaction.

        TODO: Implement transaction start
        Hints:
        1. Push new empty dictionary onto stack
        2. New transaction inherits view of parent
        """
        pass

    def put(self, key: str, value: str) -> None:
        """
        Store key-value pair in current transaction.

        TODO: Implement put operation
        Hints:
        1. Store in top of stack (current transaction)
        2. Throw error if no transaction active
        """
        pass

    def get(self, key: str) -> Optional[str]:
        """
        Get value for key (searches from current transaction to root).

        TODO: Implement get operation
        Hints:
        1. Search from top of stack downward
        2. Return first value found
        3. Return None if key not found
        """
        pass

    def commit(self) -> None:
        """
        Commit current transaction (merge into parent).

        TODO: Implement commit operation
        Hints:
        1. Pop current transaction from stack
        2. Merge all its keys into parent transaction
        3. Throw error if no transaction to commit
        """
        pass

    def abort(self) -> None:
        """
        Abort current transaction (discard changes).

        TODO: Implement abort operation
        Hints:
        1. Simply pop current transaction from stack
        2. Don't merge anything
        3. Throw error if no transaction to abort
        """
        pass
