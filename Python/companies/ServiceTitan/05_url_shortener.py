#!/usr/bin/env python3
"""
Problem 5: URL Shortener Service

Actual ServiceTitan interview question - design and implement a URL shortening service.

Requirements:
- encode(longUrl): Convert long URL to short URL
- decode(shortUrl): Convert short URL back to long URL
- Short URLs must be unique
- Handle collisions
- Thread-safe operations (bonus)

Example:
    shortener = URLShortener()

    short1 = shortener.encode("https://www.example.com/very/long/url/path")
    # Returns something like "http://short.url/abc123"

    long1 = shortener.decode(short1)
    # Returns "https://www.example.com/very/long/url/path"

    # Same long URL should return same short URL
    short2 = shortener.encode("https://www.example.com/very/long/url/path")
    assert short1 == short2

Approach:
1. Use base62 encoding (a-z, A-Z, 0-9) for short codes
2. Maintain bidirectional mapping (long -> short, short -> long)
3. Counter-based approach: increment counter and encode to base62
4. Or hash-based approach: hash long URL and handle collisions

Time Complexity: O(1) for both encode and decode
Space Complexity: O(n) for n URLs
"""

try:
    import importlib.util
    spec = importlib.util.spec_from_file_location("solution_module",
                                                   "05_url_shortener_solution.py")
    solution_module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(solution_module)
    URLShortener = solution_module.URLShortener
except Exception as e:
    print(f"❌ Error importing solution: {e}")
    exit(1)

def test_url_shortener():
    print("Testing URL Shortener...")
    print()

    # Test 1: Basic encode and decode
    print("Test 1: Basic encode and decode")
    shortener1 = URLShortener()
    long_url1 = "https://www.example.com/path/to/page"
    short_url1 = shortener1.encode(long_url1)
    decoded1 = shortener1.decode(short_url1)
    assert decoded1 == long_url1, f"Test 1 failed: {decoded1} != {long_url1}"
    print("✓ Test 1 passed")
    print()

    # Test 2: Same URL returns same short URL
    print("Test 2: Same URL returns same short URL")
    shortener2 = URLShortener()
    url2 = "https://www.google.com"
    short1 = shortener2.encode(url2)
    short2 = shortener2.encode(url2)
    assert short1 == short2, f"Test 2 failed: {short1} != {short2}"
    print("✓ Test 2 passed")
    print()

    # Test 3: Different URLs return different short URLs
    print("Test 3: Different URLs return different short URLs")
    shortener3 = URLShortener()
    url3a = "https://www.example.com/page1"
    url3b = "https://www.example.com/page2"
    short3a = shortener3.encode(url3a)
    short3b = shortener3.encode(url3b)
    assert short3a != short3b, f"Test 3 failed: {short3a} == {short3b}"
    print("✓ Test 3 passed")
    print()

    # Test 4: Decode non-existent short URL
    print("Test 4: Decode non-existent short URL")
    shortener4 = URLShortener()
    result4 = shortener4.decode("http://short.url/invalid")
    assert result4 is None or result4 == "", "Test 4 failed: should return None or empty string"
    print("✓ Test 4 passed")
    print()

    # Test 5: Multiple URLs
    print("Test 5: Multiple URLs")
    shortener5 = URLShortener()
    urls = [
        "https://www.site1.com",
        "https://www.site2.com",
        "https://www.site3.com",
        "https://www.site4.com",
        "https://www.site5.com",
    ]
    short_urls = [shortener5.encode(url) for url in urls]

    # All short URLs should be unique
    assert len(short_urls) == len(set(short_urls)), "Test 5a failed: duplicate short URLs"

    # All should decode correctly
    for i, url in enumerate(urls):
        decoded = shortener5.decode(short_urls[i])
        assert decoded == url, f"Test 5b failed at index {i}: {decoded} != {url}"
    print("✓ Test 5 passed")
    print()

    # Test 6: Very long URL
    print("Test 6: Very long URL")
    shortener6 = URLShortener()
    long_url6 = "https://www.example.com/" + "a" * 1000
    short_url6 = shortener6.encode(long_url6)
    decoded6 = shortener6.decode(short_url6)
    assert decoded6 == long_url6, "Test 6 failed"
    # Short URL should be much shorter than long URL
    assert len(short_url6) < len(long_url6), "Test 6b failed: short URL not shorter"
    print("✓ Test 6 passed")
    print()

    # Test 7: URL with query parameters
    print("Test 7: URL with query parameters")
    shortener7 = URLShortener()
    url7 = "https://www.example.com/search?q=test&page=1&limit=10"
    short7 = shortener7.encode(url7)
    decoded7 = shortener7.decode(short7)
    assert decoded7 == url7, "Test 7 failed"
    print("✓ Test 7 passed")
    print()

    # Test 8: Sequential encoding
    print("Test 8: Sequential encoding")
    shortener8 = URLShortener()
    short_urls8 = []
    for i in range(100):
        url = f"https://www.example.com/page{i}"
        short = shortener8.encode(url)
        short_urls8.append(short)

    # All should be unique
    assert len(short_urls8) == len(set(short_urls8)), "Test 8a failed"

    # All should decode correctly
    for i in range(100):
        url = f"https://www.example.com/page{i}"
        decoded = shortener8.decode(short_urls8[i])
        assert decoded == url, f"Test 8b failed at {i}"
    print("✓ Test 8 passed")
    print()

    # Test 9: URLs with special characters
    print("Test 9: URLs with special characters")
    shortener9 = URLShortener()
    url9 = "https://www.example.com/path?name=John%20Doe&age=30"
    short9 = shortener9.encode(url9)
    decoded9 = shortener9.decode(short9)
    assert decoded9 == url9, "Test 9 failed"
    print("✓ Test 9 passed")
    print()

    print("All tests passed! ✓")

if __name__ == "__main__":
    test_url_shortener()
