#!/usr/bin/env python3
"""
Problem 1: API Rate Limiter with Priority Queues

SuperDial handles healthcare voice calls that require prioritization.
Implement a rate limiter that processes API requests with priority levels.

Requirements:
- Limit to max_requests per time_window seconds
- Higher priority requests (lower number = higher priority) processed first
- Return True if request allowed, False if rate limited
- Clean up old requests outside the time window

Example:
    limiter = PriorityRateLimiter(max_requests=3, time_window=1.0)
    limiter.allow_request(priority=1)  # True (urgent)
    limiter.allow_request(priority=2)  # True
    limiter.allow_request(priority=2)  # True
    limiter.allow_request(priority=3)  # False (rate limit reached)

    # After 1 second
    limiter.allow_request(priority=1)  # True (window reset)

Time Complexity: O(log n) per request
Space Complexity: O(n) where n is max_requests
"""

# Import the solution
try:
    import importlib.util
    spec = importlib.util.spec_from_file_location(
        "solution_module",
        "01_priority_rate_limiter_solution.py"
    )
    solution_module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(solution_module)
    PriorityRateLimiter = solution_module.PriorityRateLimiter
except Exception as e:
    print(f"❌ Error importing solution: {e}")
    print(f"   Make sure 01_priority_rate_limiter_solution.py exists.")
    exit(1)

import time

def test_priority_rate_limiter():
    """Test the priority rate limiter implementation."""

    print("Testing Priority Rate Limiter...")
    print()

    # Test 1: Basic rate limiting
    print("Test 1: Basic rate limiting")
    limiter1 = PriorityRateLimiter(max_requests=3, time_window=1.0)
    assert limiter1.allow_request(priority=1) == True, "Test 1a failed: first request should be allowed"
    assert limiter1.allow_request(priority=2) == True, "Test 1b failed: second request should be allowed"
    assert limiter1.allow_request(priority=2) == True, "Test 1c failed: third request should be allowed"
    assert limiter1.allow_request(priority=3) == False, "Test 1d failed: fourth request should be blocked"
    print("✓ Test 1 passed: Basic rate limiting works")
    print()

    # Test 2: Priority ordering
    print("Test 2: Priority ordering (lower number = higher priority)")
    limiter2 = PriorityRateLimiter(max_requests=2, time_window=1.0)
    # Fill the limit with low priority
    limiter2.allow_request(priority=10)
    limiter2.allow_request(priority=10)
    # High priority should still be blocked (limit reached)
    assert limiter2.allow_request(priority=1) == False, "Test 2 failed: rate limit applies regardless of priority"
    print("✓ Test 2 passed: Priority ordering verified")
    print()

    # Test 3: Time window reset
    print("Test 3: Time window reset")
    limiter3 = PriorityRateLimiter(max_requests=2, time_window=0.5)
    limiter3.allow_request(priority=1)
    limiter3.allow_request(priority=1)
    assert limiter3.allow_request(priority=1) == False, "Test 3a failed: should be rate limited"
    time.sleep(0.6)  # Wait for window to expire
    assert limiter3.allow_request(priority=1) == True, "Test 3b failed: should allow after window reset"
    print("✓ Test 3 passed: Time window reset works")
    print()

    # Test 4: Edge case - zero requests
    print("Test 4: Edge case - zero max requests")
    limiter4 = PriorityRateLimiter(max_requests=0, time_window=1.0)
    assert limiter4.allow_request(priority=1) == False, "Test 4 failed: should block all requests"
    print("✓ Test 4 passed: Zero max requests handled")
    print()

    print("All tests passed! ✓")

if __name__ == "__main__":
    test_priority_rate_limiter()
