#!/usr/bin/env python3
"""
Solution for Problem 4: Intelligent Call Routing System

TODO: Implement the CallRouter class below.
"""

from typing import Optional, Dict, Set

class CallRouter:
    """
    Load balancer for routing calls to AI agents.
    """

    def __init__(self):
        """Initialize the call router."""
        # TODO: Implement initialization
        # You'll need to track:
        # - Agents and their properties (capacity, specialization, status)
        # - Active calls per agent
        # - Call to agent mapping
        pass

    def add_agent(self, agent_id: str, capacity: int, specialization: str) -> None:
        """
        Add a new agent to the routing pool.

        Args:
            agent_id: Unique identifier for the agent
            capacity: Maximum number of concurrent calls
            specialization: Agent's specialty (e.g., "cardiology", "general")
        """
        # TODO: Implement agent addition
        pass

    def route_call(self, call_id: str, specialty: str) -> Optional[str]:
        """
        Route a call to the best available agent.

        Args:
            call_id: Unique identifier for the call
            specialty: Required specialty for the call

        Returns:
            Agent ID if routing successful, None if no agent available
        """
        # TODO: Implement call routing
        # Hints:
        # 1. Filter agents by specialization and online status
        # 2. Find agent with lowest current load that has capacity
        # 3. Assign call to that agent
        # 4. Return agent ID or None
        pass

    def end_call(self, call_id: str) -> None:
        """
        Mark a call as ended and free up agent capacity.

        Args:
            call_id: Unique identifier for the call
        """
        # TODO: Implement call completion
        # Remove call from agent's active calls
        pass

    def set_agent_status(self, agent_id: str, online: bool) -> None:
        """
        Set agent availability status.

        Args:
            agent_id: Unique identifier for the agent
            online: True if agent is online, False if offline
        """
        # TODO: Implement status change
        pass
