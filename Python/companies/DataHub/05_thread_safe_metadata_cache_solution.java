/**
 * Solution for Problem 5: Thread-Safe Metadata Cache
 *
 * TODO: Implement the MetadataCache class below.
 */

import java.util.*;
import java.util.concurrent.locks.*;

public class ThreadSafeMetadataCacheSolution {

    static class MetadataCache {
        private final int capacity;
        private final LinkedHashMap<String, String> cache;
        private final ReadWriteLock lock;
        private final Lock readLock;
        private final Lock writeLock;

        public MetadataCache(int capacity) {
            // TODO: Implement initialization
            // Hints:
            // 1. Initialize capacity
            // 2. Create LinkedHashMap with accessOrder=true for LRU
            // 3. Initialize ReadWriteLock (use ReentrantReadWriteLock)
            // 4. Get read and write locks from the ReadWriteLock
            throw new UnsupportedOperationException("Not implemented");
        }

        public String get(String key) {
            // TODO: Implement thread-safe get
            // Hints:
            // 1. Acquire read lock (readLock.lock())
            // 2. Try to get value from cache
            // 3. Release lock in finally block (readLock.unlock())
            // 4. Return the value
            throw new UnsupportedOperationException("Not implemented");
        }

        public void put(String key, String value) {
            // TODO: Implement thread-safe put with LRU eviction
            // Hints:
            // 1. Acquire write lock (writeLock.lock())
            // 2. Put the key-value in cache
            // 3. If cache size exceeds capacity, remove eldest entry
            //    (LinkedHashMap has removeEldestEntry method)
            // 4. Release lock in finally block (writeLock.unlock())
            throw new UnsupportedOperationException("Not implemented");
        }

        public int size() {
            // TODO: Implement thread-safe size
            // Hint: Use read lock
            throw new UnsupportedOperationException("Not implemented");
        }
    }

    // Copy test cases from the main file here for testing your solution
}
