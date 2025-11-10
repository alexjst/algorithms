#!/usr/bin/env python3
"""
Minimal pytest example
"""

# Simple function to test
def add(a, b):
    return a + b


# Test functions - must start with "test_"
def test_add_positive():
    assert add(2, 3) == 5

def test_add_negative():
    assert add(-1, -1) == -2

def test_add_zero():
    assert add(5, 0) == 5


# Optional: organize tests in classes
class TestMultiplication:
    """Class name must start with 'Test'"""

    def multiply(self, a, b):
        return a * b

    def test_multiply_positive(self):
        assert self.multiply(2, 3) == 6

    def test_multiply_zero(self):
        assert self.multiply(5, 0) == 0
