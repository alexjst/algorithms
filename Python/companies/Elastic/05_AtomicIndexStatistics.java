/**
 * Problem 5: Atomic Index Statistics
 *
 * Track index statistics (document count, size) using lock-free atomic operations.
 * Multiple threads update stats concurrently without locks.
 *
 * Requirements:
 * - incrementDocCount(): Increment document count atomically
 * - addSize(bytes): Add to index size atomically
 * - getDocCount(), getSize(): Read current values
 * - Use AtomicLong for lock-free updates
 *
 * Use: AtomicLong, compareAndSet for complex updates
 */

import java.util.concurrent.atomic.*;

class AtomicIndexStatistics {
    public static void main(String[] args) throws Exception {
        System.out.println("Testing Atomic Index Statistics...\n");

        IndexStats stats = new IndexStats();

        // Test 1: Concurrent updates
        System.out.println("Test 1: Concurrent updates");
        Thread[] threads = new Thread[100];
        for (int i = 0; i < 100; i++) {
            threads[i] = new Thread(() -> {
                stats.incrementDocCount();
                stats.addSize(1024);
            });
            threads[i].start();
        }
        for (Thread t : threads) t.join();

        assert stats.getDocCount() == 100 : "Test 1a failed: count = " + stats.getDocCount();
        assert stats.getSize() == 102400 : "Test 1b failed: size = " + stats.getSize();
        System.out.println("✓ Test 1 passed\n");

        System.out.println("All tests passed! ✓");
    }
}

class IndexStats {
    // TODO: Declare AtomicLong for docCount and size

    public void incrementDocCount() {
        // TODO: Atomic increment
        throw new UnsupportedOperationException("Not implemented");
    }

    public void addSize(long bytes) {
        // TODO: Atomic addition
        throw new UnsupportedOperationException("Not implemented");
    }

    public long getDocCount() {
        // TODO: Read value
        throw new UnsupportedOperationException("Not implemented");
    }

    public long getSize() {
        // TODO: Read value
        throw new UnsupportedOperationException("Not implemented");
    }
}
