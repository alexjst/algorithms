/**
 * Problem 4: Read-Write Lock for Index Access
 *
 * Implement index access control with ReentrantReadWriteLock.
 * Multiple readers (search queries) can access simultaneously.
 * Single writer (index refresh) has exclusive access.
 *
 * Requirements:
 * - search(query): Read operation (multiple concurrent readers allowed)
 * - refresh(): Write operation (exclusive access)
 * - Use ReentrantReadWriteLock with fair policy
 *
 * Use: ReentrantReadWriteLock, read/write lock methods
 */

import java.util.concurrent.locks.*;

class ReadWriteLockIndex {
    public static void main(String[] args) throws Exception {
        System.out.println("Testing Read-Write Lock Index...\n");

        SearchIndex index = new SearchIndex();

        // Test 1: Concurrent reads
        System.out.println("Test 1: Concurrent reads");
        Thread r1 = new Thread(() -> index.search("query1"));
        Thread r2 = new Thread(() -> index.search("query2"));
        r1.start(); r2.start();
        r1.join(); r2.join();
        System.out.println("✓ Test 1 passed\n");

        // Test 2: Write blocks reads
        System.out.println("Test 2: Write exclusivity");
        index.refresh();
        System.out.println("✓ Test 2 passed\n");

        System.out.println("All tests passed! ✓");
    }
}

class SearchIndex {
    private final ReentrantReadWriteLock rwLock = new ReentrantReadWriteLock(true); // fair

    public void search(String query) {
        // TODO: Acquire read lock, perform search, release
        throw new UnsupportedOperationException("Not implemented");
    }

    public void refresh() {
        // TODO: Acquire write lock, refresh index, release
        throw new UnsupportedOperationException("Not implemented");
    }
}
