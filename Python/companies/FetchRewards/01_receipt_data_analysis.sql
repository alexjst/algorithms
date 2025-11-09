/*
Problem 1: Receipt Data Analysis

Actual Fetch Rewards assessment-style question - analyze receipt scanning data
to derive business insights.

Schema:
---------

users (user_id, username, email, created_date, state, last_login)
receipts (receipt_id, user_id, scan_date, total_spent, points_earned, store_name)
items (item_id, receipt_id, barcode, description, quantity, final_price, brand_id)
brands (brand_id, brand_name, category, cpg_id, top_brand)

Sample Data:
---------

users:
user_id | username  | email              | created_date | state | last_login
--------|-----------|--------------------|--------------| ------|------------
1       | alice     | alice@email.com    | 2024-01-15   | CA    | 2025-01-08
2       | bob       | bob@email.com      | 2024-02-20   | NY    | 2025-01-07
3       | charlie   | charlie@email.com  | 2024-03-10   | CA    | 2024-12-25

receipts:
receipt_id | user_id | scan_date  | total_spent | points_earned | store_name
-----------|---------|------------|-------------|---------------|------------
101        | 1       | 2025-01-05 | 45.50       | 100           | Target
102        | 1       | 2025-01-07 | 23.75       | 50            | Walmart
103        | 2       | 2025-01-06 | 67.20       | 150           | Target
104        | 3       | 2024-12-20 | 12.50       | 25            | CVS

items:
item_id | receipt_id | barcode      | description     | quantity | final_price | brand_id
--------|------------|--------------|-----------------|----------|-------------|----------
1001    | 101        | 012345678901 | Milk            | 2        | 7.00        | 1
1002    | 101        | 012345678902 | Bread           | 1        | 3.50        | 2
1003    | 102        | 012345678903 | Eggs            | 1        | 4.25        | 1
1004    | 103        | 012345678901 | Milk            | 3        | 10.50       | 1
1005    | 103        | 012345678904 | Cereal          | 2        | 8.00        | 3

brands:
brand_id | brand_name        | category      | cpg_id | top_brand
---------|-------------------|---------------|--------|----------
1        | Organic Valley    | Dairy         | 100    | TRUE
2        | Wonder Bread      | Bakery        | 101    | FALSE
3        | General Mills     | Breakfast     | 102    | TRUE

Questions to Answer:
--------------------

Write SQL queries to answer the following questions. Put your solutions in
01_receipt_data_analysis_solution.sql

1. TOP SPENDING USERS
   Find the top 5 users by total spending in the last 30 days.
   Include: user_id, username, total_spent, receipt_count, avg_receipt_value
   Order by: total_spent DESC

2. MONTHLY ACTIVE USERS
   Calculate the number of monthly active users (MAU) for each month in 2024.
   Include: month (YYYY-MM format), active_user_count
   A user is active if they scanned at least one receipt in that month.

3. BRAND PERFORMANCE
   For each brand, calculate:
   - Total quantity sold
   - Total revenue
   - Average price per item
   - Number of unique receipts containing the brand
   Filter to only include brands with at least 2 items sold.
   Order by total_revenue DESC

4. USER RETENTION
   Calculate the percentage of users who scanned receipts in both
   December 2024 AND January 2025.
   Return: retention_rate as a percentage (e.g., 66.67)

5. RECEIPT VALUE RANKING
   For each receipt, calculate:
   - receipt_id
   - user_id
   - total_spent
   - rank within user (partitioned by user_id, ordered by total_spent DESC)
   - overall_rank (across all receipts, ordered by total_spent DESC)
   Order by: user_id, rank_within_user

6. GAP ANALYSIS
   Find users who had gaps of more than 7 days between consecutive receipt scans.
   Include: user_id, earlier_scan_date, later_scan_date, days_between
   Order by: days_between DESC

7. STORE COMPARISON
   For each store, calculate:
   - store_name
   - total_receipts
   - total_revenue
   - avg_receipt_value
   - unique_customers
   Order by: total_revenue DESC

8. WEEKLY SPENDING TREND
   Calculate total spending by week for the last 8 weeks.
   Include: week_start_date, week_number, total_spent, receipt_count
   Order by: week_start_date DESC

Complexity:
-----------
- Queries 1-3: Medium (Joins, Aggregations)
- Queries 4-6: Medium-Hard (Window Functions, Self-Joins)
- Queries 7-8: Medium (Date Functions, CTEs)

Tips:
-----
1. Use proper date functions (DATE_TRUNC, EXTRACT, DATE_PART)
2. Window functions are essential for ranking and gaps
3. CTEs make complex queries more readable
4. Handle NULL values appropriately
5. Use proper JOIN types (INNER vs LEFT)
6. Consider edge cases (no receipts, single receipt, etc.)

Time Limit: 60-90 minutes
Expected: Complete 6-8 queries with good SQL style
*/

-- This is the problem statement file - DO NOT EDIT
-- Write your solutions in: 01_receipt_data_analysis_solution.sql
