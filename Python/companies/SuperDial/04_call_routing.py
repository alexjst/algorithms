#!/usr/bin/env python3
"""
Problem 4: Intelligent Call Routing System

SuperDial needs to route incoming voice calls to available AI agents.
Implement a load balancer that distributes calls efficiently across agents
while considering agent capacity and specialization.

Requirements:
- Route calls to least loaded available agent
- Support agent specialization (e.g., "cardiology", "general")
- Track active calls per agent
- Handle agent availability (online/offline)
- Return None if no agents available

Example:
    router = CallRouter()
    router.add_agent("agent1", capacity=5, specialization="cardiology")
    router.add_agent("agent2", capacity=3, specialization="general")

    router.route_call("call1", specialty="cardiology")  # Returns "agent1"
    router.route_call("call2", specialty="general")     # Returns "agent2"
    router.end_call("call1")                             # Frees "agent1"

Time Complexity: O(n) where n is number of agents
Space Complexity: O(a + c) where a is agents, c is active calls
"""

# Import the solution
try:
    import importlib.util
    spec = importlib.util.spec_from_file_location(
        "solution_module",
        "04_call_routing_solution.py"
    )
    solution_module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(solution_module)
    CallRouter = solution_module.CallRouter
except Exception as e:
    print(f"❌ Error importing solution: {e}")
    print(f"   Make sure 04_call_routing_solution.py exists.")
    exit(1)

def test_call_routing():
    """Test the call routing implementation."""

    print("Testing Call Routing System...")
    print()

    # Test 1: Basic routing to available agent
    print("Test 1: Basic routing to available agent")
    router1 = CallRouter()
    router1.add_agent("agent1", capacity=2, specialization="general")
    result1 = router1.route_call("call1", specialty="general")
    assert result1 == "agent1", f"Test 1 failed: expected 'agent1', got '{result1}'"
    print("✓ Test 1 passed: Basic routing works")
    print()

    # Test 2: Load balancing - route to least loaded
    print("Test 2: Load balancing across agents")
    router2 = CallRouter()
    router2.add_agent("agent1", capacity=3, specialization="general")
    router2.add_agent("agent2", capacity=3, specialization="general")
    router2.route_call("call1", specialty="general")  # Goes to agent1
    router2.route_call("call2", specialty="general")  # Goes to agent2 (load balance)
    # Both agents have 1 call, so next call can go to either
    result2 = router2.route_call("call3", specialty="general")
    assert result2 in ["agent1", "agent2"], f"Test 2 failed: expected agent1 or agent2, got '{result2}'"
    print("✓ Test 2 passed: Load balancing works")
    print()

    # Test 3: Capacity limit
    print("Test 3: Capacity limit enforcement")
    router3 = CallRouter()
    router3.add_agent("agent1", capacity=2, specialization="general")
    router3.route_call("call1", specialty="general")
    router3.route_call("call2", specialty="general")
    result3 = router3.route_call("call3", specialty="general")
    assert result3 is None, f"Test 3 failed: expected None (capacity full), got '{result3}'"
    print("✓ Test 3 passed: Capacity limit enforced")
    print()

    # Test 4: Specialization matching
    print("Test 4: Specialization matching")
    router4 = CallRouter()
    router4.add_agent("agent1", capacity=2, specialization="cardiology")
    router4.add_agent("agent2", capacity=2, specialization="general")
    result4a = router4.route_call("call1", specialty="cardiology")
    result4b = router4.route_call("call2", specialty="general")
    assert result4a == "agent1", f"Test 4a failed: expected 'agent1', got '{result4a}'"
    assert result4b == "agent2", f"Test 4b failed: expected 'agent2', got '{result4b}'"
    print("✓ Test 4 passed: Specialization matching works")
    print()

    # Test 5: Call completion frees capacity
    print("Test 5: Call completion frees capacity")
    router5 = CallRouter()
    router5.add_agent("agent1", capacity=1, specialization="general")
    router5.route_call("call1", specialty="general")
    assert router5.route_call("call2", specialty="general") is None, "Test 5a failed: should be at capacity"
    router5.end_call("call1")
    result5 = router5.route_call("call2", specialty="general")
    assert result5 == "agent1", f"Test 5b failed: expected 'agent1', got '{result5}'"
    print("✓ Test 5 passed: Call completion frees capacity")
    print()

    # Test 6: Agent offline/online
    print("Test 6: Agent availability management")
    router6 = CallRouter()
    router6.add_agent("agent1", capacity=2, specialization="general")
    router6.set_agent_status("agent1", online=False)
    result6a = router6.route_call("call1", specialty="general")
    assert result6a is None, f"Test 6a failed: expected None (agent offline), got '{result6a}'"
    router6.set_agent_status("agent1", online=True)
    result6b = router6.route_call("call1", specialty="general")
    assert result6b == "agent1", f"Test 6b failed: expected 'agent1', got '{result6b}'"
    print("✓ Test 6 passed: Agent availability management works")
    print()

    print("All tests passed! ✓")

if __name__ == "__main__":
    test_call_routing()
