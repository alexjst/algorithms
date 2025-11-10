import java.util.*;
import java.util.concurrent.*;
import java.util.concurrent.locks.*;

/**
 * Solution Template for Thread-Safe Search Cache
 *
 * Hints:
 * 1. Use ConcurrentHashMap to store cache entries
 * 2. Store both value and expiration timestamp
 * 3. Use LinkedHashMap for LRU ordering (with external synchronization)
 * 4. Or use ConcurrentHashMap + manual LRU tracking with locks
 *
 * Approach 1: ConcurrentHashMap + ReentrantLock for LRU
 * - ConcurrentHashMap for thread-safe storage
 * - LinkedHashMap (accessOrder=true) for LRU, protected by lock
 * - Store expiration time with each entry
 *
 * Approach 2: Synchronized LinkedHashMap
 * - LinkedHashMap with accessOrder=true
 * - Synchronize all methods
 * - Override removeEldestEntry for LRU eviction
 */

class SearchCache {
    private final int capacity;

    // TODO: Declare data structures
    // Hint: private final Map<String, CacheEntry> cache;
    // Hint: private final LinkedHashMap<String, Long> lruMap; // key -> last access time
    // Hint: private final ReentrantLock lock = new ReentrantLock();

    static class CacheEntry {
        String value;
        long expirationTime;

        CacheEntry(String value, long expirationTime) {
            this.value = value;
            this.expirationTime = expirationTime;
        }

        boolean isExpired() {
            return System.currentTimeMillis() > expirationTime;
        }
    }

    public SearchCache(int capacity) {
        this.capacity = capacity;
        // TODO: Initialize data structures
        /*
        this.cache = new ConcurrentHashMap<>();
        this.lruMap = new LinkedHashMap<String, Long>(capacity, 0.75f, true) {
            @Override
            protected boolean removeEldestEntry(Map.Entry<String, Long> eldest) {
                return size() > capacity;
            }
        };
        */
    }

    public void put(String key, String value, long ttlMillis) {
        if (key == null || value == null) {
            throw new IllegalArgumentException("Key and value cannot be null");
        }

        // TODO: Implement thread-safe put
        /*
        long expirationTime = System.currentTimeMillis() + ttlMillis;
        CacheEntry entry = new CacheEntry(value, expirationTime);

        lock.lock();
        try {
            // Check if we need to evict (LRU)
            if (lruMap.size() >= capacity && !lruMap.containsKey(key)) {
                // Remove eldest entry
                String eldest = lruMap.keySet().iterator().next();
                lruMap.remove(eldest);
                cache.remove(eldest);
            }

            cache.put(key, entry);
            lruMap.put(key, System.currentTimeMillis());
        } finally {
            lock.unlock();
        }
        */
    }

    public String get(String key) {
        if (key == null) {
            return null;
        }

        // TODO: Implement thread-safe get with expiration check
        /*
        CacheEntry entry = cache.get(key);
        if (entry == null) {
            return null;
        }

        // Check expiration
        if (entry.isExpired()) {
            lock.lock();
            try {
                cache.remove(key);
                lruMap.remove(key);
            } finally {
                lock.unlock();
            }
            return null;
        }

        // Update LRU
        lock.lock();
        try {
            lruMap.put(key, System.currentTimeMillis());
        } finally {
            lock.unlock();
        }

        return entry.value;
        */
        return null; // Remove this line after implementation
    }
}
