# LinkedIn ↔️ DataHub Interview Problem Crossover

## 🔗 Critical Connection: DataHub is LinkedIn's Open-Source Project

**DataHub was created by LinkedIn's data team** and spun off as an open-source metadata platform. Because of this shared DNA, there's **significant overlap** in interview patterns, especially for Java concurrency problems.

## ⚠️ Key Insight

**Any Java multithreading/concurrency problem asked at LinkedIn is a potential candidate for DataHub interviews, and vice versa.**

Both companies:
- Use Java as primary backend language (Spring Boot)
- Value concurrency expertise for distributed systems
- Test the same Java primitives: `synchronized`, locks, thread pools, blocking queues
- Come from the same engineering culture

---

## 📊 Problem Overlap Matrix

### Java Concurrency Problems

| Problem | LinkedIn | DataHub | Pattern | Difficulty |
|---------|----------|---------|---------|------------|
| **Bounded Blocking Queue** | ✅ Problem 7 | ⭐ **LIKELY** | Producer-Consumer, wait/notify | Medium |
| **Web Crawler Multithreaded** | ✅ Problem 8 | ⭐ **LIKELY** | ExecutorService, ConcurrentHashMap | Medium |
| **Thread-Safe Metadata Cache** | ⭐ **LIKELY** | ✅ Problem 5 | ReadWriteLock, LRU | Medium |
| **Producer-Consumer Ingestion** | ⭐ **LIKELY** | ✅ Problem 6 | BlockingQueue, ExecutorService | Medium-Hard |
| **Concurrent Batch Processor** | ⭐ **LIKELY** | ✅ Problem 7 | Thread Pools, Future | Medium |

### Algorithm Problems (Lower Crossover)

| Problem | LinkedIn | DataHub | Crossover Likelihood |
|---------|----------|---------|---------------------|
| **Accounts Merge** | ✅ High Freq | ❌ | Low (LinkedIn-specific social graph) |
| **Nested List Weight Sum** | ✅ High Freq | ❌ | Low (LinkedIn-specific) |
| **Graph Algorithms** | ✅ | ⭐ Medium | Medium (metadata lineage uses graphs) |

---

## 🎯 Study Strategy: Cross-Training Approach

### For LinkedIn Interviews → Study DataHub's Java Problems Too

**LinkedIn candidates should practice:**
1. ✅ LinkedIn's 2 Java problems (Bounded Blocking Queue, Web Crawler)
2. ✅ **DataHub's 3 Java problems** (Thread-Safe Cache, Producer-Consumer, Batch Processor)
3. ✅ LinkedIn's 6 Python algorithm problems

**Total: 8 Java + 6 Python = 14 problems**

### For DataHub Interviews → Study LinkedIn's Java Problems Too

**DataHub candidates should practice:**
1. ✅ DataHub's 3 Java problems (existing)
2. ✅ **LinkedIn's 2 Java problems** (Bounded Blocking Queue, Web Crawler)
3. ✅ DataHub's 4 Python algorithm problems (existing)

**Total: 5 Java + 4 Python = 9 problems**

---

## 📁 Combined Practice Locations

### Java Concurrency (5 Total Problems)

**DataHub Directory** (`/companies/DataHub/`):
- `05_thread_safe_metadata_cache.java` - ReadWriteLock, LRU
- `06_producer_consumer_ingestion.java` - BlockingQueue, poison pill
- `07_concurrent_batch_processor.java` - ExecutorService, Future

**LinkedIn Directory** (`/companies/LinkedIn/`):
- `07_BoundedBlockingQueue.java` - wait/notify, synchronized
- `08_WebCrawlerMultithreaded.java` - Thread pools, ConcurrentHashMap

### Recommended Practice Order (Java Concurrency)

**Priority Order for BOTH Companies:**

1. **Bounded Blocking Queue** (LinkedIn #7) ⭐⭐⭐⭐⭐
   - Most fundamental - tests wait/notify
   - LinkedIn's favorite
   - Core producer-consumer pattern

2. **Producer-Consumer Ingestion** (DataHub #6) ⭐⭐⭐⭐
   - Builds on blocking queue concepts
   - Real BlockingQueue usage
   - Poison pill shutdown pattern

3. **Thread-Safe Metadata Cache** (DataHub #5) ⭐⭐⭐⭐
   - ReadWriteLock pattern
   - LRU eviction logic
   - Multi-reader optimization

4. **Web Crawler Multithreaded** (LinkedIn #8) ⭐⭐⭐
   - ExecutorService thread pools
   - ConcurrentHashMap
   - Task coordination

5. **Concurrent Batch Processor** (DataHub #7) ⭐⭐⭐
   - Future and CompletionService
   - Timeout handling
   - Parallel processing

---

## 🔧 Core Java Concurrency Concepts (Both Companies Test)

### Essential Knowledge

| Concept | LinkedIn | DataHub | Interview Frequency |
|---------|----------|---------|-------------------|
| `synchronized` keyword | ✅✅✅ | ✅✅✅ | Very High |
| `wait()` / `notify()` | ✅✅✅ | ✅✅ | High |
| `ReentrantLock` | ✅✅ | ✅✅✅ | High |
| `ReadWriteLock` | ✅ | ✅✅✅ | Medium-High |
| `BlockingQueue` | ✅✅✅ | ✅✅✅ | Very High |
| `ExecutorService` | ✅✅✅ | ✅✅✅ | Very High |
| `Future` / `CompletableFuture` | ✅✅ | ✅✅ | Medium |
| `ConcurrentHashMap` | ✅✅ | ✅✅ | High |
| `AtomicInteger` | ✅ | ✅✅ | Medium |
| `CountDownLatch` | ✅ | ✅✅ | Medium |
| Java Memory Model | ✅ | ✅✅ | Medium |

### Discussion Topics (Be Ready for Both)

**Common Questions:**
1. "Explain synchronized vs ReentrantLock" ← Both ask
2. "When would you use ReadWriteLock?" ← Both ask
3. "How does wait/notify work?" ← LinkedIn favorite
4. "Explain happens-before relationship" ← DataHub emphasis
5. "How do you size a thread pool?" ← Both ask
6. "What's the difference between thread and process?" ← LinkedIn asks
7. "How would you handle deadlock?" ← Both ask

---

## 💡 Interview Preparation Timeline

### 4-Week Plan for BOTH LinkedIn and DataHub

**Week 1: Concurrency Fundamentals**
- Day 1-2: Study synchronized, wait/notify, basic locks
- Day 3-4: **Bounded Blocking Queue** (LinkedIn #7)
- Day 5-6: **Producer-Consumer Ingestion** (DataHub #6)
- Day 7: Review and understand blocking vs busy-waiting

**Week 2: Advanced Concurrency**
- Day 8-9: **Thread-Safe Cache** (DataHub #5) - ReadWriteLock
- Day 10-11: **Web Crawler** (LinkedIn #8) - ExecutorService
- Day 12-13: **Batch Processor** (DataHub #7) - Futures
- Day 14: Mock interview on concurrency

**Week 3: Algorithm Problems** (LinkedIn-specific)
- Day 15-16: **Accounts Merge** - LinkedIn signature
- Day 17: **Nested List Weight Sum**
- Day 18: **Isomorphic Strings**
- Day 19: **Max Stack**
- Day 20: **Edit Distance**
- Day 21: **Merge Intervals**

**Week 4: System Design + Review**
- Day 22-23: System design (caching, distributed systems)
- Day 24: Review all Java concurrency problems
- Day 25: Review algorithm problems
- Day 26-27: Mock interviews
- Day 28: Final review, edge cases

---

## 🎓 Technical Depth by Company

### LinkedIn Emphasizes:
- **Social graph algorithms** (Accounts Merge is signature)
- **Clean code and optimization** (1 Medium + 1 Hard in 40 min)
- **Java concurrency basics** (Bounded Blocking Queue pattern)
- **System design** (feed ranking, caching strategies)

### DataHub Emphasizes:
- **Java concurrency in Round 1** (explicitly stated)
- **Deep understanding of locks** (ReadWriteLock, stampedLock)
- **Thread pools and batch processing** (metadata ingestion scale)
- **Producer-consumer patterns** (Kafka integration)

### Overlap (Study for Both):
- ✅ Java multithreading primitives
- ✅ Producer-consumer patterns
- ✅ Thread pools (ExecutorService)
- ✅ Thread-safe data structures
- ✅ Concurrency best practices

---

## 📖 Unified Resource List

### Books (Both Companies)
- **"Java Concurrency in Practice"** by Brian Goetz ← THE book for both
- "Effective Java" (Chapter on Concurrency)
- "Designing Data-Intensive Applications" (for system design)

### Online Resources
- Oracle Java Concurrency Tutorial
- Baeldung Java Concurrency Series
- LeetCode Concurrency tag (filter by Java)

### Company-Specific
- **LinkedIn**: Engineering blog (feed ranking, Kafka)
- **DataHub**: GitHub repo (study actual concurrency usage)

---

## ✅ Pre-Interview Checklist

### For EITHER Company Interview:

**Java Concurrency Mastery:**
- [ ] Can implement Bounded Blocking Queue from scratch
- [ ] Understand difference between synchronized and ReentrantLock
- [ ] Know when to use ReadWriteLock
- [ ] Can explain wait/notify mechanism
- [ ] Comfortable with ExecutorService and thread pools
- [ ] Understand ConcurrentHashMap internals
- [ ] Can handle race conditions and deadlocks

**If LinkedIn:**
- [ ] Can solve Accounts Merge in 25 minutes
- [ ] Practiced 1 Medium + 1 Hard in 40 minutes
- [ ] Reviewed social graph concepts
- [ ] Prepared system design: feed ranking, caching

**If DataHub:**
- [ ] Deep understanding of producer-consumer pattern
- [ ] Can explain Java Memory Model
- [ ] Familiar with Kafka concepts (metadata ingestion)
- [ ] Can design batch processing systems

---

## 🚀 Quick Decision Guide

**If interviewing at LinkedIn:**
→ Study **all 8 problems** (5 Java concurrency + 6 Python algorithms)
→ Focus on Accounts Merge + Bounded Blocking Queue

**If interviewing at DataHub:**
→ Study **all 5 Java concurrency problems** (prioritize concurrency over algorithms)
→ Deep dive into ReadWriteLock and producer-consumer

**If interviewing at BOTH:**
→ **Master all 5 Java concurrency problems first** (highest overlap)
→ Then LinkedIn's algorithm problems
→ Then system design

---

## 📊 Success Metrics

Before interviewing, you should be able to:

**Java Concurrency (Both Companies):**
- ✅ Implement Bounded Blocking Queue in 30 minutes
- ✅ Explain trade-offs: synchronized vs locks vs atomic
- ✅ Design thread-safe LRU cache
- ✅ Handle producer-consumer with graceful shutdown

**LinkedIn-Specific:**
- ✅ Solve Accounts Merge in 25 minutes
- ✅ Explain time/space complexity for all algorithm solutions

**DataHub-Specific:**
- ✅ Explain happens-before relationship
- ✅ Size thread pool for given workload
- ✅ Design metadata ingestion pipeline

---

## 🎯 Bottom Line

**The shared LinkedIn → DataHub engineering DNA means:**

1. **5 Java concurrency problems** (3 DataHub + 2 LinkedIn) are **interchangeable**
2. If LinkedIn asks about thread pools → you use DataHub's practice
3. If DataHub asks about blocking queues → you use LinkedIn's practice
4. **Prepare all 5 Java problems** for maximum coverage
5. The algorithm problems (Accounts Merge, etc.) are LinkedIn-specific

**Time Investment:**
- Java Concurrency: **40 hours** (critical for both)
- LinkedIn Algorithms: **20 hours** (LinkedIn-specific)
- System Design: **15 hours** (both companies)
- Mock Interviews: **10 hours**

**Total: ~85 hours for comprehensive prep**

---

*Last updated: November 2024*
*Based on confirmed interview patterns from both LinkedIn and DataHub*
