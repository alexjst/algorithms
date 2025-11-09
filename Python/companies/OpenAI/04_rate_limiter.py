#!/usr/bin/env python3
"""
Problem 4: Rate Limiter

Common OpenAI problem - implement a thread-safe rate limiter.
Support multiple rate limiting algorithms and handle concurrent requests.

Requirements:
- is_allowed(user_id, timestamp): Check if request is allowed
- Support different algorithms: Fixed Window, Sliding Window, Token Bucket
- Thread-safe implementation
- Efficient memory usage (cleanup old entries)

Example (Fixed Window - 3 requests per 10 seconds):
    limiter = RateLimiter(max_requests=3, window_seconds=10)

    limiter.is_allowed("user1", 0)   # True (1/3)
    limiter.is_allowed("user1", 1)   # True (2/3)
    limiter.is_allowed("user1", 2)   # True (3/3)
    limiter.is_allowed("user1", 3)   # False (limit reached)
    limiter.is_allowed("user1", 10)  # True (new window, 1/3)

Example (Sliding Window):
    limiter = SlidingWindowRateLimiter(max_requests=3, window_seconds=10)

    limiter.is_allowed("user1", 0)   # True
    limiter.is_allowed("user1", 5)   # True
    limiter.is_allowed("user1", 8)   # True
    limiter.is_allowed("user1", 9)   # False (3 requests in last 10s)
    limiter.is_allowed("user1", 11)  # True (oldest request at t=0 expired)

Time Complexity:
- Fixed Window: O(1)
- Sliding Window: O(n) where n = requests in window
- Token Bucket: O(1)

Space Complexity: O(u * r) where u=users, r=requests per window
"""

try:
    import importlib.util
    spec = importlib.util.spec_from_file_location("solution_module",
                                                   "04_rate_limiter_solution.py")
    solution_module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(solution_module)
    FixedWindowRateLimiter = solution_module.FixedWindowRateLimiter
    SlidingWindowRateLimiter = solution_module.SlidingWindowRateLimiter
    TokenBucketRateLimiter = solution_module.TokenBucketRateLimiter
except Exception as e:
    print(f"❌ Error importing solution: {e}")
    exit(1)

def test_fixed_window_rate_limiter():
    print("Testing Fixed Window Rate Limiter...")
    print()

    # Test 1: Basic limiting
    print("Test 1: Basic rate limiting (3 requests per 10 seconds)")
    limiter1 = FixedWindowRateLimiter(max_requests=3, window_seconds=10)
    assert limiter1.is_allowed("user1", 0) == True, "Test 1a failed"
    assert limiter1.is_allowed("user1", 1) == True, "Test 1b failed"
    assert limiter1.is_allowed("user1", 2) == True, "Test 1c failed"
    assert limiter1.is_allowed("user1", 3) == False, "Test 1d failed"
    print("✓ Test 1 passed")
    print()

    # Test 2: Window reset
    print("Test 2: Window resets after time period")
    limiter2 = FixedWindowRateLimiter(max_requests=2, window_seconds=5)
    assert limiter2.is_allowed("user1", 0) == True, "Test 2a failed"
    assert limiter2.is_allowed("user1", 1) == True, "Test 2b failed"
    assert limiter2.is_allowed("user1", 2) == False, "Test 2c failed"
    assert limiter2.is_allowed("user1", 5) == True, "Test 2d failed: new window"
    print("✓ Test 2 passed")
    print()

    # Test 3: Multiple users
    print("Test 3: Independent limits per user")
    limiter3 = FixedWindowRateLimiter(max_requests=2, window_seconds=10)
    assert limiter3.is_allowed("user1", 0) == True, "Test 3a failed"
    assert limiter3.is_allowed("user1", 1) == True, "Test 3b failed"
    assert limiter3.is_allowed("user2", 1) == True, "Test 3c failed"
    assert limiter3.is_allowed("user2", 2) == True, "Test 3d failed"
    assert limiter3.is_allowed("user1", 2) == False, "Test 3e failed"
    assert limiter3.is_allowed("user2", 3) == False, "Test 3f failed"
    print("✓ Test 3 passed")
    print()

    print("All Fixed Window tests passed! ✓")

def test_sliding_window_rate_limiter():
    print("\nTesting Sliding Window Rate Limiter...")
    print()

    # Test 1: Sliding window behavior
    print("Test 1: Sliding window (3 requests per 10 seconds)")
    limiter1 = SlidingWindowRateLimiter(max_requests=3, window_seconds=10)
    assert limiter1.is_allowed("user1", 0) == True, "Test 1a failed"
    assert limiter1.is_allowed("user1", 5) == True, "Test 1b failed"
    assert limiter1.is_allowed("user1", 8) == True, "Test 1c failed"
    assert limiter1.is_allowed("user1", 9) == False, "Test 1d failed"
    assert limiter1.is_allowed("user1", 11) == True, "Test 1e failed: t=0 expired"
    print("✓ Test 1 passed")
    print()

    # Test 2: Old requests expire
    print("Test 2: Old requests expire from window")
    limiter2 = SlidingWindowRateLimiter(max_requests=2, window_seconds=5)
    assert limiter2.is_allowed("user1", 0) == True, "Test 2a failed"
    assert limiter2.is_allowed("user1", 3) == True, "Test 2b failed"
    assert limiter2.is_allowed("user1", 4) == False, "Test 2c failed"
    assert limiter2.is_allowed("user1", 6) == True, "Test 2d failed: t=0 expired"
    print("✓ Test 2 passed")
    print()

    print("All Sliding Window tests passed! ✓")

def test_token_bucket_rate_limiter():
    print("\nTesting Token Bucket Rate Limiter...")
    print()

    # Test 1: Token bucket with refill
    print("Test 1: Token bucket (capacity=3, refill=1 per second)")
    limiter1 = TokenBucketRateLimiter(capacity=3, refill_rate=1.0)
    assert limiter1.is_allowed("user1", 0) == True, "Test 1a failed"
    assert limiter1.is_allowed("user1", 0) == True, "Test 1b failed"
    assert limiter1.is_allowed("user1", 0) == True, "Test 1c failed"
    assert limiter1.is_allowed("user1", 0) == False, "Test 1d failed: no tokens"
    assert limiter1.is_allowed("user1", 1) == True, "Test 1e failed: 1 token refilled"
    print("✓ Test 1 passed")
    print()

    # Test 2: Burst handling
    print("Test 2: Handle burst after waiting")
    limiter2 = TokenBucketRateLimiter(capacity=2, refill_rate=1.0)
    assert limiter2.is_allowed("user1", 0) == True, "Test 2a failed"
    assert limiter2.is_allowed("user1", 0) == True, "Test 2b failed"
    assert limiter2.is_allowed("user1", 0) == False, "Test 2c failed"
    # After 3 seconds, should have 2 tokens (capped at capacity)
    assert limiter2.is_allowed("user1", 3) == True, "Test 2d failed"
    assert limiter2.is_allowed("user1", 3) == True, "Test 2e failed"
    print("✓ Test 2 passed")
    print()

    print("All Token Bucket tests passed! ✓")

if __name__ == "__main__":
    test_fixed_window_rate_limiter()
    test_sliding_window_rate_limiter()
    test_token_bucket_rate_limiter()
    print("\n" + "="*50)
    print("All Rate Limiter tests passed! ✓")
