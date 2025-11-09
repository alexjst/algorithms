#!/usr/bin/env python3
"""Solution for Problem 5: URL Shortener Service"""

from typing import Optional
import hashlib

class URLShortener:
    def __init__(self, base_url: str = "http://short.url/"):
        """
        Initialize URL shortener.

        TODO: Implement initialization
        Hints:
        1. Need two mappings:
           - long_to_short: map long URLs to short codes
           - short_to_long: map short codes to long URLs
        2. Need counter for generating unique IDs (counter-based approach)
        3. Or use hash function for generating codes (hash-based approach)
        4. Store base URL for constructing short URLs

        Counter-Based Approach:
        self.long_to_short = {}
        self.short_to_long = {}
        self.counter = 0
        self.base_url = base_url
        self.charset = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

        Args:
            base_url: Base URL for short URLs (e.g., "http://short.url/")
        """
        pass

    def encode(self, longUrl: str) -> str:
        """
        Encode long URL to short URL.

        TODO: Implement encoding
        Hints:
        1. Check if long URL already encoded (return existing short URL)
        2. Generate unique short code
        3. Store bidirectional mapping
        4. Return short URL

        Counter-Based Approach:
        if longUrl in self.long_to_short:
            return self.long_to_short[longUrl]

        # Convert counter to base62
        code = self._encode_base62(self.counter)
        self.counter += 1

        short_url = self.base_url + code
        self.long_to_short[longUrl] = short_url
        self.short_to_long[code] = longUrl

        return short_url

        Hash-Based Approach:
        if longUrl in self.long_to_short:
            return self.long_to_short[longUrl]

        # Hash the URL and take first 6 characters
        hash_value = hashlib.md5(longUrl.encode()).hexdigest()[:6]

        # Handle collisions by appending counter
        code = hash_value
        counter = 0
        while code in self.short_to_long:
            code = hash_value + str(counter)
            counter += 1

        short_url = self.base_url + code
        self.long_to_short[longUrl] = short_url
        self.short_to_long[code] = longUrl

        return short_url

        Args:
            longUrl: Long URL to encode

        Returns:
            Short URL
        """
        pass

    def decode(self, shortUrl: str) -> Optional[str]:
        """
        Decode short URL to long URL.

        TODO: Implement decoding
        Hints:
        1. Extract short code from short URL
        2. Lookup in short_to_long mapping
        3. Return long URL or None if not found

        Implementation:
        # Extract code from short URL
        code = shortUrl.replace(self.base_url, "")

        # Lookup and return
        return self.short_to_long.get(code, None)

        Args:
            shortUrl: Short URL to decode

        Returns:
            Long URL, or None if not found
        """
        pass

    def _encode_base62(self, num: int) -> str:
        """
        Helper: Convert number to base62 string.

        TODO: Implement base62 encoding (optional helper)
        Hints:
        1. Use charset: a-z, A-Z, 0-9 (62 characters)
        2. Repeatedly divide by 62 and take remainder
        3. Build string from right to left

        Implementation:
        if num == 0:
            return self.charset[0]

        result = []
        while num > 0:
            result.append(self.charset[num % 62])
            num //= 62

        return ''.join(reversed(result))

        Args:
            num: Number to encode

        Returns:
            Base62 encoded string
        """
        pass
