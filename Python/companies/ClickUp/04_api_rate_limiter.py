#!/usr/bin/env python3
"""
Problem 04: API Rate Limiter

Design a rate limiter that restricts the number of API requests a user can make within a time window.

Example:
    limiter = RateLimiter(max_requests=3, window_seconds=60)
limiter.is_allowed("user1", 0)   # True

Constraints:
    - Support sliding window rate limiting
    - Track requests per user

================================================================================
INSTRUCTIONS:
- Implement your solution in: 04_api_rate_limiter_solution.py
- Run this file to test: python 04_api_rate_limiter.py
- To reset and practice again: just delete/reset the solution file
================================================================================
"""

# Import the solution
try:
    import importlib.util
    spec = importlib.util.spec_from_file_location(
        "solution_module",
        "04_api_rate_limiter_solution.py"
    )
    solution_module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(solution_module)
    RateLimiter = solution_module.RateLimiter
except Exception as e:
    print(f"❌ Error importing solution: {e}")
    print(f"   Make sure 04_api_rate_limiter_solution.py exists.")
    exit(1)

def run_tests():
    """Run test cases for api rate limiter."""

    # Test Case 1: rate limiting
    limiter = RateLimiter(3, 60)
    assert limiter.is_allowed("user1", 0) == True
    assert limiter.is_allowed("user1", 10) == True
    assert limiter.is_allowed("user1", 20) == True
    assert limiter.is_allowed("user1", 30) == False
    print("✓ Test 1 passed: rate limiting")

    print("\n" + "="*50)
    print("All basic tests passed! ✓")
    print("="*50)


def run_custom_tests():
    """Add your own custom test cases here."""
    print("\nRunning custom tests...")
    print("No custom tests defined yet.")


if __name__ == "__main__":
    print("Testing API Rate Limiter Solution")
    print("="*50 + "\n")

    try:
        run_tests()
        run_custom_tests()
    except AssertionError as e:
        print(f"\n❌ Test failed: {e}")
    except Exception as e:
        print(f"\n❌ Error: {e}")
