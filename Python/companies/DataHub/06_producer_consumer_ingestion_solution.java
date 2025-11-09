/**
 * Solution for Problem 6: Producer-Consumer Metadata Ingestion
 *
 * TODO: Implement the MetadataIngestionPipeline class below.
 */

import java.util.*;
import java.util.concurrent.*;
import java.util.concurrent.atomic.*;

public class ProducerConsumerIngestionSolution {

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

    static class MetadataIngestionPipeline {
        private final BlockingQueue<MetadataEvent> queue;
        private final ExecutorService executorService;
        private final AtomicInteger processedCount;
        private volatile boolean isShutdown;
        private static final MetadataEvent POISON_PILL = new MetadataEvent("POISON", "PILL");

        public MetadataIngestionPipeline(int queueSize) {
            // TODO: Implement initialization
            // Hints:
            // 1. Create ArrayBlockingQueue with given capacity
            // 2. Create ExecutorService (use Executors.newFixedThreadPool later)
            // 3. Initialize AtomicInteger for counting
            // 4. Set isShutdown to false
            throw new UnsupportedOperationException("Not implemented");
        }

        public void startConsumers(int numConsumers) {
            // TODO: Start consumer threads
            // Hints:
            // 1. Create ExecutorService with numConsumers threads
            // 2. Submit consumer tasks that:
            //    a. Poll from queue (blocking)
            //    b. Check for poison pill
            //    c. Process the event
            //    d. Increment processedCount
            // Example:
            // executorService.submit(() -> {
            //     while (true) {
            //         MetadataEvent event = queue.take();
            //         if (event == POISON_PILL) break;
            //         // Process event
            //         processedCount.incrementAndGet();
            //     }
            // });
            throw new UnsupportedOperationException("Not implemented");
        }

        public boolean addEvent(MetadataEvent event) throws InterruptedException {
            // TODO: Add event to queue
            // Hints:
            // 1. Check if shutdown
            // 2. Use queue.put(event) - blocks if queue is full
            // 3. Return true if successful
            throw new UnsupportedOperationException("Not implemented");
        }

        public void shutdown() throws InterruptedException {
            // TODO: Gracefully shutdown
            // Hints:
            // 1. Set isShutdown = true
            // 2. Add poison pills (one per consumer thread)
            // 3. Shutdown executor and wait for termination
            //    executorService.shutdown();
            //    executorService.awaitTermination(10, TimeUnit.SECONDS);
            throw new UnsupportedOperationException("Not implemented");
        }

        public int getProcessedCount() {
            // TODO: Return processed count
            throw new UnsupportedOperationException("Not implemented");
        }
    }

    // Copy test cases from the main file here for testing your solution
}
