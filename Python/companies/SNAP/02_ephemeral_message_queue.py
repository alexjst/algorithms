#!/usr/bin/env python3
"""
Problem 2: Ephemeral Message Queue

Snapchat's core feature is ephemeral messaging - messages that disappear after viewing or after time.
Implement a message queue with time-to-live (TTL) functionality.

Requirements:
- Add messages with expiration time
- Retrieve messages before they expire
- Auto-delete expired messages
- Track message delivery status

Example:
    queue = EphemeralMessageQueue()
    
    queue.send_message("user1", "user2", "Hello!", ttl_seconds=10)
    queue.send_message("user1", "user2", "How are you?", ttl_seconds=5)
    
    # After 6 seconds
    messages = queue.get_messages("user2")
    # Returns: ["Hello!"]  (second message expired)
    
    queue.mark_viewed("user2", message_id=1)
    # Message auto-deleted after viewing

Time Complexity: O(log n) for send, O(n) for cleanup
Space Complexity: O(n) where n is number of messages
"""

try:
    import importlib.util
    spec = importlib.util.spec_from_file_location(
        "solution_module",
        "02_ephemeral_message_queue_solution.py"
    )
    solution_module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(solution_module)
    EphemeralMessageQueue = solution_module.EphemeralMessageQueue
except Exception as e:
    print(f"❌ Error importing solution: {e}")
    print(f"   Make sure 02_ephemeral_message_queue_solution.py exists.")
    exit(1)

import time

def test_ephemeral_queue():
    print("Testing Ephemeral Message Queue...")
    print()

    # Test 1: Basic send and receive
    print("Test 1: Basic send and receive")
    queue1 = EphemeralMessageQueue()
    queue1.send_message("alice", "bob", "Hi Bob!", ttl_seconds=10)
    messages1 = queue1.get_messages("bob")
    assert len(messages1) == 1, f"Test 1 failed: expected 1 message, got {len(messages1)}"
    assert messages1[0]["content"] == "Hi Bob!", f"Test 1 failed: wrong content"
    print("✓ Test 1 passed")
    print()

    # Test 2: Message expiration
    print("Test 2: Message expiration")
    queue2 = EphemeralMessageQueue()
    queue2.send_message("alice", "bob", "Quick message", ttl_seconds=1)
    time.sleep(1.5)
    messages2 = queue2.get_messages("bob")
    assert len(messages2) == 0, f"Test 2 failed: expected 0 messages after expiry, got {len(messages2)}"
    print("✓ Test 2 passed")
    print()

    # Test 3: View and delete
    print("Test 3: View and delete")
    queue3 = EphemeralMessageQueue()
    msg_id = queue3.send_message("alice", "bob", "Delete after view", ttl_seconds=100)
    queue3.mark_viewed("bob", msg_id)
    messages3 = queue3.get_messages("bob")
    assert len(messages3) == 0, f"Test 3 failed: message should be deleted after viewing"
    print("✓ Test 3 passed")
    print()

    # Test 4: Multiple recipients
    print("Test 4: Multiple recipients")
    queue4 = EphemeralMessageQueue()
    queue4.send_message("alice", "bob", "To Bob", ttl_seconds=10)
    queue4.send_message("alice", "charlie", "To Charlie", ttl_seconds=10)
    bob_msgs = queue4.get_messages("bob")
    charlie_msgs = queue4.get_messages("charlie")
    assert len(bob_msgs) == 1 and len(charlie_msgs) == 1, "Test 4 failed: wrong message routing"
    print("✓ Test 4 passed")
    print()

    print("All tests passed! ✓")

if __name__ == "__main__":
    test_ephemeral_queue()
