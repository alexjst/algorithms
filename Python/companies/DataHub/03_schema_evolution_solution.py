#!/usr/bin/env python3
"""
Solution for Problem 3: Schema Evolution Tracking

TODO: Implement the SchemaEvolution class below.
"""

from typing import Dict, List

class SchemaEvolution:
    """
    Track schema evolution and compatibility across versions.
    """

    def __init__(self):
        """Initialize the schema tracker."""
        # TODO: Implement initialization
        # You'll need to store:
        # - Schema versions for each table
        # - Timestamps for each version
        pass

    def add_schema(self, table_name: str, schema: Dict[str, str], version: int) -> None:
        """
        Add a schema version for a table.

        Args:
            table_name: Name of the table
            schema: Dictionary mapping field names to types
            version: Version number
        """
        # TODO: Implement schema storage
        pass

    def get_changes(self, table_name: str, version_from: int, version_to: int) -> Dict[str, List[str]]:
        """
        Get schema changes between two versions.

        Args:
            table_name: Name of the table
            version_from: Source version
            version_to: Target version

        Returns:
            Dictionary with keys "added", "removed", "modified"
            containing lists of field names
        """
        # TODO: Implement change detection
        # Hints:
        # 1. Get schemas for both versions
        # 2. Added: fields in version_to but not in version_from
        # 3. Removed: fields in version_from but not in version_to
        # 4. Modified: fields in both but with different types
        pass

    def is_backward_compatible(self, table_name: str, new_version: int, old_version: int) -> bool:
        """
        Check if new schema is backward compatible with old schema.

        Backward compatible means: new schema can read data written with old schema.

        Args:
            table_name: Name of the table
            new_version: New schema version
            old_version: Old schema version

        Returns:
            True if backward compatible, False otherwise
        """
        # TODO: Implement backward compatibility check
        # Hints:
        # Backward compatible if:
        # 1. All fields in old schema exist in new schema (no fields removed)
        # 2. Field types haven't changed in incompatible ways
        #
        # Simple approach: check that no fields were removed or had types changed
        pass
