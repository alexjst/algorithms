# ServiceTitan Software Engineer Interview Prep

Focused preparation materials for ServiceTitan software engineering interviews.

## 📊 About ServiceTitan

ServiceTitan (founded 2013, ~2,000+ employees) is a leading software platform for home and commercial service businesses. Provides end-to-end business management solutions including scheduling, dispatching, CRM, invoicing, and reporting.

**Headquarters**: Glendale, CA
**Valuation**: ~$9.5 billion (2022)
**Tech Stack**: .NET/C#, Python, SQL Server, Azure, React, Microservices

## 📁 Structure

This folder contains **practice problems** and **documentation** for ServiceTitan interviews.

### Practice Files

Each problem has **TWO files**:
1. **`XX_problem_name.py`** - Scaffolding file with tests (DON'T EDIT)
2. **`XX_problem_name_solution.py`** - Your implementation (EDIT THIS)

## 🎯 How to Practice

### First Time
```bash
# 1. Read the problem in the scaffolding file
# 2. Implement your solution in the _solution.py file
# 3. Run tests
python 01_first_non_repeating_char.py
```

### To Practice Again
```bash
# Simply reset the solution file
rm 01_first_non_repeating_char_solution.py
# Or manually clear your code and start fresh
```

## 📝 Problems List

### Coding Problems (Problems 1-6)

Based on actual ServiceTitan interview questions (2023-2025):

1. **First Non-Repeating Character** (Easy) - String manipulation, hash maps
2. **Equal Subset Sum** (Medium) - Dynamic programming, subset partition
3. **Multimap Implementation** (Medium-Hard) - Data structure design, collections
4. **Binary Tree Serialization** (Medium) - Tree traversal, BFS/DFS, string parsing
5. **URL Shortener** (Medium) - System design, hash maps, encoding algorithms
6. **Event Processing System** (Medium-Hard) - Pub/sub pattern, error handling, collections

### System Design Problems

Common ServiceTitan system design questions:

- **Real-Time Hashtag Partitioning** - Tweet ingestion and processing pipeline
- **Centralized Event Ingestion** - Multi-application event processing system
- **Service Business Management** - Scheduling, dispatching, technician routing

## 💡 Interview Process

Based on actual candidate experiences (2023-2025):

1. **HackerRank Assessment** - SQL and coding problems (1-2 hours)
2. **Technical Phone Screen** - Discuss projects, coding fundamentals (60 min)
3. **Code Pairing Interview** - Live coding in C# or Python (60-90 min)
4. **System Design** - Data pipeline or backend architecture (60 min)
5. **Behavioral/Culture Fit** - Team collaboration, values alignment (30-45 min)

## 🎓 Interview Characteristics

### Key Differences from Other Companies:

1. **C#/.NET Focus** - Strong preference for C# experience, though Python accepted
2. **Practical Problems** - Focus on real-world implementations (multimap, caching, data structures)
3. **Simple but Bug-Free** - Problems are simpler than FAANG but expect perfect implementation
4. **System Design Emphasis** - Strong focus on data pipelines and event processing
5. **Domain Knowledge** - Understanding of service business workflows is a plus

### Difficulty Assessment:
- **HackerRank**: Medium difficulty, SQL heavy
- **Interview Rating**: 2.8/5 difficulty (moderate)
- **Timeline**: Average 2-3 weeks to complete hiring process
- **Success Rate**: Moderate, focus on clean code and fundamentals

## 🔧 Tech Stack Focus

ServiceTitan uses:
- **Backend**: C# (.NET Core), Python, Node.js
- **Frontend**: React, TypeScript, Angular
- **Database**: SQL Server, PostgreSQL, Redis
- **Cloud**: Azure (primary), AWS
- **Data**: Kafka, Azure Event Hubs, Stream Analytics
- **Architecture**: Microservices, Event-Driven, Domain-Driven Design

## 🎯 Preparation Tips

### Master These Topics:

**For Software Engineers:**
- **C# Fundamentals**: Async/await, LINQ, collections, interfaces
- **Data Structures**: Hash maps, sets, queues, custom collections
- **Algorithms**: String manipulation, DP, searching, sorting
- **System Design**: Event-driven architecture, message queues, microservices
- **SQL**: Joins, aggregations, window functions, query optimization
- **OOP**: SOLID principles, design patterns, interface design

**ServiceTitan-Specific:**
- **Domain Knowledge**: Understanding of service businesses (HVAC, plumbing, electrical)
- **Real-Time Processing**: Stream processing, event handling, data pipelines
- **Multi-Tenancy**: SaaS architecture, data isolation, scalability
- **Business Logic**: Scheduling algorithms, routing optimization, pricing

## 📚 Additional Resources

- **LeetCode**: Easy/Medium problems, focus on hash maps, strings, DP
  - Practice: First unique character, subset sum, two sum variants
- **C# Practice**:
  - Collections framework deep dive
  - Async/await patterns
  - Interface implementation
- **System Design**:
  - Event-driven architecture patterns
  - Message queue design (Kafka, RabbitMQ)
  - Real-time data processing
- **SQL**:
  - Window functions
  - Complex joins
  - Data modeling from JSON

## 📖 Common Interview Questions

### Coding (from recent experiences):

**Most Common**:
- "Find the first non-repeating character in a string"
- "Equal subset sum partition"
- "Implement a multimap with union/intersection operations"
- "Serialize and deserialize a binary tree"
- "Design a URL shortening service"
- "Implement an event processing/pub-sub system"

**Other Questions**:
- Caching service implementation
- Search in list of objects
- Map containing a map implementation
- ICollection interface implementation

### System Design (from recent interviews):

**Data Pipeline Focus**:
- "Design a real-time tweet hashtag partitioning system"
- "Design centralized event ingestion for multiple applications"
- "Design a streaming data pipeline from raw data to analytics"

**ServiceTitan-Specific**:
- "Design a technician scheduling and routing system"
- "Design a multi-tenant invoicing system"
- "Design real-time job status tracking"

## 💬 Behavioral Preparation

ServiceTitan values:
- **Customer Focus**: Building for SMB service businesses
- **Ownership**: Taking responsibility for features end-to-end
- **Team Collaboration**: Working across engineering, product, and customer success
- **Growth Mindset**: Learning new technologies and domain knowledge

Be ready to discuss:
- Why ServiceTitan? Why service industry software?
- Experience with backend systems and data pipelines
- Times you solved complex technical problems
- How you ensure code quality and maintainability
- Experience with microservices or event-driven architecture

## ⚠️ Important Notes

### What Makes ServiceTitan Interviews Unique:

1. **C# Preference**: Most teams use C#, though Python is accepted
2. **HackerRank Focus**: Heavy SQL component, expect data manipulation
3. **Practical Over Theoretical**: Focus on implementable solutions
4. **Domain Context**: Understanding service business workflows helps
5. **Code Quality**: Clean, maintainable code matters more than optimal complexity

### Red Flags (Common Rejection Reasons):

- ❌ Poor SQL skills (critical for role)
- ❌ Inability to implement basic data structures
- ❌ Buggy code or incomplete implementations
- ❌ Poor async/await understanding (for C# roles)
- ❌ Weak system design reasoning
- ❌ Lack of practical backend experience

## 💰 Compensation (2024-2025)

- **Software Engineer (L2-L3)**: $120K - $160K base + equity
- **Senior Software Engineer (L4)**: $160K - $200K base + equity
- **Staff Engineer (L5)**: $200K - $240K base + equity
- **Equity**: Stock options, typically 4-year vest

## 🚀 Quick Start Example

```python
# 1. Open 01_first_non_repeating_char_solution.py
# 2. Implement the function:

def firstUniqChar(s: str) -> int:
    # Count character frequencies
    char_count = {}
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1

    # Find first character with count 1
    for i, char in enumerate(s):
        if char_count[char] == 1:
            return i

    return -1

# 3. Run tests:
# python 01_first_non_repeating_char.py
```

## 📞 Good Luck!

Remember: ServiceTitan is looking for engineers who are **detail-oriented**, **customer-focused**, and **can write clean, maintainable code**. Show your practical problem-solving skills and understanding of real-world systems!

---

*Note: These problems are based on actual ServiceTitan interview questions from Glassdoor, Blind, InterviewQuery, and candidate experiences (2023-2025). The interview process may vary by team and role.*
