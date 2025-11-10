/**
 * Problem 3: Parallel Search Query Executor
 *
 * Execute search queries across multiple shards in parallel using CompletableFuture.
 * Combine results and handle timeouts/errors.
 *
 * Requirements:
 * - executeQuery(query, shardIds): Execute on all shards in parallel
 * - Return combined results
 * - Handle timeouts (5 seconds per shard)
 * - Handle individual shard failures gracefully
 *
 * Use: CompletableFuture, timeout handling, error recovery
 */

import java.util.*;
import java.util.concurrent.*;

class ParallelQueryExecutor {
    public static void main(String[] args) throws Exception {
        System.out.println("Testing Parallel Query Executor...\n");

        QueryExecutor executor = new QueryExecutor();

        // Test 1: Parallel execution
        System.out.println("Test 1: Parallel execution");
        List<String> results = executor.executeQuery("test", Arrays.asList(1, 2, 3));
        assert results.size() == 3 : "Test 1 failed";
        System.out.println("✓ Test 1 passed\n");

        System.out.println("All tests passed! ✓");
    }
}

class QueryExecutor {
    private final ExecutorService executor = Executors.newFixedThreadPool(10);

    public List<String> executeQuery(String query, List<Integer> shardIds) {
        // TODO: Execute in parallel using CompletableFuture
        // Hint: Use CompletableFuture.allOf() to wait for all
        throw new UnsupportedOperationException("Not implemented");
    }

    private String searchShard(String query, int shardId) {
        // Simulate shard search
        try { Thread.sleep(100); } catch (InterruptedException e) {}
        return "shard" + shardId + ":" + query;
    }
}
