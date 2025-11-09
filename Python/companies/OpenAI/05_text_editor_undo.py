#!/usr/bin/env python3
"""
Problem 5: Text Editor with Undo/Redo

Common OpenAI problem - implement a text editor with undo/redo functionality.
Support insert, delete operations with unlimited undo/redo.

Requirements:
- insert(text, position): Insert text at position
- delete(start, end): Delete text from start to end
- undo(): Undo last operation
- redo(): Redo previously undone operation
- get_text(): Get current text content
- Support unlimited undo/redo operations
- Clear redo stack when new operation performed after undo

Example:
    editor = TextEditor()

    editor.insert("hello", 0)      # "hello"
    editor.insert(" world", 5)     # "hello world"
    editor.delete(5, 11)           # "hello"

    editor.undo()                  # "hello world" (undo delete)
    editor.undo()                  # "hello" (undo insert " world")

    editor.redo()                  # "hello world" (redo insert)
    editor.insert("!", 11)         # "hello world!"
    editor.redo()                  # No effect (redo stack cleared)

Advanced Features (Optional):
- cursor position tracking
- select(start, end) and replace_selection(text)
- Support for very large texts (efficient data structure)
- snapshot() and restore(snapshot_id)

Time Complexity:
- insert/delete: O(n) where n is text length (or O(log n) with rope)
- undo/redo: O(n) for reverting operation
- get_text: O(1) if caching, O(n) if rebuilding

Space Complexity: O(k * n) where k=operations, n=avg text length
"""

try:
    import importlib.util
    spec = importlib.util.spec_from_file_location("solution_module",
                                                   "05_text_editor_undo_solution.py")
    solution_module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(solution_module)
    TextEditor = solution_module.TextEditor
except Exception as e:
    print(f"❌ Error importing solution: {e}")
    exit(1)

def test_text_editor():
    print("Testing Text Editor with Undo/Redo...")
    print()

    # Test 1: Basic insert operations
    print("Test 1: Basic insert operations")
    editor1 = TextEditor()
    editor1.insert("hello", 0)
    assert editor1.get_text() == "hello", "Test 1a failed"
    editor1.insert(" world", 5)
    assert editor1.get_text() == "hello world", "Test 1b failed"
    print("✓ Test 1 passed")
    print()

    # Test 2: Delete operations
    print("Test 2: Delete operations")
    editor2 = TextEditor()
    editor2.insert("hello world", 0)
    editor2.delete(5, 11)  # Delete " world"
    assert editor2.get_text() == "hello", "Test 2a failed"
    editor2.delete(0, 5)   # Delete "hello"
    assert editor2.get_text() == "", "Test 2b failed"
    print("✓ Test 2 passed")
    print()

    # Test 3: Undo operations
    print("Test 3: Undo operations")
    editor3 = TextEditor()
    editor3.insert("abc", 0)
    editor3.insert("def", 3)
    assert editor3.get_text() == "abcdef", "Test 3a failed"
    editor3.undo()
    assert editor3.get_text() == "abc", "Test 3b failed"
    editor3.undo()
    assert editor3.get_text() == "", "Test 3c failed"
    print("✓ Test 3 passed")
    print()

    # Test 4: Redo operations
    print("Test 4: Redo operations")
    editor4 = TextEditor()
    editor4.insert("hello", 0)
    editor4.insert(" world", 5)
    editor4.undo()
    assert editor4.get_text() == "hello", "Test 4a failed"
    editor4.redo()
    assert editor4.get_text() == "hello world", "Test 4b failed"
    print("✓ Test 4 passed")
    print()

    # Test 5: Redo stack cleared on new operation
    print("Test 5: New operation clears redo stack")
    editor5 = TextEditor()
    editor5.insert("abc", 0)
    editor5.insert("def", 3)
    editor5.undo()  # "abc"
    editor5.insert("xyz", 3)  # "abcxyz" - clears redo stack
    result = editor5.redo()  # Should have no effect
    assert editor5.get_text() == "abcxyz", "Test 5 failed"
    print("✓ Test 5 passed")
    print()

    # Test 6: Multiple undo/redo
    print("Test 6: Multiple undo/redo sequence")
    editor6 = TextEditor()
    editor6.insert("a", 0)    # "a"
    editor6.insert("b", 1)    # "ab"
    editor6.insert("c", 2)    # "abc"
    editor6.delete(1, 2)      # "ac"

    assert editor6.get_text() == "ac", "Test 6a failed"

    editor6.undo()  # "abc"
    editor6.undo()  # "ab"
    assert editor6.get_text() == "ab", "Test 6b failed"

    editor6.redo()  # "abc"
    editor6.redo()  # "ac"
    assert editor6.get_text() == "ac", "Test 6c failed"
    print("✓ Test 6 passed")
    print()

    # Test 7: Insert at different positions
    print("Test 7: Insert at various positions")
    editor7 = TextEditor()
    editor7.insert("ac", 0)       # "ac"
    editor7.insert("b", 1)        # "abc"
    assert editor7.get_text() == "abc", "Test 7a failed"
    editor7.insert("x", 0)        # "xabc"
    assert editor7.get_text() == "xabc", "Test 7b failed"
    editor7.insert("z", 4)        # "xabcz"
    assert editor7.get_text() == "xabcz", "Test 7c failed"
    print("✓ Test 7 passed")
    print()

    # Test 8: Undo with no operations
    print("Test 8: Undo/redo with empty stacks")
    editor8 = TextEditor()
    result = editor8.undo()  # No effect
    assert editor8.get_text() == "", "Test 8a failed"
    result = editor8.redo()  # No effect
    assert editor8.get_text() == "", "Test 8b failed"
    print("✓ Test 8 passed")
    print()

    # Test 9: Complex sequence
    print("Test 9: Complex edit sequence")
    editor9 = TextEditor()
    editor9.insert("The quick brown fox", 0)
    editor9.delete(4, 10)  # Remove "quick "
    assert editor9.get_text() == "The brown fox", "Test 9a failed"
    editor9.insert("lazy ", 4)
    assert editor9.get_text() == "The lazy brown fox", "Test 9b failed"
    editor9.undo()
    editor9.undo()
    assert editor9.get_text() == "The quick brown fox", "Test 9c failed"
    print("✓ Test 9 passed")
    print()

    print("All tests passed! ✓")

if __name__ == "__main__":
    test_text_editor()
