# Elastic (Elasticsearch) Java Engineer Interview Prep

Focused preparation materials for Elastic Java backend engineer interviews with emphasis on **Java multithreading and concurrency**.

## 📊 About Elastic

Elastic (founded 2012, ~3,000 employees) is the company behind Elasticsearch, Kibana, Beats, and Logstash (ELK Stack). Elasticsearch is a distributed, RESTful search and analytics engine built on Apache Lucene in Java.

**Headquarters**: Mountain View, CA (distributed/remote-first)
**Stock**: NYSE: ESTC
**Tech Stack**: Java, Lucene, Netty, Distributed Systems
**Products**: Elasticsearch, Kibana, Beats, Logstash, APM, Security

## 📁 Structure

This folder contains **Java multithreading and concurrency practice problems** based on Elastic interview patterns.

### Practice Files

Problems are provided as standalone Java files. Compile and run to test:
```bash
javac 01_ThreadSafeSearchCache.java
java 01_ThreadSafeSearchCache
```

## 🎯 Interview Focus

Based on actual Elastic interviews (Glassdoor, candidate reports), technical assessment **heavily emphasizes Java concurrency**:

**Why Concurrency Matters for Elastic**:
- Elasticsearch handles thousands of concurrent search requests
- Parallel indexing of documents across shards
- Thread-safe caching (field cache, query cache, request cache)
- Concurrent index refresh and merge operations
- Distributed coordination across cluster nodes
- Multi-threaded bulk indexing API
- Parallel aggregation computation

**Interview Emphasis** (Glassdoor confirms):
- "Questions on concurrency" - direct quote from interview review
- Deep Java multithreading knowledge required
- Understanding of thread pools and async processing
- Race condition identification and fixing
- Lock-free algorithms and CAS operations

## 📝 Problems List

### Java Concurrency Problems (Problems 1-5)

Based on Elastic interview patterns and search engine requirements:

1. **Thread-Safe Search Cache** (Medium) - LRU cache with ConcurrentHashMap + ReentrantLock
   - Cache search results with TTL
   - Handle concurrent reads and writes
   - Eviction policy with thread safety

2. **Concurrent Document Indexer** (Medium-Hard) - Producer-Consumer with BlockingQueue
   - Bulk document ingestion
   - Multiple indexer threads
   - Backpressure handling

3. **Parallel Search Query Executor** (Hard) - Thread pool with CompletableFuture
   - Execute searches across multiple shards in parallel
   - Combine results from concurrent searches
   - Handle timeouts and errors

4. **Read-Write Lock for Index Access** (Medium-Hard) - ReentrantReadWriteLock
   - Multiple readers (search queries)
   - Single writer (index refresh/merge)
   - Fair lock policy

5. **Atomic Index Statistics** (Medium) - Atomic operations and volatile
   - Track document count, index size atomically
   - Lock-free updates from multiple threads
   - Memory visibility guarantees

## 💡 Interview Process

Based on Elastic candidate experiences (2023-2025):

1. **Recruiter Screen** - Background, interest in search/distributed systems (30 min)
2. **Codility Assessment** - Easy LeetCode-style problem (60-90 min)
3. **Technical Phone Screen** - Concurrency problem + algorithms (60 min)
   - Focus: "Questions on concurrency" (Glassdoor)
   - Expect: Thread safety, synchronization, concurrent collections
4. **Onsite/Virtual Rounds** (4-5 hours):
   - **Round 1**: Java concurrency deep dive (60 min)
   - **Round 2**: Algorithms + data structures (60 min)
   - **Round 3**: System design - distributed search system (60 min)
   - **Round 4**: Behavioral + technical managers (45 min)

**Interview Difficulty**: 3.0/5 (Glassdoor)
**Positive Experience**: 68%
**Average Duration**: 1-3 weeks

## 🎓 Interview Characteristics

### Key Focus Areas:

1. **Java Concurrency Expertise** - PRIMARY FOCUS
   - Deep understanding of java.util.concurrent
   - Lock contention and performance optimization
   - Debugging race conditions and deadlocks

2. **Search Engine Knowledge**
   - Understanding of inverted indices
   - Full-text search algorithms
   - Lucene architecture basics

3. **Distributed Systems**
   - Consensus algorithms (Raft used by Elasticsearch)
   - Data sharding and replication
   - CAP theorem trade-offs

4. **Performance Optimization**
   - Profiling and tuning Java applications
   - GC tuning for low-latency systems
   - Lock-free data structures

### Difficulty Assessment:
- **Concurrency**: High - expect deep, detailed questions
- **Coding**: Medium-Hard (LeetCode Medium/Hard)
- **System Design**: Distributed search systems, scalability
- **Java Knowledge**: Advanced Java required (Java 11+)

## 🔧 Tech Stack Focus

Elastic uses:
- **Core**: Java 11+, Apache Lucene
- **Concurrency**: ExecutorService, ForkJoinPool, CompletableFuture
- **Networking**: Netty (async I/O)
- **Serialization**: Custom (stream-based)
- **Coordination**: Raft consensus algorithm
- **Testing**: JUnit, Randomized Testing, Elasticsearch Test Framework

## 🎯 Preparation Tips

### Master These Java Concurrency Topics:

**Thread Fundamentals**:
- Thread lifecycle and states
- `synchronized` keyword and monitors
- `volatile` and memory visibility
- `wait()`, `notify()`, `notifyAll()`
- Thread interruption and cancellation
- Daemon threads

**Locks and Synchronizers**:
- `ReentrantLock` - explicit locking
- `ReadWriteLock` - multiple readers, single writer
- `StampedLock` - optimistic reads (Java 8+)
- `Semaphore` - resource limiting
- `CountDownLatch` - waiting for completion
- `CyclicBarrier` - coordinating threads
- `Phaser` - flexible synchronization

**Concurrent Collections**:
- `ConcurrentHashMap` - high-performance concurrent map
  - Important: Understand segment locking (Java 7) vs CAS (Java 8+)
- `CopyOnWriteArrayList` - read-heavy scenarios
- `BlockingQueue` implementations:
  - `ArrayBlockingQueue` - bounded, fairness
  - `LinkedBlockingQueue` - optionally bounded
  - `PriorityBlockingQueue` - ordered processing
- `ConcurrentSkipListMap` - sorted concurrent map
- `ConcurrentLinkedQueue` - non-blocking queue

**Thread Pools and Executors**:
- `ExecutorService` and `ThreadPoolExecutor`
- Thread pool types:
  - Fixed thread pool
  - Cached thread pool
  - Scheduled thread pool
  - Work-stealing pool (ForkJoinPool)
- Thread pool tuning:
  - Core vs maximum pool size
  - Queue types and sizing
  - Rejection policies
  - Keep-alive time
- `ForkJoinPool` for recursive parallel tasks
- Common Pitfalls:
  - Thread leaks
  - Unbounded queues causing OOM
  - Not shutting down executors

**Advanced Async Programming**:
- `CompletableFuture` for async computations
  - Chaining: `thenApply`, `thenCompose`, `thenCombine`
  - Error handling: `exceptionally`, `handle`
  - Combining: `allOf`, `anyOf`
- `Future` and `Callable`
- Timeout handling

**Atomic Operations**:
- `AtomicInteger`, `AtomicLong`, `AtomicBoolean`
- `AtomicReference` and `AtomicStampedReference`
- Compare-and-swap (CAS) operations
- Lock-free algorithms
- ABA problem and solutions

**Java Memory Model**:
- Happens-before relationship
- Memory barriers and fences
- `volatile` guarantees
- Final field semantics
- Double-checked locking (and why it needs volatile)
- False sharing and cache line padding

**Common Concurrency Issues**:
- **Deadlock**: Circular wait, prevention strategies
- **Livelock**: Threads responding to each other
- **Starvation**: Thread never gets CPU time
- **Race Conditions**: Non-atomic operations
- **Memory Visibility**: Cached values not visible
- **Thread Leaks**: Threads not properly terminated

## 📚 Additional Resources

**Books**:
- **Java Concurrency in Practice** (Brian Goetz) - ESSENTIAL
- **The Art of Multiprocessor Programming** (Herlihy & Shavit)
- **Java Performance** (Binu John)

**Online**:
- Oracle Java Concurrency Tutorial
- Baeldung Java Concurrency Articles
- DZone Java Concurrency Zone
- LeetCode Concurrency problems (1114, 1115, 1116, 1117, 1195)

**Source Code Study**:
- `java.util.concurrent` package source code
- `ConcurrentHashMap` implementation
- `ThreadPoolExecutor` internals
- Elasticsearch source code (especially thread pool management)

## 📖 Common Interview Questions

### Concurrency Fundamentals:

**Thread Safety**:
- "What is thread safety? How do you achieve it?"
- "Explain the difference between `synchronized` and `ReentrantLock`"
- "When would you use `volatile`? What guarantees does it provide?"
- "What is the happens-before relationship?"
- "Explain double-checked locking and why it needs `volatile`"

**Synchronization**:
- "What is a monitor? How does `synchronized` work?"
- "Explain wait/notify vs sleep"
- "What is spurious wakeup? How do you handle it?"
- "Difference between `notify()` and `notifyAll()`?"

### Concurrent Collections:

- "How does `ConcurrentHashMap` work internally?"
- "When would you use `CopyOnWriteArrayList`?"
- "Explain the differences between blocking and non-blocking queues"
- "How would you implement a thread-safe LRU cache?"
- "Design a bounded blocking queue from scratch"

### Thread Pools:

- "Explain the different types of thread pools"
- "How do you size a thread pool?"
- "What are the different rejection policies?"
- "Explain `ForkJoinPool` and work stealing"
- "What happens if you don't shut down an ExecutorService?"

### Advanced Topics:

- "Implement a read-write lock from scratch"
- "Explain CAS operations and lock-free programming"
- "What is the ABA problem?"
- "How does `CompletableFuture` work?"
- "Design a rate limiter using concurrency primitives"

### Elasticsearch-Specific:

- "How would you implement thread-safe caching for search results?"
- "Design a concurrent document indexer with backpressure"
- "How would you parallelize search across multiple shards?"
- "Explain how to handle concurrent index refresh operations"
- "Design a lock-free statistics counter"

### Coding Problems:

- "Fix the race condition in this code"
- "Implement producer-consumer using wait/notify"
- "Solve the dining philosophers problem"
- "Implement a thread-safe singleton"
- "Write a parallel merge sort using Fork/Join"

### System Design with Concurrency:

- "Design a distributed search engine (like Elasticsearch)"
- "Design a thread-safe connection pool"
- "Design a rate limiter for API requests"
- "Design a concurrent task scheduler"
- "Design a lock service for distributed systems"

## 💬 Behavioral Preparation

Elastic values:
- **Customer Obsession**: Building great search experiences
- **Distributed First**: Remote-friendly, async collaboration
- **Open Source**: Contributing to Elasticsearch community
- **Innovation**: Pushing boundaries of search technology

Be ready to discuss:
- Experience with concurrent/distributed systems
- Debugging performance issues in multi-threaded code
- Working on open-source projects
- Handling high-throughput, low-latency systems
- Contributing to Elasticsearch or similar projects

## ⚠️ Important Notes

### What Makes Elastic Interviews Unique:

1. **Deep Concurrency Focus**: 70%+ of technical questions are concurrency-related
2. **Practical Problems**: Tied to real search engine challenges
3. **Performance Critical**: Must understand lock contention, GC impact
4. **Distributed Context**: Concurrency in distributed systems
5. **Java Expertise**: Advanced Java knowledge required
6. **Code Quality**: Thread-safe AND maintainable code

### Red Flags (Common Rejection Reasons):

- ❌ Weak Java concurrency fundamentals
- ❌ Using `synchronized` everywhere without considering performance
- ❌ Not understanding happens-before relationships
- ❌ Inability to identify race conditions
- ❌ Poor knowledge of concurrent collections
- ❌ Not considering edge cases in multi-threaded code
- ❌ Misunderstanding of `volatile` keyword
- ❌ No experience with thread pools or async programming

### Interview Tips:

✅ **DO**:
- Think out loud about thread safety concerns
- Consider edge cases (null, empty, concurrent modification)
- Ask about expected concurrency level
- Discuss performance trade-offs (locks vs lock-free)
- Mention testing strategies for concurrent code
- Use appropriate concurrency primitives

❌ **DON'T**:
- Rush to code without considering thread safety
- Use busy-waiting instead of proper synchronization
- Forget to handle InterruptedException
- Ignore memory visibility issues
- Over-synchronize (performance killer)
- Forget to shut down thread pools

## 🚀 Quick Start Example

```java
// Example: Thread-Safe Counter

// Option 1: Using synchronized
public class SynchronizedCounter {
    private int count = 0;

    public synchronized void increment() {
        count++;
    }

    public synchronized int getCount() {
        return count;
    }
}

// Option 2: Using AtomicInteger (lock-free, better performance)
import java.util.concurrent.atomic.AtomicInteger;

public class AtomicCounter {
    private final AtomicInteger count = new AtomicInteger(0);

    public void increment() {
        count.incrementAndGet();
    }

    public int getCount() {
        return count.get();
    }
}

// Option 3: Using ReentrantLock (more flexible)
import java.util.concurrent.locks.ReentrantLock;

public class LockCounter {
    private int count = 0;
    private final ReentrantLock lock = new ReentrantLock();

    public void increment() {
        lock.lock();
        try {
            count++;
        } finally {
            lock.unlock();
        }
    }

    public int getCount() {
        lock.lock();
        try {
            return count;
        } finally {
            lock.unlock();
        }
    }
}
```

## 📞 Good Luck!

Remember: Elastic is looking for engineers who are **Java concurrency experts**, understand **distributed search systems**, and can build **high-performance, thread-safe** code. Master java.util.concurrent, practice concurrent algorithms, and be ready to discuss real-world concurrency challenges!

---

*Note: These problems are based on Java concurrency patterns commonly tested in search engine and distributed systems interviews, informed by Glassdoor reviews confirming Elastic's focus on concurrency questions.*
