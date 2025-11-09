# Java Concurrency Problems for DataHub Interviews

## ⚠️ Important: First Round Focus

**DataHub explicitly tests multithreading and concurrency in their first round interview.** These Java problems are designed to prepare you for that specific requirement.

## Why Java for DataHub?

- **DataHub's backend is Java (Spring Boot)** - not Python
- Java has robust concurrency primitives: `synchronized`, `ReentrantLock`, `ExecutorService`, etc.
- Python's GIL limits true parallelism (only I/O-bound benefits from threading)
- **For DataHub interviews, use Java for concurrency questions**

## 🔧 Setup Requirements

### Java Installation

```bash
# Check Java version (need Java 8+, Java 11+ recommended)
java -version

# If not installed:
# macOS
brew install openjdk@11

# Ubuntu/Debian
sudo apt-get install openjdk-11-jdk

# Windows
# Download from https://adoptium.net/
```

### Verify Installation

```bash
java -version  # Should show version 8 or higher
javac -version # Should show same version
```

## 📝 Java Concurrency Problems (Problems 5-7)

These complement the Python algorithm problems (1-4):

### 5. **Thread-Safe Metadata Cache** (ReadWriteLock)
- **Focus**: Thread-safe LRU cache with concurrent reads/writes
- **Concepts**: `ReadWriteLock`, `ReentrantReadWriteLock`, `LinkedHashMap`
- **Difficulty**: Medium
- **Real-world**: DataHub caches frequently accessed metadata

### 6. **Producer-Consumer Metadata Ingestion** (BlockingQueue)
- **Focus**: Multi-producer, multi-consumer pattern
- **Concepts**: `BlockingQueue`, `ExecutorService`, poison pill pattern
- **Difficulty**: Medium-Hard
- **Real-world**: DataHub ingests metadata from 100+ sources concurrently

### 7. **Concurrent Batch Processor** (Thread Pools)
- **Focus**: Parallel batch processing with thread pools
- **Concepts**: `ExecutorService`, `Future`, `CompletionService`, timeout handling
- **Difficulty**: Medium
- **Real-world**: DataHub processes large batches of schema updates

## 🎯 How to Practice

### File Structure (Same as Python)

Each problem has **TWO files**:
1. **`XX_problem_name.java`** - Scaffolding with tests (DON'T EDIT)
2. **`XX_problem_name_solution.java`** - Your implementation (EDIT THIS)

### Workflow

```bash
# 1. Read the problem
cat 05_thread_safe_metadata_cache.java

# 2. Implement your solution
# Edit: 05_thread_safe_metadata_cache_solution.java

# 3. Compile (from DataHub directory)
javac 05_thread_safe_metadata_cache_solution.java

# 4. Copy your solution class into the test file
# (Java requires both classes in same file to run easily)
# OR use the helper script below

# 5. Run tests
java ThreadSafeMetadataCache
```

### Helper Script for Testing

Create `test_java.sh` in DataHub folder:

```bash
#!/bin/bash
# Usage: ./test_java.sh 05_thread_safe_metadata_cache

PROBLEM_NUM=$1

if [ -z "$PROBLEM_NUM" ]; then
    echo "Usage: ./test_java.sh <problem_file_base_name>"
    echo "Example: ./test_java.sh 05_thread_safe_metadata_cache"
    exit 1
fi

# Extract class name from solution file
CLASS_NAME=$(grep "^public class" ${PROBLEM_NUM}_solution.java | awk '{print $3}')
TEST_CLASS=$(grep "^public class" ${PROBLEM_NUM}.java | awk '{print $3}')

echo "Compiling ${PROBLEM_NUM}_solution.java..."
javac ${PROBLEM_NUM}_solution.java

if [ $? -eq 0 ]; then
    echo "Running tests from ${PROBLEM_NUM}.java..."
    javac ${PROBLEM_NUM}.java
    java $TEST_CLASS
else
    echo "Compilation failed!"
    exit 1
fi
```

Make it executable:
```bash
chmod +x test_java.sh
./test_java.sh 05_thread_safe_metadata_cache
```

## 📚 Key Java Concurrency Concepts

### Essential Primitives

| Concept | Use Case | Example |
|---------|----------|---------|
| `synchronized` | Basic mutual exclusion | Method-level or block-level locking |
| `ReentrantLock` | Advanced locking | Explicit lock/unlock, tryLock |
| `ReadWriteLock` | Many readers, few writers | Metadata cache reads |
| `Semaphore` | Limit concurrent access | Rate limiting |
| `CountDownLatch` | Wait for N events | Coordinate startup |
| `CyclicBarrier` | Synchronize N threads | Batch processing |
| `AtomicInteger` | Lock-free counters | Statistics tracking |

### Thread Pools

```java
// Fixed thread pool (best for known workload)
ExecutorService executor = Executors.newFixedThreadPool(4);

// Submit tasks
Future<String> future = executor.submit(() -> {
    // Your task
    return "result";
});

// Get result (blocking)
String result = future.get();

// Shutdown
executor.shutdown();
executor.awaitTermination(60, TimeUnit.SECONDS);
```

### Producer-Consumer Pattern

```java
// Bounded queue
BlockingQueue<Task> queue = new ArrayBlockingQueue<>(100);

// Producer
queue.put(task);  // Blocks if full

// Consumer
Task task = queue.take();  // Blocks if empty
```

### Common Pitfalls

1. **Forgetting to unlock**: Always use try-finally
   ```java
   lock.lock();
   try {
       // Critical section
   } finally {
       lock.unlock();  // Always unlock!
   }
   ```

2. **Deadlock**: Consistent lock ordering
   ```java
   // BAD: Thread 1 locks A then B, Thread 2 locks B then A
   // GOOD: Always lock in same order (e.g., by object ID)
   ```

3. **Race conditions**: Use atomic operations
   ```java
   // BAD: count++ (not atomic)
   // GOOD: atomicCount.incrementAndGet()
   ```

4. **Not handling InterruptedException**
   ```java
   try {
       Thread.sleep(1000);
   } catch (InterruptedException e) {
       Thread.currentThread().interrupt();  // Restore flag
       // Handle interruption
   }
   ```

## 🎓 Interview Tips for DataHub Concurrency Round

### What They're Looking For

1. **Understanding of Java concurrency primitives**
   - When to use `synchronized` vs `ReentrantLock`
   - ReadWriteLock for read-heavy workloads
   - Proper use of `volatile` keyword

2. **Thread safety awareness**
   - Identify race conditions
   - Explain happens-before relationship
   - Understand memory visibility

3. **Practical design patterns**
   - Producer-consumer
   - Thread pools for scalability
   - Graceful shutdown handling

4. **Performance considerations**
   - Lock contention
   - Thread pool sizing
   - Avoiding unnecessary synchronization

### Common Interview Questions

1. "Implement a thread-safe counter"
2. "Design a rate limiter using Java concurrency"
3. "Explain the difference between synchronized and ReentrantLock"
4. "How would you handle 1000 concurrent metadata updates?"
5. "What's the difference between wait() and sleep()?"
6. "Explain happens-before relationship in Java Memory Model"

### Practice Strategy

1. **Master the fundamentals** (Week 1)
   - synchronized, wait/notify
   - Lock interfaces
   - Atomic classes

2. **Practice patterns** (Week 2)
   - Producer-consumer
   - Thread pools
   - Barrier/latch coordination

3. **Build projects** (Week 3)
   - Thread-safe cache
   - Concurrent web scraper
   - Parallel file processor

4. **Review Java Memory Model**
   - Visibility guarantees
   - Happens-before rules
   - volatile semantics

## 📖 Additional Resources

### Books
- **"Java Concurrency in Practice"** by Brian Goetz (THE definitive guide)
- "Effective Java" Chapter on Concurrency
- "The Art of Multiprocessor Programming"

### Online Resources
- Oracle Java Concurrency Tutorial
- Baeldung Java Concurrency Series
- Java Memory Model FAQ (Jeremy Manson)

### Practice Platforms
- LeetCode (filter by "Concurrency" tag)
- HackerRank Java Concurrency challenges
- Project Euler (parallelization problems)

### DataHub-Specific
- Study DataHub's Java codebase on GitHub
- Look for `@Async`, `ExecutorService` usage
- Review their Kafka consumer implementations

## ✅ Testing Your Solutions

```bash
# Test individual problem
javac 05_thread_safe_metadata_cache.java
java ThreadSafeMetadataCache

# Test all Java problems
for file in 05_*.java 06_*.java 07_*.java; do
    if [[ ! $file =~ "_solution" ]]; then
        echo "Testing $file..."
        javac $file && java $(grep "^public class" $file | awk '{print $3}')
    fi
done
```

## 🚀 Quick Reference

### Thread-Safe Collections

```java
// Concurrent collections (no external sync needed)
ConcurrentHashMap<K,V>      // Thread-safe map
CopyOnWriteArrayList<E>     // Thread-safe list (read-heavy)
BlockingQueue<E>            // Producer-consumer
ConcurrentLinkedQueue<E>    // Non-blocking queue
```

### Lock Patterns

```java
// Exclusive lock
synchronized(object) { /* critical section */ }

// Read-write lock
ReadWriteLock rwLock = new ReentrantReadWriteLock();
rwLock.readLock().lock();    // Multiple readers OK
rwLock.writeLock().lock();   // Exclusive writer
```

### Thread Pool Sizing

```java
// CPU-bound: cores + 1
int threads = Runtime.getRuntime().availableProcessors() + 1;

// I/O-bound: cores * (1 + wait/compute ratio)
int threads = cores * 2;  // Rough estimate
```

## 📞 Good Luck!

Remember: **DataHub tests concurrency in Round 1**. Make sure you're comfortable with:
- Thread-safe data structures
- Lock mechanisms (synchronized, ReentrantLock, ReadWriteLock)
- Producer-consumer patterns
- Thread pools and ExecutorService
- Handling race conditions and deadlocks

Focus on **correctness first, then performance**. Be ready to explain your design choices and trade-offs!
