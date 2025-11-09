# Fetch Rewards Data Engineer / Analytics Engineer Interview Prep

Focused preparation materials for Fetch Rewards data engineering and analytics engineering interviews.

## 📊 About Fetch Rewards

Fetch Rewards (founded 2013, ~1,000 employees) is a shopping rewards platform where users earn points by scanning receipts. The platform partners with brands to provide personalized offers and rewards.

**Headquarters**: Chicago, IL
**Valuation**: ~$2.5 billion (2021)
**Tech Stack**: Python, SQL, AWS (Redshift, S3, Lambda), Spark, Kafka, Airflow, dbt

## 📁 Structure

This folder contains **practice problems** and **take-home assessment prep** for Fetch Rewards interviews.

### Practice Files

Each problem has **TWO files**:
1. **`XX_problem_name.sql`** or **`XX_problem_name.py`** - Problem statement
2. **`XX_problem_name_solution.sql`** or **`XX_problem_name_solution.py`** - Your implementation

## 🎯 How to Practice

### SQL Problems
```bash
# 1. Read the problem in the .sql file
# 2. Write your query in the _solution.sql file
# 3. Test with sample data (provided in problem file)
```

### Python Problems
```bash
# 1. Read the problem in the .py file
# 2. Implement your solution in the _solution.py file
# 3. Run tests
python 03_json_to_relational.py
```

## 📝 Problems List

### SQL Problems (Problems 1-3)

Based on actual Fetch Rewards assessments and interview questions:

1. **Receipt Data Analysis** (Medium) - Joins, aggregations, window functions
2. **User Spending Patterns** (Medium) - CTEs, date functions, ranking
3. **Brand Performance Metrics** (Medium-Hard) - Complex joins, analytics functions

### Python Problems (Problems 4-6)

Based on actual Fetch Rewards take-home assessments:

4. **JSON to Relational Transformation** (Medium) - Data modeling, ETL
5. **Data Quality Validation** (Medium) - Error detection, data profiling
6. **Streaming Receipt Processor** (Hard) - Event processing, state management

## 💡 Interview Process

Based on actual candidate experiences (2023-2025):

1. **Phone Screen** - Behavioral, background discussion (30 min)
2. **SQL Assessment** - Live coding or take-home SQL challenge (60-90 min)
3. **Take-Home Project** - Data engineering project (4-8 hours, 48-hour window)
4. **Technical Deep Dive** - Discuss take-home, data concepts (60-90 min)
5. **Final Round** - System design + behavioral (2-3 hours)

## 🎓 Interview Characteristics

### Key Focus Areas:

1. **SQL Mastery** - Core competency, complex analytical queries required
2. **Data Modeling** - JSON to relational, star schema, normalization
3. **Data Quality** - Identifying issues, validation rules, data profiling
4. **Python/PySpark** - Data transformation, ETL pipelines
5. **AWS Services** - S3, Redshift, Lambda, Glue knowledge is a plus
6. **Communication** - Ability to explain technical decisions clearly

### Take-Home Assessment Characteristics:

**What to Expect**:
- **Duration**: 4-8 hours of work, 48-72 hour submission window
- **Focus**: JSON data modeling, SQL queries, data quality analysis
- **Deliverables**: ERD diagram, SQL queries, data quality report, documentation
- **Evaluation Criteria**: Code quality, documentation, SQL efficiency, data modeling decisions

**Common Take-Home Components**:
1. Data modeling from JSON/semi-structured data
2. Writing analytical SQL queries
3. Data quality assessment and documentation
4. Python ETL script (optional)
5. README with design decisions and assumptions

### Difficulty Assessment:
- **SQL**: Medium-Hard, expect window functions and CTEs
- **Overall Rating**: 3.2/5 difficulty (moderate to challenging)
- **Timeline**: 2-4 weeks to complete hiring process
- **Success Rate**: Moderate, strong SQL skills are critical

## 🔧 Tech Stack Focus

Fetch Rewards uses:
- **Data Processing**: Python, PySpark, pandas
- **SQL**: PostgreSQL, Amazon Redshift
- **Data Pipeline**: Apache Airflow, AWS Lambda
- **Streaming**: Kafka, AWS Kinesis
- **Data Warehouse**: Redshift, Snowflake
- **Cloud**: AWS (S3, Glue, EMR, Lambda, Redshift)
- **BI Tools**: Tableau, Looker, dbt
- **ML**: Python (scikit-learn, TensorFlow)

## 🎯 Preparation Tips

### Master These Topics:

**For Data Engineers:**
- **SQL Advanced**: Window functions, CTEs, complex joins, query optimization
- **Data Modeling**: Star schema, normalization, JSON to relational
- **ETL/ELT**: Data pipelines, transformation logic, incremental loads
- **Data Quality**: Validation rules, anomaly detection, data profiling
- **Python**: pandas, PySpark, data transformation
- **AWS**: S3, Redshift, Lambda, Glue, Airflow

**For Analytics Engineers:**
- **SQL Mastery**: Analytical queries, business metrics, aggregations
- **dbt**: Models, tests, documentation, best practices
- **Data Warehousing**: Dimensional modeling, fact/dimension tables
- **BI Tools**: Tableau, Looker, dashboard design
- **Business Metrics**: KPIs, cohort analysis, funnel analytics

**Fetch-Specific Skills:**
- **Receipt Data**: Understanding receipt structure, OCR data, transaction data
- **User Behavior Analytics**: DAU/MAU, retention, engagement metrics
- **E-commerce Metrics**: GMV, conversion rates, basket analysis
- **Offer/Promotion Analysis**: Campaign performance, attribution

## 📚 Additional Resources

- **SQL Practice**:
  - LeetCode Database (Medium/Hard)
  - HackerRank SQL (Advanced)
  - Mode Analytics SQL Tutorial
  - Window Functions Deep Dive

- **Data Modeling**:
  - Kimball Dimensional Modeling
  - JSON to relational best practices
  - Star schema design patterns

- **Python/Data Engineering**:
  - pandas documentation
  - PySpark fundamentals
  - ETL design patterns
  - Data pipeline orchestration

- **AWS**:
  - Redshift best practices
  - S3 data lake patterns
  - Lambda for ETL
  - Glue catalog and crawlers

## 📖 Common Interview Questions

### SQL Questions (from recent assessments):

**Data Analysis**:
- "Find the top 10 users by total spending in the last 30 days"
- "Calculate monthly active users and retention rate"
- "Identify brands with highest average transaction value"
- "Find users who scanned receipts but haven't redeemed rewards"
- "Calculate running totals and moving averages for daily revenue"

**Window Functions**:
- "Rank users by spending within each category"
- "Find first and last purchase date for each user"
- "Calculate percent change in monthly revenue"
- "Identify gaps in user activity (days without scans)"

**Complex Joins**:
- "Join receipts, items, brands, and users to analyze purchase patterns"
- "Handle NULL values and missing data appropriately"
- "Self-joins to find user referral chains"

### Take-Home Assessment Questions:

**Data Modeling**:
- "Model receipt JSON data into a relational schema"
- "Design fact and dimension tables for analytics"
- "Create ERD for receipt scanning system"

**Data Quality**:
- "Identify data quality issues in receipt data"
- "Write validation rules for transaction data"
- "Detect duplicate or anomalous records"
- "Handle missing brand information"

**Python/ETL**:
- "Write ETL script to transform JSON receipts to relational format"
- "Implement data validation and error handling"
- "Create incremental load logic"
- "Process streaming receipt data"

### System Design Questions:

**Data Engineering**:
- "Design a real-time receipt processing pipeline"
- "Design a data warehouse for receipt analytics"
- "Design ETL pipeline for third-party data ingestion"
- "Design a system to detect fraudulent receipts"

**Analytics**:
- "Design dashboards for business stakeholders"
- "Design metrics for user engagement and retention"
- "Design A/B testing framework for offers"

## 💬 Behavioral Preparation

Fetch Rewards values:
- **Collaboration**: Working with data scientists, analysts, and engineers
- **Ownership**: Taking end-to-end responsibility for data quality
- **Innovation**: Finding creative solutions to data challenges
- **Customer Focus**: Understanding how data drives user experience

Be ready to discuss:
- Why Fetch Rewards? Why work in consumer apps/e-commerce?
- Experience with data pipelines and ETL
- Times you improved data quality or fixed data issues
- How you handle ambiguous requirements
- Experience with stakeholder communication
- Debugging and troubleshooting data issues

## ⚠️ Important Notes

### What Makes Fetch Rewards Interviews Unique:

1. **SQL-Heavy**: Expect 60-70% of technical assessment to be SQL
2. **Take-Home Focus**: Main technical evaluation is take-home project
3. **Data Quality Emphasis**: Strong focus on identifying and documenting data issues
4. **Documentation**: Communicate design decisions clearly in README
5. **Practical Over Perfect**: Working solution with good documentation > perfect code
6. **Extendability**: Code should be easy to extend and maintain

### Take-Home Best Practices:

✅ **DO**:
- Write clear, well-documented code
- Create comprehensive README with assumptions
- Use proper SQL formatting and indentation
- Include data quality analysis
- Explain design decisions
- Test your queries thoroughly
- Consider edge cases
- Use version control (Git)

❌ **DON'T**:
- Submit incomplete solutions
- Skip documentation
- Use overly complex solutions when simple works
- Ignore data quality issues
- Submit without testing
- Miss the deadline (late submissions rarely accepted)
- Plagiarize or use others' solutions

### Red Flags (Common Rejection Reasons):

- ❌ Weak SQL skills (dealbreaker for this role)
- ❌ Poor data modeling decisions
- ❌ Ignoring data quality issues
- ❌ Lack of documentation or unclear communication
- ❌ Unable to explain design choices
- ❌ Messy or unreadable code
- ❌ Missing deliverables in take-home

## 💰 Compensation (2024-2025)

- **Analytics Engineer**: $90K - $130K base + equity + bonus
- **Data Engineer (Mid)**: $110K - $150K base + equity + bonus
- **Senior Data Engineer**: $140K - $180K base + equity + bonus
- **Staff Data Engineer**: $170K - $210K base + equity + bonus
- **Benefits**: 401k match, health insurance, unlimited PTO

## 🚀 Example Take-Home Structure

Typical Fetch Rewards take-home includes:

```
submission/
├── README.md                 # Design decisions, assumptions, setup
├── schema.sql                # DDL for tables
├── data_model.png            # ERD diagram
├── queries.sql               # Analytical queries with comments
├── data_quality_report.md    # Issues found and recommendations
├── etl_script.py             # (Optional) Python ETL script
└── sample_data/              # Sample input/output data
    ├── receipts.json
    └── expected_output.csv
```

### Sample README Structure:

```markdown
# Fetch Rewards Data Engineering Assessment

## Overview
Brief description of solution approach

## Data Model Design
- Explain schema decisions
- Why normalized vs denormalized
- Handling of JSON fields
- Indexing strategy

## Assumptions
- List any assumptions made
- Data quality assumptions
- Business logic assumptions

## Setup Instructions
1. Create database
2. Run schema.sql
3. Load data
4. Execute queries.sql

## Data Quality Findings
1. Issue 1: Description and recommendation
2. Issue 2: Description and recommendation
...

## Query Explanations
Brief explanation of each analytical query

## Future Improvements
What would you add with more time?
```

## 📞 Good Luck!

Remember: Fetch Rewards is looking for data engineers who are **SQL experts**, **detail-oriented**, and **excellent communicators**. Focus on data quality, clear documentation, and practical solutions!

---

*Note: These problems are based on actual Fetch Rewards interview questions and take-home assessments from 一亩三分地, Glassdoor, Blind, and candidate experiences (2023-2025). The interview process may vary by team and role.*
