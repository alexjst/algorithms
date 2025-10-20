# System Design Learning Resources

A curated guide to supplement your system design curriculum with high-quality video content and interactive practice.

## 🎯 Overview

This guide maps **ByteByteGo** and **Hello Interview** resources to your 28-day system design curriculum. Use these resources to:
- Watch visual explanations before reading detailed content
- Practice real interview problems with expert guidance
- Reinforce concepts with multiple perspectives

---

## 📺 Primary Resources

### ByteByteGo (Alex Xu)
- **YouTube**: [ByteByteGo Channel](https://www.youtube.com/@ByteByteGo)
- **Website**: [bytebytego.com](https://bytebytego.com)
- **Newsletter**: [ByteByteGo Newsletter](https://blog.bytebytego.com)
- **Best For**: Visual learners, concept understanding, system architecture diagrams
- **Format**: Short videos (5-15 min), visual diagrams, newsletter deep-dives

### Hello Interview
- **Website**: [hellointerview.com](https://www.hellointerview.com)
- **Practice**: [System Design Practice](https://www.hellointerview.com/practice/overview)
- **Problem Breakdowns**: [System Design Problems](https://www.hellointerview.com/learn/system-design/problem-breakdowns/overview)
- **Best For**: FAANG interview prep, structured problem-solving, level-specific guidance
- **Format**: Interactive practice, answer keys, problem breakdowns by seniority level

---

## 📚 Topic Mapping to Your Curriculum

### Week 1: Foundations

#### Day 1: Scalability Fundamentals
**ByteByteGo Topics:**
- "What is Load Balancing?" - Understanding horizontal vs vertical scaling
- "How to Scale to Millions of Users" - Practical scaling strategies
- "Top 20 System Design Concepts" - Overview of key concepts

**Hello Interview:**
- [Core Concepts - System Design in a Hurry](https://www.hellointerview.com/learn/system-design/in-a-hurry/core-concepts)
- Focus on: Performance metrics, capacity estimation, bottleneck identification

#### Day 2: Load Balancing
**ByteByteGo Topics:**
- "Load Balancer Algorithms Explained" - Round robin, least connections, consistent hashing
- "How Netflix Scales" - Real-world load balancing at scale

**Hello Interview:**
- Pattern: Distributed Request Handling
- [The 7 Must Know Patterns](https://www.hellointerview.com/blog/patterns)

#### Day 3: Caching Strategies
**ByteByteGo Topics:**
- "Caching Strategies Explained" - Cache-aside, write-through, write-back
- "Redis Crash Course" - In-memory caching fundamentals
- "Why is Redis So Fast?" - Deep dive into Redis architecture

**Hello Interview:**
- Pattern: Caching Layer Design
- Focus on: Cache invalidation, eviction policies, cache stampede

#### Day 4: Database Fundamentals
**ByteByteGo Topics:**
- "Understanding Database Types" - SQL vs NoSQL comparison
- "Database Indexing Strategies" - B-trees, LSM trees, hash indexes
- "How to Choose the Right Database" - Decision framework

**Hello Interview:**
- [System Design in a Hurry - Data Storage](https://www.hellointerview.com/learn/system-design/in-a-hurry/introduction)
- Focus on: ACID properties, CAP theorem basics

#### Day 5: Consistency Models
**ByteByteGo Topics:**
- "Strong vs Eventual Consistency" - Tradeoffs and use cases
- "Distributed Transactions Explained" - 2PC, Saga pattern

**Hello Interview:**
- Pattern: Consistency Management
- Focus on: Read-after-write consistency, monotonic reads

#### Day 6: CAP Theorem
**ByteByteGo Topics:**
- "CAP Theorem Explained" - Visual breakdown of tradeoffs
- "Database Consistency Models" - CP vs AP systems

**Hello Interview:**
- [System Design in a Hurry - Tradeoffs](https://www.hellointerview.com/learn/system-design/in-a-hurry/core-concepts)

#### Day 7: URL Shortener Design (Integration)
**ByteByteGo Topics:**
- "Design a URL Shortener Like bit.ly" - Complete system design
- "Hash Functions for URLs" - ID generation strategies

**Hello Interview:**
- Practice Problem: Design a URL Shortener
- Focus on: Hash collisions, base62 encoding, analytics integration

---

### Week 2: Distributed Systems

#### Day 8: Message Queues & Async Communication
**ByteByteGo Topics:**
- "Message Queue Explained" - Kafka vs RabbitMQ vs SQS
- "Why is Kafka So Fast?" - Architecture deep dive
- "How to Choose a Message Queue" - Decision framework

**Hello Interview:**
- Pattern: Event-Driven Architecture
- Practice: Design a notification system

#### Day 9: API Design Best Practices
**ByteByteGo Topics:**
- "Mastering the Art of API Design" - RESTful principles
- "REST vs GraphQL" - When to use each
- "API Gateway Pattern" - Centralized routing and auth

**Hello Interview:**
- Focus on: Rate limiting, versioning, pagination, error handling

#### Day 10: Microservices Architecture
**ByteByteGo Topics:**
- "Microservices vs Monolith" - Tradeoffs and migration strategies
- "Service Mesh Explained" - Istio, Linkerd patterns
- "Kubernetes Crash Course" - Container orchestration

**Hello Interview:**
- [The 7 Must Know Patterns - Microservices](https://www.hellointerview.com/blog/patterns)
- Practice: Break down a monolith

#### Day 11: Service Discovery & Health Monitoring
**ByteByteGo Topics:**
- "Service Discovery Patterns" - Client-side vs server-side
- "Health Check Strategies" - Liveness vs readiness probes
- "Observability in Microservices" - Logging, metrics, tracing

**Hello Interview:**
- Focus on: Circuit breakers, retry logic, graceful degradation

#### Day 12: Data Partitioning Strategies
**ByteByteGo Topics:**
- "Database Sharding Explained" - Horizontal partitioning strategies
- "Consistent Hashing" - Key distribution algorithms
- "Partition Rebalancing" - Handling hotspots

**Hello Interview:**
- Pattern: Data Distribution
- Practice: Design a distributed storage system

#### Day 13: Database Replication
**ByteByteGo Topics:**
- "Master-Slave Replication" - Read replicas and failover
- "Multi-Master Replication" - Conflict resolution
- "Database Backup Strategies" - PITR, snapshots

**Hello Interview:**
- Focus on: Replication lag, split-brain scenarios, failover timing

#### Day 14: Chat System Design (Integration)
**ByteByteGo Topics:**
- "Design WhatsApp" - Real-time messaging at scale
- "WebSocket vs Long Polling" - Push notification strategies
- "Message Delivery Guarantees" - At-least-once vs exactly-once

**Hello Interview:**
- Practice Problem: Design a Chat System
- Focus on: Online presence, read receipts, message ordering

---

### Week 3: Scale & Performance

#### Day 15: Advanced Database Sharding
**ByteByteGo Topics:**
- "Database Sharding Patterns" - Range, hash, directory-based
- "Cross-Shard Queries" - Fan-out and aggregation
- "Shard Rebalancing" - Dynamic redistribution

**Hello Interview:**
- Practice: Design Instagram (photo storage and sharding)

#### Day 16: Content Delivery Networks (CDN)
**ByteByteGo Topics:**
- "CDN Explained" - Edge caching and origin servers
- "How Netflix Delivers Content" - Multi-tier CDN strategy
- "Cache Control Headers" - HTTP caching mechanisms

**Hello Interview:**
- Focus on: Cache invalidation at scale, geographic distribution

#### Day 17: Search Systems & Information Retrieval
**ByteByteGo Topics:**
- "How Search Engines Work" - Crawling, indexing, ranking
- "Elasticsearch Fundamentals" - Inverted indexes and scoring
- "Search Autocomplete System" - Trie data structures

**Hello Interview:**
- Practice Problem: Design Facebook Post Search
- Focus on: Relevance ranking, personalization, freshness

#### Day 18: Big Data Processing Systems
**ByteByteGo Topics:**
- "MapReduce Explained" - Distributed computing paradigm
- "Batch vs Stream Processing" - Hadoop vs Spark vs Flink
- "Data Pipeline Architecture" - ETL patterns

**Hello Interview:**
- Practice: Design an Ad Click Aggregator
- Focus on: Real-time analytics, lambda architecture

#### Day 19: NoSQL Database Deep Dive
**ByteByteGo Topics:**
- "DynamoDB Explained" - Key-value stores
- "MongoDB Architecture" - Document databases
- "Cassandra Design" - Wide-column stores
- "When to Use NoSQL" - Decision matrix

**Hello Interview:**
- Focus on: Data modeling, consistency levels, query patterns

#### Day 20: Social Media Feed Design (Integration)
**ByteByteGo Topics:**
- "Design Facebook Newsfeed" - Fan-out strategies
- "Design Instagram" - Photo storage and feed generation
- "Design Twitter Timeline" - Pull vs push vs hybrid

**Hello Interview:**
- Practice Problem: Design a Social Media Feed
- Focus on: Ranking algorithms, personalization, real-time updates

---

### Week 4: Production & Security

#### Day 21: Security & Authentication
**ByteByteGo Topics:**
- "Authentication Explained" - Password, Session, Cookie, Token, JWT, SSO, OAuth
- "HTTPS and TLS" - Secure communication
- "API Security Best Practices" - API keys, OAuth2, rate limiting

**Hello Interview:**
- Focus on: Zero-trust architecture, encryption at rest/in transit

#### Day 22: Monitoring & Observability
**ByteByteGo Topics:**
- "Observability in Microservices" - Three pillars (logs, metrics, traces)
- "Distributed Tracing" - Jaeger, Zipkin patterns
- "Alerting Strategies" - SLIs, SLOs, SLAs

**Hello Interview:**
- Focus on: Key metrics to monitor, alert fatigue prevention

#### Day 23: Rate Limiting & Traffic Management
**ByteByteGo Topics:**
- "Rate Limiting Algorithms" - Token bucket, leaky bucket, fixed window
- "API Gateway Patterns" - Centralized rate limiting
- "DDoS Protection" - Traffic filtering strategies

**Hello Interview:**
- Practice: Design a rate limiter
- Focus on: Distributed rate limiting, user quotas

#### Day 24: Distributed Systems Consensus
**ByteByteGo Topics:**
- "Paxos and Raft Explained" - Consensus algorithms
- "Leader Election" - Distributed coordination
- "ZooKeeper Fundamentals" - Centralized configuration

**Hello Interview:**
- Focus on: Split-brain scenarios, quorum-based systems

#### Day 25: System Integration & Architecture Patterns
**ByteByteGo Topics:**
- "Top System Design Patterns" - Comprehensive overview
- "Event Sourcing and CQRS" - Advanced patterns
- "Saga Pattern" - Distributed transactions

**Hello Interview:**
- [The 7 Must Know Patterns](https://www.hellointerview.com/blog/patterns)

#### Day 26: Mock Interview 1 - Ride Sharing System
**ByteByteGo Topics:**
- "Design Uber" - Real-time location tracking and matching
- "Geospatial Indexing" - QuadTree, Geohash, S2
- "Real-time Pricing" - Surge pricing algorithms

**Hello Interview:**
- Practice Problem: Design a Ride Sharing System
- Focus on: Matching algorithm, ETA calculation, payment processing

#### Day 27: Mock Interview 2 - Video Streaming Platform
**ByteByteGo Topics:**
- "Design YouTube" - Video storage and streaming
- "Design Netflix" - Content recommendation and CDN
- "Video Encoding and ABR" - Adaptive bitrate streaming

**Hello Interview:**
- [Practice Problem: Design YouTube](https://www.hellointerview.com/learn/system-design/problem-breakdowns/youtube)
- Focus on: Thumbnail generation, view counting, recommendation engine

#### Day 28: Mock Interview 3 - E-commerce Platform
**ByteByteGo Topics:**
- "Design Amazon" - Product catalog and inventory
- "Payment System Design" - Transaction processing
- "Digital Wallet Architecture" - Account balance management

**Hello Interview:**
- Practice Problem: Design an E-commerce Platform
- Focus on: Order processing, inventory management, fraud detection

---

## 🎓 How to Use This Guide

### Daily Study Routine

**1. Pre-Study (15-20 min)**
- Watch relevant ByteByteGo video for today's topic
- Take notes on key visual concepts and architecture patterns

**2. Main Study (30-40 min)**
- Work through your curriculum's detailed content
- Practice estimation questions and conceptual questions

**3. Reinforcement (15-20 min)**
- Read Hello Interview's problem breakdown for related topic
- Note differences in approach or additional insights

**4. Practice (Optional, 30-45 min)**
- Do Hello Interview's guided practice for the topic
- Draw system diagrams on paper/whiteboard
- Explain your design out loud

### For Reviews

When completing spaced repetition reviews:
- **1-day review**: Re-watch ByteByteGo video at 1.5x speed
- **3-day review**: Complete Hello Interview practice problem
- **7-day review**: Draw system diagram from memory, compare with notes
- **14-day review**: Do a mock interview-style walkthrough

---

## 📖 Additional ByteByteGo Topics

### Core Concepts to Master
- Load Balancing
- Rate Limiting
- API Gateway
- Microservices
- CDN (Content Delivery Network)
- Database Indexing
- Data Partitioning
- Scalability
- Fault Tolerance
- Consistency and Availability

### Common System Design Problems
- URL Shortener (like bit.ly)
- Web Crawler
- Notification System
- Payment System
- Digital Wallet
- Search Autocomplete
- Gaming Leaderboard
- Mail Server
- Hotel Reservation System
- Stock Exchange
- Ads Aggregation
- BlockingQueue

### Technology Deep Dives
- Crash Course in Kubernetes
- Crash Course in Docker
- Crash Course in Redis
- Crash Course in DNS
- Why is Kafka So Fast
- Understanding Database Types

---

## 🎯 Hello Interview Features

### Guided Practice
Interactive problem-solving with step-by-step guidance and instant feedback from FAANG interviewers.

### Problem Breakdowns
Expert analysis showing:
- What to prioritize at different seniority levels (Junior/Mid/Senior/Staff)
- Common mistakes to avoid
- How to structure your answer
- Follow-up questions and how to handle them

### The 7 Must-Know Patterns
1. **Load Balancing & Distribution** - Spread traffic across resources
2. **Caching** - Store frequently accessed data
3. **Data Partitioning** - Split data across storage systems
4. **Asynchronous Processing** - Decouple long-running operations
5. **Replication** - Duplicate data for availability
6. **Message Queues** - Buffer and route events
7. **Microservices** - Decompose into independent services

---

## 💡 Study Tips

### For ByteByteGo Content
- ✅ Pause videos to sketch diagrams yourself
- ✅ Focus on "why" not just "what" - understand tradeoffs
- ✅ Read the newsletter articles for deeper dives beyond videos
- ✅ Use the visual diagrams as templates for your own designs

### For Hello Interview
- ✅ Practice explaining your design out loud as you work
- ✅ Pay attention to level-specific expectations (what Staff engineers prioritize)
- ✅ Note the "common mistakes" sections - these are interview red flags
- ✅ Use their answer keys to calibrate your solutions

### General Best Practices
- 🎯 **Breadth before depth**: Understand many systems lightly, then go deep on key ones
- 🎯 **Practice estimates**: Get comfortable with back-of-envelope calculations
- 🎯 **Draw diagrams**: Visual communication is critical in interviews
- 🎯 **Explain tradeoffs**: Never say "X is better" without discussing context
- 🎯 **Ask questions**: Real interviews start with clarifying requirements

---

## 📊 Tracking Your Progress

Use your study tracker to log:
- Which ByteByteGo videos you've watched
- Which Hello Interview problems you've completed
- Difficulty rating for each topic
- Questions you couldn't answer (revisit these)

Add notes like:
```
Day 3 - Caching: Watched ByteByteGo Redis video. Key insight:
use write-through for data durability, cache-aside for flexibility.
Need to revisit: cache stampede prevention strategies.
```

---

## 🔗 Quick Links

### ByteByteGo
- YouTube: https://www.youtube.com/@ByteByteGo
- Newsletter: https://blog.bytebytego.com
- Course: https://bytebytego.com

### Hello Interview
- Main Site: https://www.hellointerview.com
- Problem Breakdowns: https://www.hellointerview.com/learn/system-design/problem-breakdowns/overview
- Practice: https://www.hellointerview.com/practice/overview
- System Design in a Hurry: https://www.hellointerview.com/learn/system-design/in-a-hurry/introduction

### Supplementary Resources
- System Design Primer (GitHub): https://github.com/donnemartin/system-design-primer
- ByteByteGo System Design 101: https://github.com/ByteByteGoHq/system-design-101
- High Scalability Blog: https://highscalability.com

---

## 🎯 Interview Preparation Timeline

### 4 Weeks Out
- Complete all 28 days of curriculum
- Watch all relevant ByteByteGo videos
- Read Hello Interview problem breakdowns

### 2 Weeks Out
- Focus on reviews and reinforcement
- Complete Hello Interview practice problems
- Do mock interviews with friends or mentors

### 1 Week Out
- Review your notes and diagrams
- Re-watch ByteByteGo videos at 2x speed for key topics
- Practice explaining designs out loud
- Get comfortable with estimation math

### Day Before
- Review the 7 key patterns
- Skim your notes for common tradeoffs
- Get good sleep - clarity of thought matters more than cramming

---

**Good luck with your system design interviews! 🚀**

Remember: The goal isn't to memorize solutions, but to develop a framework for approaching any system design problem with clarity, structure, and strong engineering judgment.
