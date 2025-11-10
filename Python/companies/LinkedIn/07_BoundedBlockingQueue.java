/**
 * Problem 7: Design Bounded Blocking Queue (Medium)
 *
 * **LinkedIn's Favorite Java Multithreading Problem - VERY High Frequency**
 *
 * Implement a thread-safe bounded blocking queue that has the following methods:
 *
 * - BoundedBlockingQueue(int capacity) The constructor initializes the queue with maximum capacity.
 * - void enqueue(int element) Adds element to the front of the queue. If the queue is full, the
 *   calling thread is blocked until the queue is no longer full.
 * - int dequeue() Returns the element at the rear of the queue and removes it. If the queue is
 *   empty, the calling thread is blocked until the queue is no longer empty.
 * - int size() Returns the current size of the queue.
 *
 * IMPORTANT: You are NOT allowed to use Java's built-in BlockingQueue implementations.
 * You must implement this using basic synchronization primitives (synchronized, wait, notify).
 *
 * Example:
 *     BoundedBlockingQueue queue = new BoundedBlockingQueue(2);  // capacity = 2
 *
 *     Thread producer1 = new Thread(() -> {
 *         queue.enqueue(1);
 *         queue.enqueue(2);
 *         queue.enqueue(3);  // Blocks until space available
 *     });
 *
 *     Thread consumer1 = new Thread(() -> {
 *         System.out.println(queue.dequeue());  // 1
 *         System.out.println(queue.dequeue());  // 2
 *         System.out.println(queue.dequeue());  // 3
 *     });
 *
 *     producer1.start();
 *     consumer1.start();
 *
 * Constraints:
 * - 1 <= Number of Prdoucers <= 4
 * - 1 <= Number of Consumers <= 4
 * - 1 <= size <= 2000
 * - 0 <= element <= 1000
 * - The sum of the amount of work done by all producers is equal to the amount of work done by all consumers.
 *
 * Approach:
 * - Use a Queue (LinkedList or ArrayDeque) as the underlying data structure
 * - Use synchronized blocks for thread safety
 * - Use wait() when queue is full (for enqueue) or empty (for dequeue)
 * - Use notifyAll() to wake up waiting threads when state changes
 *
 * Key Concepts:
 * - Producer-Consumer pattern
 * - wait() and notify()/notifyAll()
 * - synchronized keyword
 * - Thread blocking and waking
 *
 * Time Complexity: O(1) for all operations
 * Space Complexity: O(capacity)
 */

import java.util.*;
import java.util.concurrent.*;
import java.util.concurrent.atomic.*;

class BoundedBlockingQueue {
    private final int capacity;

    public BoundedBlockingQueue(int capacity) {
        this.capacity = capacity;
        // TODO: Initialize your data structure (Queue)
        throw new UnsupportedOperationException("Not implemented");
    }

    public void enqueue(int element) throws InterruptedException {
        // TODO: Implement thread-safe enqueue
        // Hints:
        // 1. Use synchronized(this) to ensure thread safety
        // 2. While queue is full, call wait()
        // 3. Add element to queue
        // 4. Call notifyAll() to wake up waiting consumers
        throw new UnsupportedOperationException("Not implemented");
    }

    public int dequeue() throws InterruptedException {
        // TODO: Implement thread-safe dequeue
        // Hints:
        // 1. Use synchronized(this) to ensure thread safety
        // 2. While queue is empty, call wait()
        // 3. Remove and return element from queue
        // 4. Call notifyAll() to wake up waiting producers
        throw new UnsupportedOperationException("Not implemented");
    }

    public int size() {
        // TODO: Implement size()
        // Must be synchronized to ensure thread-safe read
        throw new UnsupportedOperationException("Not implemented");
    }
}

class BoundedBlockingQueueTest {
    public static void main(String[] args) throws Exception {
        System.out.println("Testing Bounded Blocking Queue...\n");

        // Test 1: Single producer, single consumer
        System.out.println("Test 1: Single producer, single consumer");
        BoundedBlockingQueue queue1 = new BoundedBlockingQueue(2);
        List<Integer> consumed1 = Collections.synchronizedList(new ArrayList<>());

        Thread producer1 = new Thread(() -> {
            try {
                queue1.enqueue(1);
                queue1.enqueue(2);
                queue1.enqueue(3);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        });

        Thread consumer1 = new Thread(() -> {
            try {
                consumed1.add(queue1.dequeue());
                consumed1.add(queue1.dequeue());
                consumed1.add(queue1.dequeue());
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        });

        producer1.start();
        consumer1.start();
        producer1.join();
        consumer1.join();

        assert consumed1.equals(Arrays.asList(1, 2, 3)) : "Test 1 failed";
        System.out.println("✓ Test 1 passed\n");

        // Test 2: Multiple producers and consumers
        System.out.println("Test 2: Multiple producers and consumers");
        BoundedBlockingQueue queue2 = new BoundedBlockingQueue(5);
        CountDownLatch latch = new CountDownLatch(20);  // 10 enqueues + 10 dequeues

        // 2 producers, each producing 5 items
        for (int i = 0; i < 2; i++) {
            final int producerId = i;
            new Thread(() -> {
                try {
                    for (int j = 0; j < 5; j++) {
                        queue2.enqueue(producerId * 10 + j);
                        latch.countDown();
                    }
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
            }).start();
        }

        // 2 consumers, each consuming 5 items
        for (int i = 0; i < 2; i++) {
            new Thread(() -> {
                try {
                    for (int j = 0; j < 5; j++) {
                        queue2.dequeue();
                        latch.countDown();
                    }
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
            }).start();
        }

        latch.await(5, TimeUnit.SECONDS);
        assert queue2.size() == 0 : "Test 2 failed: queue should be empty";
        System.out.println("✓ Test 2 passed\n");

        // Test 3: Test blocking behavior
        System.out.println("Test 3: Blocking behavior");
        BoundedBlockingQueue queue3 = new BoundedBlockingQueue(1);
        AtomicBoolean producerBlocked = new AtomicBoolean(false);

        queue3.enqueue(100);  // Fill the queue

        Thread blockingProducer = new Thread(() -> {
            try {
                producerBlocked.set(true);
                queue3.enqueue(200);  // This should block
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        });

        blockingProducer.start();
        Thread.sleep(100);  // Give time for producer to block
        assert producerBlocked.get() : "Test 3a failed: producer should have attempted enqueue";

        queue3.dequeue();  // Unblock producer
        blockingProducer.join(1000);
        assert queue3.size() == 1 : "Test 3b failed: queue should have 1 element";
        System.out.println("✓ Test 3 passed\n");

        System.out.println("All tests passed! ✓");
    }
}
