/**
 * Problem 2: Concurrent Document Indexer
 *
 * Implement a multi-threaded document indexing system using producer-consumer pattern.
 * Multiple producer threads add documents to index, multiple indexer threads process them.
 *
 * Requirements:
 * - addDocument(doc): Add document to indexing queue (non-blocking)
 * - start(numIndexers): Start indexer threads
 * - shutdown(): Stop indexers gracefully
 * - getIndexedCount(): Return total documents indexed
 * - Handle backpressure (bounded queue)
 *
 * Use: BlockingQueue, ExecutorService, AtomicInteger
 */

import java.util.concurrent.*;
import java.util.concurrent.atomic.*;

class ConcurrentDocumentIndexer {
    public static void main(String[] args) throws Exception {
        System.out.println("Testing Concurrent Document Indexer...\n");

        // Test 1: Basic indexing
        System.out.println("Test 1: Basic indexing");
        DocumentIndexer indexer1 = new DocumentIndexer(10);
        indexer1.start(2);
        for (int i = 0; i < 5; i++) {
            indexer1.addDocument("doc" + i);
        }
        Thread.sleep(500);
        indexer1.shutdown();
        assert indexer1.getIndexedCount() == 5 : "Test 1 failed";
        System.out.println("✓ Test 1 passed\n");

        // Test 2: High concurrency
        System.out.println("Test 2: High concurrency");
        DocumentIndexer indexer2 = new DocumentIndexer(100);
        indexer2.start(5);
        ExecutorService producers = Executors.newFixedThreadPool(10);
        for (int i = 0; i < 100; i++) {
            final int id = i;
            producers.submit(() -> indexer2.addDocument("doc" + id));
        }
        producers.shutdown();
        producers.awaitTermination(2, TimeUnit.SECONDS);
        Thread.sleep(500);
        indexer2.shutdown();
        assert indexer2.getIndexedCount() == 100 : "Test 2 failed";
        System.out.println("✓ Test 2 passed\n");

        System.out.println("All tests passed! ✓");
    }
}

class DocumentIndexer {
    private final int queueCapacity;

    public DocumentIndexer(int queueCapacity) {
        this.queueCapacity = queueCapacity;
        // TODO: Initialize BlockingQueue, ExecutorService, counters
    }

    public void start(int numIndexers) {
        // TODO: Start indexer threads
        throw new UnsupportedOperationException("Not implemented");
    }

    public void addDocument(String document) {
        // TODO: Add to queue (handle InterruptedException)
        throw new UnsupportedOperationException("Not implemented");
    }

    public void shutdown() throws InterruptedException {
        // TODO: Graceful shutdown
        throw new UnsupportedOperationException("Not implemented");
    }

    public int getIndexedCount() {
        // TODO: Return count
        throw new UnsupportedOperationException("Not implemented");
    }
}
