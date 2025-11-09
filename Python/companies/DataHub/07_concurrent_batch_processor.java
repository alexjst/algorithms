/**
 * Problem 7: Concurrent Batch Processor
 *
 * DataHub needs to process large batches of metadata updates efficiently.
 * Implement a concurrent batch processor using thread pools that:
 * - Processes items in parallel using a fixed thread pool
 * - Aggregates results from all threads
 * - Handles failures gracefully
 * - Waits for all tasks to complete
 *
 * Requirements:
 * - Use ExecutorService with thread pool
 * - Process batches concurrently
 * - Collect results from all threads safely
 * - Handle exceptions without crashing
 * - Proper shutdown and cleanup
 *
 * Example:
 *     BatchProcessor processor = new BatchProcessor(4);
 *
 *     List<String> datasets = Arrays.asList("ds1", "ds2", "ds3", ..., "ds100");
 *     List<String> results = processor.processBatch(datasets);
 *
 *     processor.shutdown();
 *
 * Time Complexity: O(n/p) where n is items, p is threads (parallelization)
 * Space Complexity: O(n) for results
 */

import java.util.*;
import java.util.concurrent.*;
import java.util.concurrent.atomic.*;

class ConcurrentBatchProcessor {

    /**
     * Metadata batch processor with thread pool.
     *
     * TODO: Implement this class in ConcurrentBatchProcessorSolution.java
     */
    static class BatchProcessor {
        // TODO: Add necessary fields
        // Hints:
        // - ExecutorService for thread pool
        // - Consider using CompletionService for collecting results

        public BatchProcessor(int threadPoolSize) {
            // TODO: Implement
            throw new UnsupportedOperationException("Not implemented");
        }

        /**
         * Process a batch of dataset names and return processed results.
         * Simulates metadata enrichment by adding prefix to each dataset.
         */
        public List<String> processBatch(List<String> datasets) throws InterruptedException, ExecutionException {
            // TODO: Implement concurrent batch processing
            // Hints:
            // 1. Create a task for each dataset
            // 2. Submit all tasks to executor
            // 3. Collect results using Future.get() or CompletionService
            // 4. Handle exceptions from individual tasks
            // 5. Return aggregated results
            throw new UnsupportedOperationException("Not implemented");
        }

        /**
         * Process with timeout - fail if any task takes too long.
         */
        public List<String> processBatchWithTimeout(List<String> datasets, long timeout, TimeUnit unit)
                throws InterruptedException, ExecutionException, TimeoutException {
            // TODO: Implement with timeout
            // Hint: Use Future.get(timeout, unit)
            throw new UnsupportedOperationException("Not implemented");
        }

        /**
         * Process and count failures - continue even if some tasks fail.
         */
        public ProcessResult processBatchWithFailures(List<String> datasets) throws InterruptedException {
            // TODO: Implement with failure handling
            // Return both successful results and failure count
            throw new UnsupportedOperationException("Not implemented");
        }

        public void shutdown() throws InterruptedException {
            // TODO: Shutdown executor service gracefully
            throw new UnsupportedOperationException("Not implemented");
        }
    }

    static class ProcessResult {
        List<String> successes;
        int failures;

        public ProcessResult(List<String> successes, int failures) {
            this.successes = successes;
            this.failures = failures;
        }
    }

    // Helper method to simulate processing
    static String processDataset(String dataset) throws Exception {
        // Simulate processing time
        Thread.sleep(10);

        // Simulate occasional failures
        if (dataset.contains("fail")) {
            throw new Exception("Processing failed for " + dataset);
        }

        return "processed_" + dataset;
    }

    // Test cases
    public static void main(String[] args) throws Exception {
        System.out.println("Testing Concurrent Batch Processor...\n");

        // Test 1: Basic batch processing
        System.out.println("Test 1: Basic batch processing");
        BatchProcessor processor1 = new BatchProcessor(4);
        List<String> datasets1 = Arrays.asList("ds1", "ds2", "ds3", "ds4", "ds5");
        List<String> results1 = processor1.processBatch(datasets1);
        assert results1.size() == 5 : "Test 1 failed: expected 5 results, got " + results1.size();
        processor1.shutdown();
        System.out.println("✓ Test 1 passed: Basic batch processing works\n");

        // Test 2: Large batch with parallelization
        System.out.println("Test 2: Large batch with parallelization");
        BatchProcessor processor2 = new BatchProcessor(8);
        List<String> datasets2 = new ArrayList<>();
        for (int i = 0; i < 100; i++) {
            datasets2.add("dataset_" + i);
        }

        long start2 = System.currentTimeMillis();
        List<String> results2 = processor2.processBatch(datasets2);
        long duration2 = System.currentTimeMillis() - start2;

        assert results2.size() == 100 : "Test 2a failed: expected 100 results, got " + results2.size();
        // With 8 threads, should be faster than single-threaded (100 * 10ms = 1000ms)
        // Parallel should be ~200-300ms
        System.out.println("  Processing time: " + duration2 + "ms (parallelized)");
        assert duration2 < 800 : "Test 2b failed: should benefit from parallelization";
        processor2.shutdown();
        System.out.println("✓ Test 2 passed: Parallelization improves performance\n");

        // Test 3: Timeout handling
        System.out.println("Test 3: Timeout handling");
        BatchProcessor processor3 = new BatchProcessor(2);
        List<String> datasets3 = Arrays.asList("ds1", "ds2", "ds3");

        boolean timeoutCaught = false;
        try {
            // Very short timeout should fail
            processor3.processBatchWithTimeout(datasets3, 5, TimeUnit.MILLISECONDS);
        } catch (TimeoutException e) {
            timeoutCaught = true;
        }

        assert timeoutCaught : "Test 3 failed: should throw TimeoutException";
        processor3.shutdown();
        System.out.println("✓ Test 3 passed: Timeout handling works\n");

        // Test 4: Failure handling
        System.out.println("Test 4: Failure handling");
        BatchProcessor processor4 = new BatchProcessor(4);
        List<String> datasets4 = Arrays.asList("ds1", "fail_ds2", "ds3", "fail_ds4", "ds5");
        ProcessResult result4 = processor4.processBatchWithFailures(datasets4);

        assert result4.successes.size() == 3 : "Test 4a failed: expected 3 successes, got " + result4.successes.size();
        assert result4.failures == 2 : "Test 4b failed: expected 2 failures, got " + result4.failures;
        processor4.shutdown();
        System.out.println("✓ Test 4 passed: Failure handling works\n");

        // Test 5: Different thread pool sizes
        System.out.println("Test 5: Different thread pool sizes");
        List<String> datasets5 = new ArrayList<>();
        for (int i = 0; i < 50; i++) {
            datasets5.add("ds_" + i);
        }

        // Single thread
        BatchProcessor processor5a = new BatchProcessor(1);
        long start5a = System.currentTimeMillis();
        processor5a.processBatch(datasets5);
        long duration5a = System.currentTimeMillis() - start5a;
        processor5a.shutdown();

        // 10 threads
        BatchProcessor processor5b = new BatchProcessor(10);
        long start5b = System.currentTimeMillis();
        processor5b.processBatch(datasets5);
        long duration5b = System.currentTimeMillis() - start5b;
        processor5b.shutdown();

        System.out.println("  Single thread: " + duration5a + "ms");
        System.out.println("  10 threads: " + duration5b + "ms");
        assert duration5b < duration5a : "Test 5 failed: more threads should be faster";
        System.out.println("✓ Test 5 passed: Thread pool size affects performance\n");

        System.out.println("All tests passed! ✓");
    }
}
