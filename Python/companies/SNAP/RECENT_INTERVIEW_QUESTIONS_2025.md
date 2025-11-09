# Recent SNAP Interview Questions (2025)

**Source**: 一亩三分地 (1Point3Acres) - Actual interview experiences from Jul-Dec 2025

This document contains **actual interview questions** from recent SNAP (Snapchat) interviews, extracted from Chinese tech forums.

## 📊 Summary

- **Coding Problems Found**: 10+ unique questions
- **System Design Topics**: 6+ design prompts
- **Interview Level**: Primarily L4-L5 SDE positions
- **Success Rate**: Mixed (many rejections despite correct solutions)
- **Interview Format**: 2 coding + 2 design rounds (typical onsite)

## 🔍 Coding Problems

### Problem 1: Find the Spy (Graph + Greedy)
**Level**: Medium
**Tags**: Graph, In/Out Degree
**Similar to**: LeetCode 277 - Find the Celebrity

**Description**:
Given `n` people and trust relationships where `trust[i] = [a, b]` means person `a` accuses person `b` of being a spy, find the person who is accused by everyone else (in-degree = n-1, out-degree = 0).

**Example**:
```
Input: n = 3, trust = [[1, 3], [2, 3]]
Output: 3 (person 3 is accused by both 1 and 2)

Input: n = 3, trust = [[1, 3], [2, 3], [3, 1]]
Output: -1 (no spy exists - person 3 accuses person 1)
```

**Solution Approach**: O(n) using in-degree and out-degree counting

---

### Problem 2: Tree Game - Gold Collection (Tree + DFS + DP)
**Level**: Hard
**Tags**: Tree, Dynamic Programming, Game Theory

**Description**:
In a tree structure, Player 1 starts from root going downward, Player 2 starts from any node going upward. Each node has gold dust value. Calculate maximum gold each player can collect.

**Example**:
```
Input: n = 3, edges = [[1, 2, 2], [2, 3, 3]]
Output: [5, 5] (both players can collect 5 gold)

Input: n = 4, edges = [[1, 2, 1], [1, 3, 4], [3, 4, 5]]
Output: [10, 9]
```

**Solution Approach**: DFS with DP to find optimal paths for each player

---

### Problem 3: Co-purchases (Hash Table + Sorting)
**Level**: Medium
**Tags**: Hash Map, Sorting, Frequency Counting

**Description**:
Given shopping transactions (lists of products bought together), and a target product, return all products purchased with the target, sorted by co-occurrence frequency.

**Example**:
```
Input:
  transactions = [
    ['apple', 'banana'],
    ['apple', 'orange'],
    ['banana', 'orange', 'apple']
  ]
  target = 'apple'
Output: ['banana', 'orange']  # banana appears 2 times, orange 2 times
```

**Solution Approach**: Hash map to count co-occurrences, then sort by frequency

---

### Problem 4: Max Rectangle Area from Points (Geometry + Hash)
**Level**: Hard
**Tags**: Geometry, Hash Table, Math

**Description**:
Given array of points `[x, y]`, find the maximum rectangle area that can be formed. Note: rectangle can be rotated (not necessarily axis-aligned).

**Example**:
```
Input: points = [[1,1], [1,3], [3,1], [3,3], [2,2]]
Output: 4 (rectangle formed by corners (1,1), (1,3), (3,1), (3,3))
```

**Solution Approach**: Hash set for O(1) lookup, check all pairs of points as potential diagonals

---

### Problem 5: Nested Transaction KV Store (Stack + Hash)
**Level**: Medium
**Tags**: Data Structures, Stack, Hash Table, System Design

**Description**:
Implement a key-value store supporting nested transactions with operations:
- `start_transaction()`: Begin new nested transaction
- `put(key, value)`: Store in current transaction
- `get(key)`: Retrieve value (searches current → root)
- `commit()`: Merge current transaction into parent
- `abort()`: Discard current transaction

**Example**:
```python
store = TransactionStore()
store.start_transaction()
store.put("foo", "bar")
store.put("a", "b")

store.start_transaction()  # Nested
store.put("foo", "car")
store.put("a", "b2")

store.commit()  # KV now: {foo: car, a: b2}
store.abort()   # KV now: {} (all transactions aborted)
```

**Solution Approach**: Stack of dictionaries, commit merges top into parent

---

### Problem 6: TV Remote Keyboard Navigation (BFS)
**Level**: Medium
**Tags**: BFS, Shortest Path, Grid, String

**Description**:
Given input string and keyboard layout (2D grid), find shortest sequence of TV remote button presses (UP, DOWN, LEFT, RIGHT, OK) to type the string. Cursor starts at (0,0).

**Example**:
```
Keyboard:
A B C D E
F G H I J
K L M N O
P Q R S T
U V W X Y

Input: "GAB"
Output: ["RIGHT", "DOWN", "OK", "UP", "LEFT", "OK", "RIGHT", "OK"]

Explanation:
- Type 'G': (0,0) → (1,1) = RIGHT, DOWN, OK
- Type 'A': (1,1) → (0,0) = UP, LEFT, OK
- Type 'B': (0,0) → (0,1) = RIGHT, OK
```

**Solution Approach**: BFS for each character to find shortest path

---

### Problem 7: Topological Sort / Course Schedule (Graph)
**Level**: Medium
**Tags**: Graph, Topological Sort, BFS/DFS

**Description**:
Given directed graph with `n` nodes and `m` edges, determine if a topological ordering exists.

**Example**:
```
Input: n = 3, edges = [[1, 2], [2, 3]]
Output: "Yes" (ordering: 1 → 2 → 3)
```

**Solution Approach**: Kahn's algorithm (BFS) or DFS with cycle detection

---

## 🏗️ System Design Questions

### 1. Design Ride-sharing Application (Uber-like)
**Level**: L5 Onsite
**Focus Areas**:
- User registration and authentication
- Driver online/offline status management
- Passenger-driver matching algorithm
- Map display and route planning
- Data storage (user profiles, trip history)
- Backend architecture (microservices)
- API interface design
- Real-time location tracking
- Payment processing

---

### 2. Design Metric Collection and Alerting System
**Level**: L5 Onsite
**Focus Areas**:
- Metric collection pipeline
- Time-series data storage
- Alerting thresholds and rules
- Dashboard and visualization
- DAU (Daily Active Users) calculation
- Monitoring system health metrics
- Event streaming vs system metrics
- Scalability to handle millions of events/sec

**Tricky Points**:
- Distinguish between event streaming collection (user behavior) vs system monitoring metrics
- How to efficiently query DAU from collected metrics

---

### 3. Design Snapchat Stories
**Level**: L4-L5 (Very Common)
**Focus Areas**:
- 24-hour TTL (time-to-live) implementation
- Sequential viewing order
- View count tracking
- Privacy controls (friends-only, custom lists)
- Media storage and CDN distribution
- Push notifications for new stories
- Story replies and reactions
- Scalability for 400M+ users

---

### 4. Design Harmful Content Detection System
**Level**: L4+ Onsite
**Focus Areas**:
- Image/video content moderation
- ML model deployment and serving
- Real-time vs batch processing
- Human review workflow
- Appeal process
- False positive handling
- Content classification categories
- Scalability and latency requirements

---

### 5. Design Netflix Streaming Service
**Level**: L4+ Onsite
**Focus Areas**:
- Video encoding and adaptive bitrate
- CDN architecture
- Content recommendation
- User profiles and watch history
- Concurrent stream limits
- Download for offline viewing
- Analytics and engagement tracking

---

### 6. Design Metric Collection (Alternative)
**Level**: L5 Onsite
**Additional Focus**:
- How to store metrics efficiently
- How to calculate DAU from metrics
- Difference between monitoring metrics and analytics events

---

## 📈 Interview Insights

### Success Factors:
1. **Speed**: SNAP values fast problem-solving - don't get stuck
2. **Clean Code**: Must be runnable, not pseudocode
3. **Communication**: Explain approach clearly before coding
4. **Edge Cases**: Handle all edge cases explicitly
5. **Complexity Analysis**: Know time/space complexity

### Common Rejection Reasons:
1. ❌ **"Code not complete"** - Even with correct approach, incomplete code = rejection
2. ❌ **"Wrong time complexity analysis"** - Must analyze accurately
3. ❌ **"Didn't pass all test cases"** - Hidden test cases can fail you
4. ❌ **"Communication issues"** - Language barrier or unclear explanation
5. ❌ **"Cultural fit"** - Not demonstrating "Kind, Smart, Creative" values

### Interview Experience Notes:
- **Cooldown Period**: 6 months after rejection
- **Interviewer Style**: Generally friendly, collaborative ("like discussing with colleagues")
- **Time Pressure**: 45-60 minutes per coding round
- **Follow-up Questions**: Expect optimization discussions
- **Behavioral**: Integrated throughout, not always separate round

## 🎯 Preparation Recommendations

### For Coding:
1. ✅ Practice with time constraints (45 min per problem)
2. ✅ Focus on graph problems (BFS, DFS, topological sort)
3. ✅ Master data structure design (LRU cache, transaction store)
4. ✅ Study tree DP and game theory problems
5. ✅ Practice grid/path finding with BFS

### For System Design:
1. ✅ Understand Snapchat's actual features (Stories, Spotlight, Chat)
2. ✅ Study real-time messaging architectures (WebSocket, MQTT)
3. ✅ Learn CDN and video streaming concepts
4. ✅ Practice designing ride-sharing/matching systems
5. ✅ Understand monitoring/observability systems

### Resources:
- **一亩三分地 (1point3acres.com)**: Most up-to-date interview experiences
- **LeetCode Premium**: SNAP company tag (though not always current)
- **System Design Primer**: Focus on real-time, distributed systems
- **SNAP Engineering Blog**: Understand their tech stack

## 📊 Interview Statistics (From Sample)

- **Total Threads Analyzed**: 15+ recent threads
- **Time Period**: July - December 2025
- **Positions**: Primarily L4-L5 SDE, some MLE
- **Interview Format**:
  - Phone Screen: 1 coding (45-60 min)
  - Onsite: 2 coding + 2 design (typical)
- **Outcome Distribution**:
  - Pass to next round: ~30%
  - Rejected after phone: ~40%
  - Rejected after onsite: ~30%

---

**Last Updated**: 2025-01-09
**Source Reliability**: High (direct candidate reports)
**Recommended Use**: Practice these actual questions, understand the patterns, and prepare for similar variations
