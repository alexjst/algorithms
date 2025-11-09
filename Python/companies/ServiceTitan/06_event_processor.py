#!/usr/bin/env python3
"""
Problem 6: Event Processing System

ServiceTitan-style system design problem - implement an event processing system
that can subscribe to events, publish events, and process them with handlers.

Requirements:
- subscribe(event_type, handler): Register handler for event type
- unsubscribe(event_type, handler): Remove handler for event type
- publish(event): Publish event to all subscribed handlers
- Support multiple handlers per event type
- Handlers should be called in order of subscription
- Handle errors in handlers gracefully (one handler error shouldn't affect others)

Example:
    processor = EventProcessor()

    def on_user_login(event):
        print(f"User {event['user_id']} logged in")

    def on_user_logout(event):
        print(f"User {event['user_id']} logged out")

    processor.subscribe("user.login", on_user_login)
    processor.subscribe("user.logout", on_user_logout)

    processor.publish({"type": "user.login", "user_id": 123})
    # Prints: User 123 logged in

    processor.publish({"type": "user.logout", "user_id": 123})
    # Prints: User 123 logged out

Advanced Features:
- Priority-based handlers
- Wildcard event subscriptions (e.g., "user.*")
- Event filtering
- Async event processing

Time Complexity:
- subscribe/unsubscribe: O(1)
- publish: O(n) where n is number of handlers for event type

Space Complexity: O(m * n) for m event types and n handlers per type
"""

try:
    import importlib.util
    spec = importlib.util.spec_from_file_location("solution_module",
                                                   "06_event_processor_solution.py")
    solution_module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(solution_module)
    EventProcessor = solution_module.EventProcessor
except Exception as e:
    print(f"❌ Error importing solution: {e}")
    exit(1)

def test_event_processor():
    print("Testing Event Processing System...")
    print()

    # Test 1: Basic subscribe and publish
    print("Test 1: Basic subscribe and publish")
    processor1 = EventProcessor()
    events1 = []

    def handler1(event):
        events1.append(event)

    processor1.subscribe("test.event", handler1)
    processor1.publish({"type": "test.event", "data": "hello"})

    assert len(events1) == 1, "Test 1a failed"
    assert events1[0]["data"] == "hello", "Test 1b failed"
    print("✓ Test 1 passed")
    print()

    # Test 2: Multiple handlers for same event
    print("Test 2: Multiple handlers for same event")
    processor2 = EventProcessor()
    events2 = []

    def handler2a(event):
        events2.append("A")

    def handler2b(event):
        events2.append("B")

    processor2.subscribe("test", handler2a)
    processor2.subscribe("test", handler2b)
    processor2.publish({"type": "test"})

    assert len(events2) == 2, "Test 2a failed"
    assert events2 == ["A", "B"], "Test 2b failed: handlers should be called in order"
    print("✓ Test 2 passed")
    print()

    # Test 3: Unsubscribe handler
    print("Test 3: Unsubscribe handler")
    processor3 = EventProcessor()
    events3 = []

    def handler3(event):
        events3.append(event)

    processor3.subscribe("test", handler3)
    processor3.publish({"type": "test", "msg": "1"})
    processor3.unsubscribe("test", handler3)
    processor3.publish({"type": "test", "msg": "2"})

    assert len(events3) == 1, "Test 3 failed: should only receive first event"
    assert events3[0]["msg"] == "1", "Test 3b failed"
    print("✓ Test 3 passed")
    print()

    # Test 4: Multiple event types
    print("Test 4: Multiple event types")
    processor4 = EventProcessor()
    events4 = {"login": 0, "logout": 0}

    def on_login(event):
        events4["login"] += 1

    def on_logout(event):
        events4["logout"] += 1

    processor4.subscribe("user.login", on_login)
    processor4.subscribe("user.logout", on_logout)
    processor4.publish({"type": "user.login"})
    processor4.publish({"type": "user.login"})
    processor4.publish({"type": "user.logout"})

    assert events4["login"] == 2, "Test 4a failed"
    assert events4["logout"] == 1, "Test 4b failed"
    print("✓ Test 4 passed")
    print()

    # Test 5: Handler error doesn't affect other handlers
    print("Test 5: Error handling")
    processor5 = EventProcessor()
    events5 = []

    def handler5a(event):
        raise ValueError("Handler A error")

    def handler5b(event):
        events5.append("B executed")

    processor5.subscribe("test", handler5a)
    processor5.subscribe("test", handler5b)
    processor5.publish({"type": "test"})

    assert len(events5) == 1, "Test 5 failed: handler B should still execute"
    assert events5[0] == "B executed", "Test 5b failed"
    print("✓ Test 5 passed")
    print()

    # Test 6: Publish to non-existent event type
    print("Test 6: Non-existent event type")
    processor6 = EventProcessor()
    # Should not raise error
    processor6.publish({"type": "non.existent"})
    print("✓ Test 6 passed")
    print()

    # Test 7: Unsubscribe non-existent handler
    print("Test 7: Unsubscribe non-existent handler")
    processor7 = EventProcessor()

    def handler7(event):
        pass

    # Should not raise error
    processor7.unsubscribe("test", handler7)
    print("✓ Test 7 passed")
    print()

    # Test 8: Same handler subscribed multiple times
    print("Test 8: Duplicate handler subscription")
    processor8 = EventProcessor()
    count8 = [0]

    def handler8(event):
        count8[0] += 1

    processor8.subscribe("test", handler8)
    processor8.subscribe("test", handler8)  # Subscribe again
    processor8.publish({"type": "test"})

    # Handler should only be called once (no duplicates)
    assert count8[0] == 1, f"Test 8 failed: handler called {count8[0]} times, expected 1"
    print("✓ Test 8 passed")
    print()

    # Test 9: Complex event data
    print("Test 9: Complex event data")
    processor9 = EventProcessor()
    received9 = []

    def handler9(event):
        received9.append(event)

    processor9.subscribe("order.created", handler9)
    event_data = {
        "type": "order.created",
        "order_id": 12345,
        "customer": {"id": 1, "name": "John Doe"},
        "items": [
            {"product": "Widget", "quantity": 2, "price": 10.99},
            {"product": "Gadget", "quantity": 1, "price": 25.50}
        ],
        "total": 47.48
    }
    processor9.publish(event_data)

    assert len(received9) == 1, "Test 9a failed"
    assert received9[0]["order_id"] == 12345, "Test 9b failed"
    assert received9[0]["customer"]["name"] == "John Doe", "Test 9c failed"
    assert len(received9[0]["items"]) == 2, "Test 9d failed"
    print("✓ Test 9 passed")
    print()

    # Test 10: Multiple subscribe/unsubscribe cycles
    print("Test 10: Multiple subscribe/unsubscribe cycles")
    processor10 = EventProcessor()
    events10 = []

    def handler10(event):
        events10.append(event["msg"])

    processor10.subscribe("test", handler10)
    processor10.publish({"type": "test", "msg": "1"})
    processor10.unsubscribe("test", handler10)
    processor10.publish({"type": "test", "msg": "2"})
    processor10.subscribe("test", handler10)
    processor10.publish({"type": "test", "msg": "3"})

    assert events10 == ["1", "3"], f"Test 10 failed: got {events10}"
    print("✓ Test 10 passed")
    print()

    print("All tests passed! ✓")

if __name__ == "__main__":
    test_event_processor()
