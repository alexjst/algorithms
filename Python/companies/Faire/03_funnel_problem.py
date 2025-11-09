#!/usr/bin/env python3
"""
Problem 4: Funnel Problem

Analyze conversion funnel for e-commerce platform. Users go through stages:
Browse -> View -> Cart -> Checkout -> Purchase

Given user events, calculate conversion rates and find drop-off stages.

Example:
    Input: [
        ('u1', 'Browse', 100),
        ('u1', 'View', 105),
        ('u1', 'Cart', 110),
        ('u1', 'Purchase', 120),
        ('u2', 'Browse', 100),
        ('u2', 'View', 105),
        ('u3', 'Browse', 101),
    ]

    Funnel:
        Browse: 3 users
        View: 2 users (66.7% conversion)
        Cart: 1 user (50% conversion)
        Purchase: 1 user (100% conversion)

Constraints:
    - 1 <= events <= 10^5
    - Events: (user_id, stage, timestamp)
    - Users counted once per stage
    - Stages in order: Browse, View, Cart, Checkout, Purchase - TEST SCAFFOLDING (DO NOT EDIT)

================================================================================
INSTRUCTIONS:
- Implement your solution in: 04_funnel_problem_solution.py
- Run this file to test: python 04_funnel_problem.py
- To reset and practice again: just delete/reset the solution file
================================================================================
"""

# Import the solution
try:
    import importlib.util
    spec = importlib.util.spec_from_file_location(
        "solution_module",
        "03_funnel_problem_solution.py"
    )
    solution_module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(solution_module)
    FunnelAnalyzer = solution_module.FunnelAnalyzer
except Exception as e:
    print(f"❌ Error importing solution: {e}")
    print(f"   Make sure 03_funnel_problem_solution.py exists.")
    exit(1)

def run_tests():
    """Run test cases for FunnelAnalyzer."""

    # Test Case 1: Basic funnel
    events1 = [
        ('u1', 'Browse', 1), ('u1', 'View', 2),
        ('u2', 'Browse', 1)
    ]
    analyzer1 = FunnelAnalyzer(events1)
    metrics1 = analyzer1.get_funnel_metrics()
    # Should be able to create analyzer
    assert isinstance(metrics1, dict), "Test 1 failed: metrics should be a dict"
    print("✓ Test 1 passed: Basic funnel created")

    # Test Case 2: Complete journey
    events2 = [
        ('u1', 'Browse', 1),
        ('u1', 'View', 2),
        ('u1', 'Cart', 3),
        ('u1', 'Checkout', 4),
        ('u1', 'Purchase', 5)
    ]
    analyzer2 = FunnelAnalyzer(events2)
    metrics2 = analyzer2.get_funnel_metrics()
    assert isinstance(metrics2, dict), "Test 2 failed: metrics should be a dict"
    print("✓ Test 2 passed: Complete user journey")

    # Test Case 3: Drop-off detection
    events3 = [
        ('u1', 'Browse', 1), ('u1', 'View', 2),
        ('u2', 'Browse', 1), ('u2', 'View', 2),
        ('u3', 'Browse', 1), ('u3', 'View', 2),
        ('u1', 'Cart', 3)  # Only u1 proceeds
    ]
    analyzer3 = FunnelAnalyzer(events3)
    dropoff_stage, rate = analyzer3.find_dropoff_stage()
    # Should find View->Cart as biggest drop-off (3 users to 1 user = 66.7% drop)
    assert dropoff_stage != "", f"Test 3 failed: should identify drop-off stage, got empty string"
    print("✓ Test 3 passed: Drop-off detection")

    print("\n" + "="*50)
    print("All basic tests passed! ✓")
    print("="*50)



def run_custom_tests():
    """Add your own custom test cases here."""
    print("\nRunning custom tests...")

    # Add your custom test cases here

    print("No custom tests defined yet.")



if __name__ == "__main__":
    print("Testing Funnel Analyzer Solution")
    print("="*50 + "\n")

    try:
        run_tests()
        run_custom_tests()
    except AssertionError as e:
        print(f"\n❌ Test failed: {e}")
    except Exception as e:
        print(f"\n❌ Error: {e}")
