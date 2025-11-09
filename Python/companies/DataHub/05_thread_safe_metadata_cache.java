/**
 * Problem 5: Thread-Safe Metadata Cache
 *
 * DataHub's metadata service needs a thread-safe cache for frequently accessed metadata.
 * Implement a thread-safe LRU cache that handles concurrent reads and writes.
 *
 * Requirements:
 * - Thread-safe get() and put() operations
 * - LRU eviction policy when capacity is reached
 * - Support concurrent reads (multiple threads can read simultaneously)
 * - Writes must be exclusive (only one writer at a time)
 * - No data corruption under concurrent access
 *
 * Example:
 *     MetadataCache cache = new MetadataCache(2);
 *
 *     // Thread 1
 *     cache.put("dataset1", "metadata1");
 *
 *     // Thread 2 (concurrent)
 *     cache.put("dataset2", "metadata2");
 *
 *     // Thread 3 (concurrent read)
 *     String m = cache.get("dataset1");
 *
 * Time Complexity: O(1) for both get and put
 * Space Complexity: O(capacity)
 */

import java.util.*;
import java.util.concurrent.*;
import java.util.concurrent.locks.*;

class ThreadSafeMetadataCache {

    /**
     * Thread-safe LRU cache for metadata.
     *
     * TODO: Implement this class in ThreadSafeMetadataCacheSolution.java
     */
    static class MetadataCache {
        // TODO: Add necessary fields
        // Hints:
        // - Use LinkedHashMap for LRU ordering
        // - Use ReadWriteLock for concurrent read, exclusive write
        // - Consider ReentrantReadWriteLock

        public MetadataCache(int capacity) {
            // TODO: Implement
            throw new UnsupportedOperationException("Not implemented");
        }

        public String get(String key) {
            // TODO: Implement thread-safe get with read lock
            throw new UnsupportedOperationException("Not implemented");
        }

        public void put(String key, String value) {
            // TODO: Implement thread-safe put with write lock
            throw new UnsupportedOperationException("Not implemented");
        }

        public int size() {
            // TODO: Implement thread-safe size
            throw new UnsupportedOperationException("Not implemented");
        }
    }

    // Test cases
    public static void main(String[] args) throws InterruptedException {
        System.out.println("Testing Thread-Safe Metadata Cache...\n");

        // Test 1: Basic put and get
        System.out.println("Test 1: Basic put and get");
        MetadataCache cache1 = new MetadataCache(3);
        cache1.put("dataset1", "metadata1");
        cache1.put("dataset2", "metadata2");
        String result1 = cache1.get("dataset1");
        assert result1.equals("metadata1") : "Test 1 failed: expected 'metadata1', got '" + result1 + "'";
        System.out.println("✓ Test 1 passed: Basic operations work\n");

        // Test 2: LRU eviction
        System.out.println("Test 2: LRU eviction");
        MetadataCache cache2 = new MetadataCache(2);
        cache2.put("dataset1", "metadata1");
        cache2.put("dataset2", "metadata2");
        cache2.put("dataset3", "metadata3");  // Should evict dataset1
        String result2a = cache2.get("dataset1");
        String result2b = cache2.get("dataset2");
        assert result2a == null : "Test 2a failed: dataset1 should be evicted";
        assert result2b != null : "Test 2b failed: dataset2 should still exist";
        System.out.println("✓ Test 2 passed: LRU eviction works\n");

        // Test 3: Concurrent reads
        System.out.println("Test 3: Concurrent reads");
        MetadataCache cache3 = new MetadataCache(10);
        cache3.put("shared", "value");

        CountDownLatch latch3 = new CountDownLatch(5);
        List<String> results3 = new CopyOnWriteArrayList<>();

        for (int i = 0; i < 5; i++) {
            new Thread(() -> {
                results3.add(cache3.get("shared"));
                latch3.countDown();
            }).start();
        }

        latch3.await();
        assert results3.size() == 5 : "Test 3a failed: expected 5 results, got " + results3.size();
        for (String r : results3) {
            assert r.equals("value") : "Test 3b failed: expected 'value', got '" + r + "'";
        }
        System.out.println("✓ Test 3 passed: Concurrent reads work\n");

        // Test 4: Concurrent writes
        System.out.println("Test 4: Concurrent writes");
        MetadataCache cache4 = new MetadataCache(100);
        CountDownLatch latch4 = new CountDownLatch(10);

        for (int i = 0; i < 10; i++) {
            final int num = i;
            new Thread(() -> {
                cache4.put("key" + num, "value" + num);
                latch4.countDown();
            }).start();
        }

        latch4.await();
        Thread.sleep(100);  // Give time for all operations to complete
        assert cache4.size() == 10 : "Test 4 failed: expected size 10, got " + cache4.size();
        System.out.println("✓ Test 4 passed: Concurrent writes work\n");

        // Test 5: Mixed concurrent reads and writes
        System.out.println("Test 5: Mixed concurrent operations");
        MetadataCache cache5 = new MetadataCache(50);
        CountDownLatch latch5 = new CountDownLatch(20);

        // 10 writers
        for (int i = 0; i < 10; i++) {
            final int num = i;
            new Thread(() -> {
                cache5.put("dataset" + num, "metadata" + num);
                latch5.countDown();
            }).start();
        }

        // 10 readers
        for (int i = 0; i < 10; i++) {
            final int num = i;
            new Thread(() -> {
                cache5.get("dataset" + num);  // May return null if write hasn't happened
                latch5.countDown();
            }).start();
        }

        latch5.await();
        Thread.sleep(100);
        assert cache5.size() <= 50 : "Test 5 failed: cache size should not exceed capacity";
        System.out.println("✓ Test 5 passed: Mixed concurrent operations work\n");

        System.out.println("All tests passed! ✓");
    }
}
