#!/usr/bin/env python3
"""
Problem 2: Streaming Data Buffer Management

SuperDial processes real-time voice transcription data in chunks.
Implement a circular buffer that efficiently manages streaming data.

Requirements:
- Fixed-size buffer with efficient write/read operations
- Support for writing chunks of data
- Support for reading all available data
- Handle buffer overflow (old data overwritten)
- Track number of bytes written and available

Example:
    buffer = StreamingBuffer(capacity=10)
    buffer.write("Hello")      # Returns 5 (bytes written)
    buffer.write(" World")     # Returns 6
    buffer.read()              # Returns "Hello Worl" (last 10 bytes)
    buffer.available()         # Returns 10

Time Complexity: O(n) for write/read where n is data size
Space Complexity: O(capacity)
"""

# Import the solution
try:
    import importlib.util
    spec = importlib.util.spec_from_file_location(
        "solution_module",
        "02_streaming_buffer_solution.py"
    )
    solution_module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(solution_module)
    StreamingBuffer = solution_module.StreamingBuffer
except Exception as e:
    print(f"❌ Error importing solution: {e}")
    print(f"   Make sure 02_streaming_buffer_solution.py exists.")
    exit(1)

def test_streaming_buffer():
    """Test the streaming buffer implementation."""

    print("Testing Streaming Buffer...")
    print()

    # Test 1: Basic write and read
    print("Test 1: Basic write and read")
    buffer1 = StreamingBuffer(capacity=10)
    written = buffer1.write("Hello")
    assert written == 5, f"Test 1a failed: expected 5 bytes written, got {written}"
    data = buffer1.read()
    assert data == "Hello", f"Test 1b failed: expected 'Hello', got '{data}'"
    assert buffer1.available() == 5, f"Test 1c failed: expected 5 bytes available, got {buffer1.available()}"
    print("✓ Test 1 passed: Basic write and read work")
    print()

    # Test 2: Buffer overflow (circular behavior)
    print("Test 2: Buffer overflow handling")
    buffer2 = StreamingBuffer(capacity=5)
    buffer2.write("Hello")
    buffer2.write("World")  # Should overwrite "Hello"
    data = buffer2.read()
    assert data == "World", f"Test 2 failed: expected 'World', got '{data}'"
    assert buffer2.available() == 5, f"Test 2 failed: expected 5 bytes available, got {buffer2.available()}"
    print("✓ Test 2 passed: Buffer overflow handled correctly")
    print()

    # Test 3: Multiple writes and reads
    print("Test 3: Multiple writes and reads")
    buffer3 = StreamingBuffer(capacity=15)
    buffer3.write("Hello ")
    buffer3.write("World!")
    assert buffer3.available() == 12, f"Test 3a failed: expected 12 bytes available, got {buffer3.available()}"
    data = buffer3.read()
    assert data == "Hello World!", f"Test 3b failed: expected 'Hello World!', got '{data}'"
    print("✓ Test 3 passed: Multiple writes and reads work")
    print()

    # Test 4: Empty buffer
    print("Test 4: Empty buffer")
    buffer4 = StreamingBuffer(capacity=10)
    assert buffer4.available() == 0, f"Test 4a failed: expected 0 bytes available, got {buffer4.available()}"
    data = buffer4.read()
    assert data == "", f"Test 4b failed: expected empty string, got '{data}'"
    print("✓ Test 4 passed: Empty buffer handled")
    print()

    # Test 5: Exact capacity
    print("Test 5: Writing exactly buffer capacity")
    buffer5 = StreamingBuffer(capacity=8)
    buffer5.write("12345678")
    assert buffer5.available() == 8, f"Test 5a failed: expected 8 bytes available, got {buffer5.available()}"
    data = buffer5.read()
    assert data == "12345678", f"Test 5b failed: expected '12345678', got '{data}'"
    print("✓ Test 5 passed: Exact capacity write works")
    print()

    print("All tests passed! ✓")

if __name__ == "__main__":
    test_streaming_buffer()
