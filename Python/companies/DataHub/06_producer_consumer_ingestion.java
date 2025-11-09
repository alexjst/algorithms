/**
 * Problem 6: Producer-Consumer Metadata Ingestion
 *
 * DataHub ingests metadata from multiple sources concurrently.
 * Implement a producer-consumer pattern where producers add metadata events
 * to a queue and consumers process them.
 *
 * Requirements:
 * - Thread-safe queue for metadata events
 * - Multiple producers can add events concurrently
 * - Multiple consumers process events concurrently
 * - Graceful shutdown (process all pending events)
 * - No events should be lost or processed twice
 *
 * Example:
 *     MetadataIngestionPipeline pipeline = new MetadataIngestionPipeline(10);
 *
 *     // Start 3 consumer threads
 *     pipeline.startConsumers(3);
 *
 *     // Producers add events
 *     pipeline.addEvent(new MetadataEvent("dataset1", "SCHEMA_CHANGE"));
 *     pipeline.addEvent(new MetadataEvent("dataset2", "LINEAGE_UPDATE"));
 *
 *     // Shutdown and wait for completion
 *     pipeline.shutdown();
 *
 * Time Complexity: O(1) for add/poll operations
 * Space Complexity: O(queue_size)
 */

import java.util.*;
import java.util.concurrent.*;
import java.util.concurrent.atomic.*;

class ProducerConsumerIngestion {

    static class MetadataEvent {
        String datasetName;
        String eventType;
        long timestamp;

        public MetadataEvent(String datasetName, String eventType) {
            this.datasetName = datasetName;
            this.eventType = eventType;
            this.timestamp = System.currentTimeMillis();
        }

        @Override
        public String toString() {
            return eventType + ":" + datasetName;
        }
    }

    /**
     * Metadata ingestion pipeline with producer-consumer pattern.
     *
     * TODO: Implement this class in ProducerConsumerIngestionSolution.java
     */
    static class MetadataIngestionPipeline {
        // TODO: Add necessary fields
        // Hints:
        // - Use BlockingQueue<MetadataEvent> for the queue
        // - Use ExecutorService for consumer threads
        // - Use AtomicInteger to count processed events
        // - Consider using a poison pill for shutdown

        public MetadataIngestionPipeline(int queueSize) {
            // TODO: Implement
            throw new UnsupportedOperationException("Not implemented");
        }

        public void startConsumers(int numConsumers) {
            // TODO: Start consumer threads
            // Hint: Each consumer should poll from queue and process events
            throw new UnsupportedOperationException("Not implemented");
        }

        public boolean addEvent(MetadataEvent event) throws InterruptedException {
            // TODO: Add event to queue (blocking if full)
            throw new UnsupportedOperationException("Not implemented");
        }

        public void shutdown() throws InterruptedException {
            // TODO: Gracefully shutdown
            // Hints:
            // 1. Stop accepting new events
            // 2. Add poison pills to signal consumers to stop
            // 3. Wait for all consumers to finish
            // 4. Shutdown executor service
            throw new UnsupportedOperationException("Not implemented");
        }

        public int getProcessedCount() {
            // TODO: Return number of events processed
            throw new UnsupportedOperationException("Not implemented");
        }
    }

    // Test cases
    public static void main(String[] args) throws InterruptedException {
        System.out.println("Testing Producer-Consumer Metadata Ingestion...\n");

        // Test 1: Single producer, single consumer
        System.out.println("Test 1: Single producer, single consumer");
        MetadataIngestionPipeline pipeline1 = new MetadataIngestionPipeline(10);
        pipeline1.startConsumers(1);

        for (int i = 0; i < 5; i++) {
            pipeline1.addEvent(new MetadataEvent("dataset" + i, "SCHEMA_CHANGE"));
        }

        pipeline1.shutdown();
        int processed1 = pipeline1.getProcessedCount();
        assert processed1 == 5 : "Test 1 failed: expected 5 processed, got " + processed1;
        System.out.println("✓ Test 1 passed: Single producer/consumer works\n");

        // Test 2: Multiple producers, single consumer
        System.out.println("Test 2: Multiple producers, single consumer");
        MetadataIngestionPipeline pipeline2 = new MetadataIngestionPipeline(20);
        pipeline2.startConsumers(1);

        CountDownLatch latch2 = new CountDownLatch(3);
        for (int p = 0; p < 3; p++) {
            final int producerId = p;
            new Thread(() -> {
                try {
                    for (int i = 0; i < 5; i++) {
                        pipeline2.addEvent(new MetadataEvent("p" + producerId + "_dataset" + i, "UPDATE"));
                    }
                } catch (InterruptedException e) {
                    Thread.currentThread().interrupt();
                }
                latch2.countDown();
            }).start();
        }

        latch2.await();
        pipeline2.shutdown();
        int processed2 = pipeline2.getProcessedCount();
        assert processed2 == 15 : "Test 2 failed: expected 15 processed, got " + processed2;
        System.out.println("✓ Test 2 passed: Multiple producers work\n");

        // Test 3: Single producer, multiple consumers
        System.out.println("Test 3: Single producer, multiple consumers");
        MetadataIngestionPipeline pipeline3 = new MetadataIngestionPipeline(30);
        pipeline3.startConsumers(3);

        for (int i = 0; i < 20; i++) {
            pipeline3.addEvent(new MetadataEvent("dataset" + i, "LINEAGE"));
        }

        pipeline3.shutdown();
        int processed3 = pipeline3.getProcessedCount();
        assert processed3 == 20 : "Test 3 failed: expected 20 processed, got " + processed3;
        System.out.println("✓ Test 3 passed: Multiple consumers work\n");

        // Test 4: Multiple producers, multiple consumers
        System.out.println("Test 4: Multiple producers, multiple consumers");
        MetadataIngestionPipeline pipeline4 = new MetadataIngestionPipeline(50);
        pipeline4.startConsumers(5);

        CountDownLatch latch4 = new CountDownLatch(10);
        for (int p = 0; p < 10; p++) {
            final int producerId = p;
            new Thread(() -> {
                try {
                    for (int i = 0; i < 10; i++) {
                        pipeline4.addEvent(new MetadataEvent("p" + producerId + "_ds" + i, "EVENT"));
                    }
                } catch (InterruptedException e) {
                    Thread.currentThread().interrupt();
                }
                latch4.countDown();
            }).start();
        }

        latch4.await();
        pipeline4.shutdown();
        int processed4 = pipeline4.getProcessedCount();
        assert processed4 == 100 : "Test 4 failed: expected 100 processed, got " + processed4;
        System.out.println("✓ Test 4 passed: Multiple producers and consumers work\n");

        // Test 5: Bounded queue (backpressure)
        System.out.println("Test 5: Bounded queue with backpressure");
        MetadataIngestionPipeline pipeline5 = new MetadataIngestionPipeline(5);
        pipeline5.startConsumers(1);

        Thread.sleep(100);  // Let consumer start

        // Add more events than queue capacity (should block/wait)
        new Thread(() -> {
            try {
                for (int i = 0; i < 15; i++) {
                    pipeline5.addEvent(new MetadataEvent("dataset" + i, "EVENT"));
                }
            } catch (InterruptedException e) {
                Thread.currentThread().interrupt();
            }
        }).start();

        Thread.sleep(500);  // Let some events process
        pipeline5.shutdown();
        int processed5 = pipeline5.getProcessedCount();
        assert processed5 == 15 : "Test 5 failed: expected 15 processed, got " + processed5;
        System.out.println("✓ Test 5 passed: Bounded queue works with backpressure\n");

        System.out.println("All tests passed! ✓");
    }
}
