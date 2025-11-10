/**
 * Problem 1: Thread-Safe Search Cache
 *
 * Implement a thread-safe LRU cache for Elasticsearch search results with TTL (time-to-live).
 *
 * Requirements:
 * - put(key, value, ttlMillis): Store search result with TTL
 * - get(key): Retrieve cached result, return null if expired or missing
 * - Thread-safe for concurrent reads and writes
 * - LRU eviction when cache is full
 * - Automatic expiration of entries based on TTL
 *
 * Example:
 *   SearchCache cache = new SearchCache(2); // capacity = 2
 *   cache.put("query1", "results1", 5000);  // TTL 5 seconds
 *   cache.put("query2", "results2", 5000);
 *   cache.get("query1");  // "results1"
 *   cache.put("query3", "results3", 5000);  // evicts query2 (LRU)
 *   cache.get("query2");  // null (evicted)
 *
 * Concurrency Approach:
 * - ConcurrentHashMap for O(1) access
 * - ReentrantLock for LRU ordering updates
 * - Or use synchronized methods with proper locking
 *
 * See 01_ThreadSafeSearchCacheSolution.java for implementation template.
 */

import java.util.*;
import java.util.concurrent.*;

class ThreadSafeSearchCache {

    public static void main(String[] args) throws InterruptedException {
        System.out.println("Testing Thread-Safe Search Cache...\n");

        // Test 1: Basic put and get
        System.out.println("Test 1: Basic put and get");
        SearchCache cache1 = new SearchCache(3);
        cache1.put("query1", "results1", 10000);
        assert cache1.get("query1").equals("results1") : "Test 1 failed";
        System.out.println("✓ Test 1 passed\n");

        // Test 2: LRU eviction
        System.out.println("Test 2: LRU eviction");
        SearchCache cache2 = new SearchCache(2);
        cache2.put("q1", "r1", 10000);
        cache2.put("q2", "r2", 10000);
        cache2.get("q1");  // Access q1, making q2 LRU
        cache2.put("q3", "r3", 10000);  // Should evict q2
        assert cache2.get("q1") != null : "Test 2a failed";
        assert cache2.get("q2") == null : "Test 2b failed: q2 should be evicted";
        assert cache2.get("q3") != null : "Test 2c failed";
        System.out.println("✓ Test 2 passed\n");

        // Test 3: TTL expiration
        System.out.println("Test 3: TTL expiration");
        SearchCache cache3 = new SearchCache(3);
        cache3.put("short", "value", 100);  // 100ms TTL
        assert cache3.get("short") != null : "Test 3a failed";
        Thread.sleep(200);  // Wait for expiration
        assert cache3.get("short") == null : "Test 3b failed: should be expired";
        System.out.println("✓ Test 3 passed\n");

        // Test 4: Concurrent access
        System.out.println("Test 4: Concurrent access");
        SearchCache cache4 = new SearchCache(100);
        ExecutorService executor = Executors.newFixedThreadPool(10);
        CountDownLatch latch = new CountDownLatch(100);

        for (int i = 0; i < 100; i++) {
            final int id = i;
            executor.submit(() -> {
                try {
                    cache4.put("key" + id, "value" + id, 10000);
                    String result = cache4.get("key" + id);
                    assert result != null : "Concurrent put/get failed";
                } finally {
                    latch.countDown();
                }
            });
        }

        latch.await(5, TimeUnit.SECONDS);
        executor.shutdown();
        System.out.println("✓ Test 4 passed\n");

        // Test 5: Null key/value handling
        System.out.println("Test 5: Null handling");
        SearchCache cache5 = new SearchCache(2);
        try {
            cache5.put(null, "value", 1000);
            assert false : "Should reject null key";
        } catch (IllegalArgumentException e) {
            // Expected
        }
        System.out.println("✓ Test 5 passed\n");

        System.out.println("All tests passed! ✓");
    }
}

/**
 * Implement this class in 01_ThreadSafeSearchCacheSolution.java
 */
class SearchCache {
    private final int capacity;

    public SearchCache(int capacity) {
        this.capacity = capacity;
        // TODO: Initialize data structures
    }

    public void put(String key, String value, long ttlMillis) {
        // TODO: Implement thread-safe put with TTL
        throw new UnsupportedOperationException("Not implemented");
    }

    public String get(String key) {
        // TODO: Implement thread-safe get with expiration check
        throw new UnsupportedOperationException("Not implemented");
    }
}
