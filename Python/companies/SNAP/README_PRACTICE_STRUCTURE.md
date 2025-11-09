# SNAP (Snapchat) Backend Engineer Interview Prep

Comprehensive preparation materials for SNAP Inc. (Snapchat) backend engineering interviews.

## 📊 About SNAP

SNAP Inc. (founded 2011, ~5,000 employees, $100B+ market cap) is a camera company behind Snapchat, a multimedia messaging app used by 400M+ daily active users. SNAP focuses on ephemeral content, AR filters, Stories, Spotlight, and innovative communication features.

## 📁 Structure

This folder contains **practice problems** and **comprehensive documentation** for SNAP interviews.

### Practice Files (Separated for Easy Reset)

Each problem has **TWO files**:

1. **`XX_problem_name.py`** - Scaffolding file with tests (DON'T EDIT)
2. **`XX_problem_name_solution.py`** - Your implementation (EDIT THIS)

## 🎯 How to Practice

### First Time
```bash
# 1. Read the problem in the scaffolding file or PDF
# 2. Implement your solution in the _solution.py file
# 3. Run tests
python 01_shortest_path_maze.py
```

### To Practice Again
```bash
# Simply reset the solution file (keep scaffolding)
rm 01_shortest_path_maze_solution.py
# Or manually clear your code and start fresh
```

## 📝 Problems List

### Core Algorithm Problems (Problems 1-7)

Based on actual SNAP interview questions from multiple sources:

1. **Shortest Path in Maze** - BFS/Dijkstra for grid pathfinding with wall breaking
2. **Ephemeral Message Queue** - Time-based TTL queue for disappearing messages (Snapchat core feature)
3. **Copy List with Random Pointers** - Deep copy of linked list (frequently asked)
4. **Rainwater Trapping** - Classic array problem with two-pointer technique
5. **LRU Cache** - Design O(1) cache with doubly linked list + hash map
6. **Serialize/Deserialize Binary Tree** - Tree encoding for data persistence
7. **Video Stream Scheduling** - Priority queue for Stories/Spotlight video chunks

### New Problems from 一亩三分地 (Problems 8-10)

Recent actual interview questions (2025):

8. **Find the Spy** - Graph problem to find person accused by majority (O(n) solution)
9. **Nested Transaction KV Store** - Stack-based transactional key-value store with commit/abort
10. **TV Remote Keyboard Navigation** - BFS shortest path for typing on grid keyboard

## 📖 Complete Documentation

See `snap_interview_questions.pdf` for:
- Complete problem descriptions
- Full solutions with explanations
- Time/space complexity analysis
- Test cases and edge cases
- Interview tips and strategies

## 🔧 Tech Stack Focus

SNAP uses:
- **Backend**: Python, C++, Java, Go (microservices architecture)
- **Infrastructure**: AWS & GCP (Kubernetes, EKS)
- **Storage**: Cassandra, Redis, DynamoDB, S3
- **Real-time**: WebSockets, Firebase Cloud Messaging, Envoy service mesh
- **CDN**: Akamai, Cloudflare
- **Data**: BigQuery, Dataflow, Apache Beam
- **ML/AR**: TensorFlow, PyTorch, Lens Studio
- **Frontend**: React Native, Swift, Kotlin

## 💡 Interview Process

Based on actual candidate experiences:

1. **Recruiter Screen** - Background, interest in camera/AR/social (30 min)
2. **Technical Phone Screen** - 1-2 LeetCode medium problems, expects runnable code (45-60 min)
3. **Onsite/Virtual Rounds** (4-6 hours):
   - **Coding Rounds (2-4)** - LeetCode medium/hard, focus on speed and correctness
   - **System Design (1-2)** - Design Snapchat features or scalable infrastructure
   - **Behavioral** - Integrated throughout, values: "Kind, Smart, Creative"

## 🎓 Preparation Tips

### Master These Topics:
- **Graphs**: BFS/DFS, shortest path algorithms (Dijkstra, A*), grid traversal
- **Trees**: Serialization, traversal, BST operations
- **Hash Maps**: Design problems, caching, frequency counting
- **Heaps/Priority Queues**: Top K, real-time ranking, scheduling
- **Sliding Window**: Stream processing, time-based problems
- **Dynamic Programming**: Medium/hard DP (coin change, knapsack variations)
- **System Design**: Distributed systems, CDN, caching, real-time messaging

### SNAP-Specific Knowledge:
- **Ephemeral Content**: Temporary data, auto-deletion, TTL systems
- **Real-time Systems**: WebSockets, push notifications, low-latency design
- **AR/Camera**: Face tracking, filters, computer vision basics
- **Stories/Spotlight**: Timeline algorithms, content ranking, recommendation
- **Scalability**: Handling 400M+ DAU, microservices, load balancing
- **Privacy & Security**: E2E encryption, data retention, compliance

### Technical Discussion Topics:
- Designing ephemeral messaging systems (auto-delete after viewing)
- Building real-time video streaming at scale
- AR filter architecture and face detection
- CDN routing and content delivery optimization
- Microservices migration strategies
- Handling spikes during major events

### Practice Strategy:
1. Solve all problems without looking at solutions
2. Focus on shortest path problems - very common at SNAP
3. Practice implementing clean, runnable code (no pseudocode!)
4. Study Snapchat's product features and engineering blog
5. Understand distributed systems and real-time architectures

## 📚 Additional Resources

- **LeetCode**: Focus on graphs, arrays, trees (medium/hard)
  - Company tag: SNAP/Snapchat (requires Premium)
  - Common problems: Number of Islands, Serialize Binary Tree, LRU Cache, Rainwater Trapping
- **System Design**:
  - "Designing Data-Intensive Applications" by Martin Kleppmann
  - Grokking the System Design Interview
  - Focus on: Real-time systems, CDN, caching
- **SNAP Engineering Blog**: Study their architecture and tech stack
- **一亩三分地 (1Point3Acres)**: Chinese forum with recent interview experiences
- **AR/Camera**: Learn basics of computer vision, face detection, WebGL

## ✅ Testing Your Solutions

All problems include comprehensive test suites:
```bash
# Run individual problem
python 01_shortest_path_maze.py

# Check all problems
for file in 0*_*.py; do
    [ "$file" != *"_solution.py" ] && python "$file"
done
```

## 🎯 Interview Focus Areas

### For SNAP Specifically:
1. **Speed**: SNAP values fast problem-solving - practice timed coding
2. **Clean Code**: Must be runnable, production-quality code
3. **Product Knowledge**: Understand Snapchat features and use cases
4. **Real-time Systems**: Deep understanding of low-latency architectures
5. **Creativity**: Show innovative thinking (aligns with "Creative" value)

### Common Interview Questions:

**Coding (from recent 一亩三分地 threads, 2025)**:
- "Find the spy in organization" (graph, in/out degree)
- "Implement nested transaction KV store" (stack + hash map)
- "TV remote keyboard navigation" (BFS shortest path)
- "Tree game - gold collection by two players" (DFS + DP on trees)
- "Co-purchases product recommendations" (hash table + sorting)
- "Max rectangle area from points" (geometry + hash)
- "Topological sort / Course Schedule" (graph theory)
- "Shortest path with wall-breaking" (BFS/Dijkstra)

**System Design (from recent interviews)**:
- "Design Snapchat Stories feature" (very common)
- "Design ride-sharing application" (Uber-like)
- "Design metric collection and alerting system" (monitoring/observability)
- "Design system to handle 400M daily active users"
- "Design AR filter delivery system with low latency"
- "Design harmful content detection system"
- "Design Netflix streaming service"

### System Design Deep Dives:
- **Stories Architecture**: Temporary content storage, 24-hour TTL, sequential viewing
- **Real-time Messaging**: WebSocket architecture, presence detection, delivery confirmation
- **AR Filters**: Face landmark detection, 3D mask rendering, filter distribution via CDN
- **Video Streaming**: Adaptive bitrate, chunking, CDN selection, low latency
- **Recommendation Engine**: User engagement signals, content ranking, personalization

## 💬 Behavioral Preparation

SNAP values (explicitly evaluated):
- **Kind**: Collaborative, respectful, inclusive culture
- **Smart**: Problem-solving, technical excellence, learning mindset
- **Creative**: Innovation, bold ideas, thinking differently

Be ready to discuss:
- Why SNAP? Why camera/AR technology?
- Experience with real-time systems or video/image processing
- Building scalable, distributed systems
- Product thinking and user empathy
- Times you demonstrated kindness, intelligence, creativity

## 📊 Understanding SNAP Products

### Core Features to Understand:
1. **Snaps**: Ephemeral photo/video messages (auto-delete)
2. **Stories**: 24-hour temporary content timelines
3. **Spotlight**: Short-form video discovery (like TikTok)
4. **Discover**: Publisher content and news
5. **Lenses/Filters**: AR camera effects and face tracking
6. **Chat**: Real-time messaging with multimedia
7. **Snap Map**: Location sharing and geo-based features
8. **Memories**: Cloud storage for saved Snaps

### Technical Challenges:
- **Scale**: 400M+ DAU, 5.4B+ Snaps sent daily
- **Real-time**: Low-latency messaging and video
- **Ephemeral**: Auto-deletion, temporary storage, privacy
- **AR**: Real-time face detection and 3D rendering
- **CDN**: Global content delivery for media

## 🚀 Quick Start Example

```python
# 1. Open 01_shortest_path_maze_solution.py
# 2. Implement the class:

from collections import deque
import heapq

class MazeSolver:
    def shortest_path(self, grid, start, end):
        """BFS for shortest path without wall breaking."""
        if not grid or not grid[0]:
            return -1

        rows, cols = len(grid), len(grid[0])
        queue = deque([(start[0], start[1], 0)])
        visited = {start}

        while queue:
            r, c, dist = queue.popleft()

            if (r, c) == end:
                return dist

            for dr, dc in [(0,1), (1,0), (0,-1), (-1,0)]:
                nr, nc = r + dr, c + dc
                if (0 <= nr < rows and 0 <= nc < cols and
                    grid[nr][nc] == 0 and (nr, nc) not in visited):
                    visited.add((nr, nc))
                    queue.append((nr, nc, dist + 1))

        return -1

# 3. Run tests:
# python 01_shortest_path_maze.py
#
# Output:
# ✓ Test 1 passed: Basic shortest path works
# ✓ Test 2 passed: Wall blocking handled
# ...
# All tests passed! ✓
```

## 📞 Good Luck!

Remember: SNAP is looking for engineers who are **passionate about camera/AR technology**, **experienced with real-time systems**, and **creative problem-solvers**. Show your algorithmic skills, system design thinking, understanding of their product, and enthusiasm for building innovative communication tools!

---

*Note: These problems are based on actual SNAP interview questions from Glassdoor, LeetCode, 一亩三分地, Prepfully, interviewing.io, and GitHub repositories of company-specific questions. Study SNAP's engineering blog and product features to understand their technical challenges.*
