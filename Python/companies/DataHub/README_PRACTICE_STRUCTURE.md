# DataHub (Acryl Data) Backend Engineer Interview Prep

Comprehensive preparation materials for DataHub/Acryl Data backend engineering interviews.

## 📊 About DataHub

DataHub is an open-source metadata platform that helps organizations discover, understand, and trust their data. Acryl Data (founded 2020, ~50 employees) is the company behind DataHub, offering a managed version with enterprise features. They focus on data cataloging, lineage tracking, and data governance.

## 📁 Structure

This folder contains **practice problems** and **comprehensive documentation** for DataHub interviews.

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
python 01_metadata_lineage_graph.py
```

### To Practice Again
```bash
# Simply reset the solution file (keep scaffolding)
rm 01_metadata_lineage_graph_solution.py
# Or manually clear your code and start fresh
```

## 📝 Problems List

### Python Algorithm Problems (Problems 1-4)

1. **Metadata Lineage Graph** - Track data dependencies using directed graphs
2. **Metadata Search Index** - Efficient search with prefix matching and ranking
3. **Schema Evolution Tracking** - Version control for schemas with compatibility checks
4. **Data Quality Monitoring** - Anomaly detection in data quality metrics

### ⚠️ Java Concurrency Problems (Problems 5-7) - FIRST ROUND FOCUS

**DataHub explicitly tests multithreading/concurrency in Round 1 interviews.**

5. **Thread-Safe Metadata Cache** (Java) - LRU cache with ReadWriteLock
6. **Producer-Consumer Ingestion** (Java) - BlockingQueue pattern for metadata events
7. **Concurrent Batch Processor** (Java) - Thread pools with ExecutorService

See `README_JAVA_CONCURRENCY.md` for Java setup and concurrency concepts.

## 📖 Complete Documentation

See `datahub_interview_questions.pdf` for:
- Complete problem descriptions
- Full solutions with explanations
- Time/space complexity analysis
- Test cases and edge cases
- Interview tips and strategies

## 🔧 Tech Stack Focus

DataHub uses:
- **Backend**: **Java (Spring Boot)** - PRIMARY LANGUAGE FOR INTERVIEWS
- **Storage**: MySQL/PostgreSQL for metadata, Elasticsearch for search
- **Graph**: Neo4j or graph databases for lineage
- **Message Queue**: Kafka for metadata ingestion
- **Frontend**: React, TypeScript
- **Cloud**: Kubernetes, Docker for deployment

**Important**: While Python problems (1-4) are good for algorithm practice, **Java problems (5-7) are critical** because:
1. DataHub's backend is Java
2. Round 1 explicitly tests Java concurrency
3. Production systems use Java's concurrency primitives

## 💡 Interview Process

Based on typical data infrastructure startups:

1. **Recruiter Screen** - Background, interest in data infrastructure (30 min)
2. **Technical Phone Screen** - LeetCode medium + data structures (45-60 min)
3. **Take-Home Assignment** - Build a metadata API or data processing pipeline (2-4 hours)
4. **Onsite/Virtual Rounds** (4-5 hours):
   - System Design - Design a metadata catalog or lineage system
   - Coding - LeetCode medium/hard, focus on graphs and data structures
   - Technical Deep Dive - Discuss past projects and technical decisions
   - Cultural Fit - Team collaboration and values alignment

## 🎓 Preparation Tips

### Master These Topics:
- **Graph Algorithms**: DFS/BFS, topological sort, cycle detection (critical for lineage)
- **Search/Indexing**: Prefix trees, inverted indices, ranking algorithms
- **Data Structures**: Hash maps, heaps, trees for efficient metadata storage
- **System Design**: Distributed systems, scalability, consistency
- **Databases**: SQL optimization, indexing strategies
- **Streaming**: Kafka, event-driven architectures

### Data Infrastructure Knowledge:
- **Metadata Management**: Data catalogs, data dictionaries, business glossaries
- **Data Lineage**: Column-level and table-level lineage tracking
- **Schema Management**: Schema registry, evolution, compatibility
- **Data Quality**: Profiling, validation, anomaly detection
- **Data Governance**: Access control, compliance, audit logs

### Technical Discussion Topics:
- Graph database vs relational database trade-offs
- Building scalable search systems
- Handling schema changes in production
- Real-time metadata ingestion architectures
- Metadata versioning and historical tracking

### Practice Strategy:
1. Solve all problems without looking at solutions
2. Focus on graph problems - DataHub is heavily graph-based
3. Practice explaining system design trade-offs
4. Study open-source DataHub architecture on GitHub
5. Understand distributed systems concepts

## 📚 Additional Resources

- **LeetCode**: Focus on graphs, trees, search algorithms (medium/hard)
- **System Design**:
  - "Designing Data-Intensive Applications" by Martin Kleppmann
  - Grokking the System Design Interview
- **DataHub Open Source**: Study the codebase on GitHub
- **Data Engineering**: "Fundamentals of Data Engineering" by Joe Reis
- **Metadata Standards**: Apache Atlas, Amundsen architecture

## ✅ Testing Your Solutions

All problems include comprehensive test suites:
```bash
# Run individual problem
python 01_metadata_lineage_graph.py

# Check all problems
for file in 0*_*.py; do
    [ "$file" != *"_solution.py" ] && python "$file"
done
```

## 🚀 Quick Start Example

```python
# 1. Open 01_metadata_lineage_graph_solution.py
# 2. Implement the class:

from collections import defaultdict, deque

class MetadataLineage:
    def __init__(self):
        self.graph = defaultdict(list)  # source -> [targets]

    def add_dependency(self, target: str, source: str) -> None:
        self.graph[source].append(target)

    def get_downstream(self, dataset: str) -> List[str]:
        visited = set()
        queue = deque([dataset])

        while queue:
            node = queue.popleft()
            if node in visited:
                continue
            visited.add(node)

            for neighbor in self.graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)

        visited.discard(dataset)  # Don't include source
        return list(visited)

# 3. Run tests:
# python 01_metadata_lineage_graph.py
#
# Output:
# ✓ Test 1 passed: Basic downstream dependencies work
# ✓ Test 2 passed: Multiple dependencies work
# ...
# All tests passed! ✓
```

## 🎯 Interview Focus Areas

### For DataHub/Acryl Data Specifically:
1. **Graph Knowledge**: Deep understanding of graph algorithms and data structures
2. **Scalability**: Experience with large-scale distributed systems
3. **Data Engineering**: Understanding of modern data stacks and tools
4. **Open Source**: Familiarity with DataHub project (study GitHub repo!)
5. **Product Thinking**: How metadata helps data teams work better

### Common Interview Questions:
- "Design a data lineage tracking system"
- "How would you build a search index for millions of datasets?"
- "Explain how you'd handle schema evolution in a production system"
- "Design a system to detect data quality issues automatically"
- "How would you ensure consistency in a distributed metadata system?"

### System Design Deep Dives:
- **Metadata Catalog**: How to store and query billions of metadata entries
- **Lineage Graph**: Efficient storage and traversal of large dependency graphs
- **Real-time Ingestion**: Processing metadata events from hundreds of data sources
- **Search Ranking**: Relevance algorithms for dataset discovery

## 💬 Behavioral Preparation

DataHub/Acryl Data values:
- **Data Democratization**: Making data accessible to everyone
- **Open Source First**: Commitment to open-source community
- **Engineering Excellence**: High-quality, scalable systems
- **Customer-Centric**: Solving real data discovery problems

Be ready to discuss:
- Why data infrastructure? Why metadata management?
- Experience with open-source projects
- Building scalable backend systems
- Working with data engineering teams
- Balancing product features vs technical debt

## 📊 Understanding DataHub

### Core Concepts:
- **Entities**: Datasets, Charts, Dashboards, Pipelines, ML Models
- **Aspects**: Metadata facets (schema, ownership, lineage, tags)
- **MCE/MAE**: Metadata Change Events/Metadata Audit Events
- **GMS**: General Metadata Service (backend API)
- **MCL**: Metadata Change Log (event stream)

### Key Features to Understand:
1. **Discovery**: Search and browse data assets
2. **Lineage**: Understand data flow and dependencies
3. **Governance**: Ownership, tags, glossary terms
4. **Observability**: Data quality, freshness, volume

### Architecture:
- **Frontend**: React UI for data discovery
- **Backend**: Spring Boot APIs for metadata CRUD
- **Search**: Elasticsearch for full-text search
- **Graph**: Neo4j or in-memory for lineage
- **Storage**: MySQL/Postgres for primary storage
- **Ingestion**: Kafka for event streaming

## 📞 Good Luck!

Remember: DataHub/Acryl Data is looking for engineers who are **passionate about data infrastructure**, **experienced with distributed systems**, and **excited about solving metadata challenges at scale**. Show your graph algorithm skills, system design thinking, and enthusiasm for their mission!

---

*Note: Since DataHub/Acryl Data has limited public interview data, these problems are based on the open-source DataHub project, typical data infrastructure challenges, and metadata platform requirements. Study the DataHub GitHub repository to understand their architecture and technical choices.*
