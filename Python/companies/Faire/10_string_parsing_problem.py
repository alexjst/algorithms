#!/usr/bin/env python3
"""
Problem 10: String Parsing Problem

Parse log entries and extract structured information.

Log format: "[TIMESTAMP] LEVEL: message | key1=value1 key2=value2"

Example:
    Input: "[2024-01-15 10:30:45] ERROR: Database connection failed | host=db.example.com port=5432"

    Output: {
        'timestamp': '2024-01-15 10:30:45',
        'level': 'ERROR',
        'message': 'Database connection failed',
        'metadata': {
            'host': 'db.example.com',
            'port': '5432'
        }
    }

Constraints:
    - Timestamp format: YYYY-MM-DD HH:MM:SS
    - Levels: DEBUG, INFO, WARNING, ERROR, CRITICAL
    - Metadata is optional (may not have | section)
    - Key-value pairs separated by spaces
"""

from typing import Dict, Optional
import re


def parse_log_entry(log: str) -> Optional[Dict]:
    """
    Parse a log entry into structured format.

    Args:
        log: Log string to parse

    Returns:
        Dictionary with timestamp, level, message, metadata
        Returns None if invalid format
    """
    # TODO: Implement log parsing with regex
    return None  # Placeholder


def parse_logs(log_string: str) -> list:
    """
    Parse multiple log entries (separated by newlines).

    Args:
        log_string: Multi-line log string

    Returns:
        List of parsed log dictionaries
    """
    # TODO: Implement multi-line parsing
    return []  # Placeholder


def run_tests():
    """Run test cases for log parsing."""

    # Test Case 1: Basic log with metadata
    log1 = "[2024-01-15 10:30:45] ERROR: Database connection failed | host=db.example.com port=5432"
    result1 = parse_log_entry(log1)
    assert result1 is not None, "Test 1 failed: returned None"
    assert result1['level'] == 'ERROR', f"Test 1 failed: wrong level {result1['level']}"
    assert result1['message'] == 'Database connection failed', "Test 1 failed: wrong message"
    print("✓ Test 1 passed: Log with metadata")

    # Test Case 2: Log without metadata
    log2 = "[2024-01-15 10:30:46] INFO: Server started successfully"
    result2 = parse_log_entry(log2)
    assert result2 is not None, "Test 2 failed: returned None"
    assert result2['level'] == 'INFO', "Test 2 failed: wrong level"
    print("✓ Test 2 passed: Log without metadata")

    # Test Case 3: Invalid log format
    log3 = "This is not a valid log"
    result3 = parse_log_entry(log3)
    assert result3 is None, f"Test 3 failed: should return None, got {result3}"
    print("✓ Test 3 passed: Invalid format detected")

    # Test Case 4: Multiple logs
    logs4 = """[2024-01-15 10:30:45] ERROR: Connection failed
[2024-01-15 10:30:46] INFO: Retrying connection"""
    results4 = parse_logs(logs4)
    assert len(results4) == 2, f"Test 4 failed: expected 2 logs, got {len(results4)}"
    print("✓ Test 4 passed: Multiple logs")

    print("\n" + "="*50)
    print("All basic tests passed! ✓")
    print("="*50)


def run_custom_tests():
    """Add your own custom test cases here."""
    print("\nRunning custom tests...")

    # Add your custom test cases here

    print("No custom tests defined yet.")


if __name__ == "__main__":
    print("Testing String Parsing Solution")
    print("="*50 + "\n")

    try:
        run_tests()
        run_custom_tests()
    except AssertionError as e:
        print(f"\n❌ Test failed: {e}")
    except Exception as e:
        print(f"\n❌ Error: {e}")
