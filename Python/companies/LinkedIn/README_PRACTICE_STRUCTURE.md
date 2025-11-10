# LinkedIn Software Engineer Interview Prep

Comprehensive preparation materials for LinkedIn software engineering interviews, based on confirmed interview patterns from Glassdoor, 一亩三分地, and LeetCode discussions.

## ⚠️ IMPORTANT: LinkedIn ↔️ DataHub Crossover

**DataHub was created by LinkedIn's data team.** There's significant overlap in Java concurrency problems between the two companies.

**📖 See [LINKEDIN_DATAHUB_CROSSOVER.md](../LINKEDIN_DATAHUB_CROSSOVER.md) for complete crossover analysis.**

**Quick Summary:**
- LinkedIn has 2 Java concurrency problems (Bounded Blocking Queue, Web Crawler)
- DataHub has 3 Java concurrency problems (Thread-Safe Cache, Producer-Consumer, Batch Processor)
- **All 5 problems are interchangeable** between the companies
- Study **all 5 Java concurrency problems** for maximum interview coverage

## 📁 Structure

This folder contains **practice problems** and **comprehensive documentation** for LinkedIn interviews.

### Practice Files (Separated for Easy Reset)

Each problem has **TWO files**:

1. **`XX_problem_name.py`** or **`XX_problem_name.java`** - Scaffolding file with tests (DON'T EDIT)
2. **`XX_problem_name_solution.py`** or **`XX_problem_name_solution.java`** - Your implementation (EDIT THIS)

## 🎯 How to Practice

### Python Problems
```bash
# 1. Read the problem in the scaffolding file
# 2. Implement your solution in the _solution.py file
# 3. Run tests
python 01_nested_list_weight_sum.py
```

### Java Problems
```bash
# 1. Read the problem in the .java file
# 2. Implement your solution
# 3. Compile and run
javac 07_BoundedBlockingQueue.java
java BoundedBlockingQueue
```

### To Practice Again
```bash
# Simply reset the solution file (keep scaffolding)
rm 01_nested_list_weight_sum_solution.py
# Or manually clear your code and start fresh
```

## 📝 Problems List

### Python Algorithm Problems (LinkedIn-Tagged + High Frequency)

1. **Nested List Weight Sum** (Easy) - DFS, Recursion - **LinkedIn Signature Problem**
2. **Isomorphic Strings** (Easy) - Hash Map - **Confirmed in recent interviews**
3. **Max Stack** (Easy/Medium) - Stack Design - **LinkedIn-Tagged Premium**
4. **Accounts Merge** (Medium) - Union-Find/DFS - **Very High Frequency for LinkedIn**
5. **Edit Distance** (Medium) - Dynamic Programming
6. **Merge Intervals** (Medium) - Sorting, Arrays

### Java Concurrency Problems (Backend Focus)

7. **Bounded Blocking Queue** (Medium) - Semaphores, wait/notify - **LinkedIn Favorite**
8. **Web Crawler Multithreaded** (Medium) - Thread pools, synchronization

## 🎯 LinkedIn Interview Focus

### Confirmed Problem Patterns (2024-2025)

**From Glassdoor & 一亩三分地:**
- **Graphs**: "Undirected graphs - finding connected groups" (Accounts Merge)
- **Trees**: "Find leaves of binary tree"
- **Caching**: "Pros vs cons of different caching methods" (system design)
- **Concurrency**: Thread vs process discussion
- **Nested Structures**: Nested integer problems

**From LeetCode Discussion:**
- Typical format: **1 Medium + 1 Hard** in 40 minutes
- Focus on **clean code** and **optimization**
- Strong emphasis on **graph problems** (social network context)

### Interview Structure

1. **Recruiter Phone Screen** (20 min)
   - Behavioral questions
   - Role expectations
   - Compensation discussion

2. **Technical Phone Screen** (45 min)
   - 1-2 coding problems (Easy/Medium)
   - Focus on data structures & algorithms
   - Communication and problem-solving approach

3. **Virtual Onsite** (3-4 hours)
   - **2 Coding Rounds** (40 min each): 1 Medium + 1 Hard
   - **System Design Round** (45 min): Design LinkedIn feature or distributed system
   - **Behavioral Round** (30 min): Cultural fit, past experiences
   - **Hiring Manager Round** (30 min): Technical resume discussion

**Average Hiring Time**: 23 days (306 interviews on Glassdoor)

## 🔧 Tech Stack Focus

LinkedIn uses:
- **Backend**: Java, Scala (Play Framework), Spring Boot
- **Frontend**: React, Ember.js
- **Data**: Kafka, Espresso, Voldemort (distributed DB)
- **Infrastructure**: Kubernetes, Docker
- **Big Data**: Hadoop, Spark

## 💡 Preparation Strategy

### Master These Topics:

**Algorithms (Must-Know for LinkedIn):**
- **Graphs** ⭐⭐⭐ (Accounts Merge, Connected Components, BFS/DFS)
- **Trees** ⭐⭐⭐ (DFS, Binary Tree problems)
- **Dynamic Programming** ⭐⭐ (Edit Distance, House Robber II)
- **Hash Maps** ⭐⭐ (Isomorphic Strings, Two Sum variants)
- **Design Problems** ⭐⭐ (Max Stack, LRU Cache)
- **Intervals** ⭐ (Merge Intervals, Meeting Rooms)

**Java Concurrency (Backend Roles):**
- Producer-Consumer pattern
- Bounded Blocking Queue implementation
- Semaphores and locks
- Thread pools and ExecutorService
- synchronized, wait(), notify()

**System Design Topics:**
- Caching strategies (Redis, Memcached)
- Distributed systems (CAP theorem)
- Message queues (Kafka)
- Social graph design
- Feed ranking systems
- Microservices architecture

### Technical Discussion Topics:

Be prepared to discuss:
- **Java fundamentals**: JVM, garbage collection, memory model
- **Concurrency**: Thread safety, deadlocks, race conditions
- **Databases**: SQL vs NoSQL, indexing, transactions
- **Networking**: HTTP/HTTPS, REST APIs, WebSockets
- **LinkedIn's tech**: Kafka basics, distributed systems

### Practice Strategy:

1. **Week 1-2**: Solve all algorithm problems without looking at solutions
2. **Week 3**: Focus on graph problems (Accounts Merge variations)
3. **Week 4**: Java concurrency + system design
4. **Throughout**: Practice explaining your approach out loud (mock interviews)

## 📊 Difficulty Distribution

Based on LinkedIn interview reports:

- **Easy (30%)**: Nested List, Isomorphic Strings, basic tree problems
- **Medium (60%)**: Accounts Merge, Edit Distance, Merge Intervals, Bounded Blocking Queue
- **Hard (10%)**: Advanced DP (Paint House II), complex graph problems

**Typical Interview Combinations:**
- Phone Screen: 1 Easy + 1 Medium
- Onsite Round 1: 1 Medium (graphs/trees)
- Onsite Round 2: 1 Medium (DP/design) + 1 Hard

## 🎓 LinkedIn-Specific Tips

### Why These Problems Matter:

1. **Accounts Merge** - Tests graph algorithms (social connections)
2. **Nested List Weight Sum** - Tests recursion and data structure traversal
3. **Max Stack** - Tests design skills and optimization thinking
4. **Bounded Blocking Queue** - Tests Java concurrency knowledge (critical for backend)

### What LinkedIn Looks For:

- **Clean, readable code** - They value maintainability
- **Optimization awareness** - Discuss time/space complexity
- **Edge case handling** - Null checks, empty inputs
- **Communication** - Explain your thought process clearly
- **Collaboration** - Work with the interviewer, ask clarifying questions

### Common Mistakes to Avoid:

❌ Jumping into code without discussing approach
❌ Not asking about input constraints
❌ Ignoring edge cases
❌ Not testing your solution
❌ Poor variable naming
❌ Not discussing trade-offs

✅ Discuss multiple approaches before coding
✅ Clarify requirements and constraints
✅ Handle edge cases explicitly
✅ Walk through test cases
✅ Use descriptive names
✅ Explain time/space complexity

## 📚 Additional Resources

### LeetCode Study:
- **LinkedIn Tagged Problems** (61 problems on LeetCode Premium)
- Focus on: Graph, Tree, DFS/BFS, Design
- Practice medium problems (60% of interview questions)

### Books:
- "Cracking the Coding Interview" - Chapters 10 (Scalability), 15 (Threads)
- "Designing Data-Intensive Applications" - For system design

### LinkedIn Engineering Blog:
- Read about LinkedIn's architecture and engineering challenges
- Topics: Kafka, Venice, Espresso, Feed ranking

### Mock Interviews:
- Practice on interviewing.io or Pramp
- Focus on communication and problem-solving approach

## ✅ Testing Your Solutions

### Test Individual Problems
```bash
# Python
python 01_nested_list_weight_sum.py
python 04_accounts_merge.py

# Java
javac 07_BoundedBlockingQueue.java && java BoundedBlockingQueue
```

### Test All Problems
```bash
# Test all Python problems
for file in 0*_*.py; do
    [ "$file" != *"_solution.py" ] && echo "Testing $file" && python "$file"
done

# Test all Java problems
for file in 0*_*.java; do
    [ "$file" != *"Solution.java" ] && javac "$file" 2>/dev/null && \
    class_name=$(grep "^class.*{" "$file" | head -1 | awk '{print $2}') && \
    java "$class_name" && rm -f *.class
done
```

## 🚀 Quick Start Example

```python
# 1. Open 01_nested_list_weight_sum_solution.py
# 2. Implement the function:

def depthSum(nestedList: List[NestedInteger]) -> int:
    def dfs(nested, depth):
        total = 0
        for item in nested:
            if item.isInteger():
                total += item.getInteger() * depth
            else:
                total += dfs(item.getList(), depth + 1)
        return total

    return dfs(nestedList, 1)

# 3. Run tests:
# python 01_nested_list_weight_sum.py
#
# Output:
# ✓ Test 1 passed: [[1,1],2,[1,1]] = 10
# ✓ Test 2 passed: [1,[4,[6]]] = 27
# ...
# All tests passed! ✓
```

## 📞 Timeline & Preparation

### 4-Week Preparation Plan:

**Week 1: Foundation**
- Day 1-2: Review graph algorithms (BFS, DFS, Union-Find)
- Day 3-4: Solve Nested List, Isomorphic Strings, Max Stack
- Day 5-7: Deep dive into Accounts Merge variations

**Week 2: Medium Problems**
- Day 8-10: Edit Distance, Merge Intervals
- Day 11-12: More graph problems (LeetCode LinkedIn tag)
- Day 13-14: System design fundamentals

**Week 3: Java Concurrency**
- Day 15-17: Bounded Blocking Queue, multithreading concepts
- Day 18-19: Web Crawler, thread pool problems
- Day 20-21: System design practice (caching, distributed systems)

**Week 4: Mock Interviews**
- Day 22-24: Full mock interviews (algorithm + system design)
- Day 25-26: Review weak areas
- Day 27-28: Behavioral prep, LinkedIn culture research

## 🏆 Success Metrics

Before your interview, you should be able to:

✅ Solve Accounts Merge in 25-30 minutes with optimal solution
✅ Implement Bounded Blocking Queue from scratch without looking
✅ Explain time/space complexity for all solutions
✅ Design a basic feed ranking system
✅ Discuss LinkedIn's tech stack confidently
✅ Handle follow-up optimization questions

## 📝 Interview Day Checklist

**Before the Interview:**
- [ ] Review your resume - be ready to discuss every project
- [ ] Prepare 2-3 questions about LinkedIn's engineering culture
- [ ] Test your setup (camera, mic, IDE, internet)
- [ ] Have paper and pen ready for notes

**During the Interview:**
- [ ] Greet enthusiastically and professionally
- [ ] Repeat the problem back to confirm understanding
- [ ] Ask clarifying questions about constraints
- [ ] Discuss approach before coding
- [ ] Think out loud while coding
- [ ] Test with sample inputs
- [ ] Ask insightful questions at the end

## 🌟 Good Luck!

Remember: LinkedIn values **impact**, **collaboration**, and **technical excellence**. Show your problem-solving skills, communicate clearly, and demonstrate enthusiasm for building products that connect professionals worldwide!

**"Create economic opportunity for every member of the global workforce."** - LinkedIn's mission

---

*Last updated: November 2024*
*Based on 306+ Glassdoor interviews, 一亩三分地 reports, and LeetCode discussions*
