/*
Solution for Problem 1: Receipt Data Analysis

TODO: Implement SQL queries to answer the 8 questions in the problem statement.

Hints and Solution Approaches:
-------------------------------

1. TOP SPENDING USERS
   Approach:
   - JOIN users and receipts
   - Filter for last 30 days (scan_date >= CURRENT_DATE - INTERVAL '30 days')
   - GROUP BY user_id, username
   - Calculate SUM(total_spent), COUNT(*), AVG(total_spent)
   - ORDER BY total_spent DESC
   - LIMIT 5

   Example:
   SELECT
       u.user_id,
       u.username,
       SUM(r.total_spent) AS total_spent,
       COUNT(r.receipt_id) AS receipt_count,
       AVG(r.total_spent) AS avg_receipt_value
   FROM users u
   JOIN receipts r ON u.user_id = r.user_id
   WHERE r.scan_date >= CURRENT_DATE - INTERVAL '30 days'
   GROUP BY u.user_id, u.username
   ORDER BY total_spent DESC
   LIMIT 5;

2. MONTHLY ACTIVE USERS
   Approach:
   - Extract month from scan_date (DATE_TRUNC or TO_CHAR)
   - COUNT(DISTINCT user_id) per month
   - Filter for 2024 (EXTRACT(YEAR FROM scan_date) = 2024)

   Example:
   SELECT
       TO_CHAR(scan_date, 'YYYY-MM') AS month,
       COUNT(DISTINCT user_id) AS active_user_count
   FROM receipts
   WHERE EXTRACT(YEAR FROM scan_date) = 2024
   GROUP BY TO_CHAR(scan_date, 'YYYY-MM')
   ORDER BY month;

3. BRAND PERFORMANCE
   Approach:
   - JOIN items and brands
   - GROUP BY brand_id, brand_name
   - Calculate SUM(quantity), SUM(final_price), AVG(final_price)
   - COUNT(DISTINCT receipt_id)
   - HAVING SUM(quantity) >= 2

   Example:
   SELECT
       b.brand_id,
       b.brand_name,
       SUM(i.quantity) AS total_quantity,
       SUM(i.final_price) AS total_revenue,
       AVG(i.final_price / i.quantity) AS avg_price_per_item,
       COUNT(DISTINCT i.receipt_id) AS receipt_count
   FROM items i
   JOIN brands b ON i.brand_id = b.brand_id
   GROUP BY b.brand_id, b.brand_name
   HAVING SUM(i.quantity) >= 2
   ORDER BY total_revenue DESC;

4. USER RETENTION
   Approach:
   - Use CTE to get users active in Dec 2024
   - Use CTE to get users active in Jan 2025
   - Find intersection (users in both months)
   - Calculate percentage: (both_months / dec_users) * 100

   Example:
   WITH dec_users AS (
       SELECT DISTINCT user_id
       FROM receipts
       WHERE scan_date >= '2024-12-01' AND scan_date < '2025-01-01'
   ),
   jan_users AS (
       SELECT DISTINCT user_id
       FROM receipts
       WHERE scan_date >= '2025-01-01' AND scan_date < '2025-02-01'
   )
   SELECT
       ROUND(
           (COUNT(DISTINCT jan_users.user_id)::NUMERIC /
            COUNT(DISTINCT dec_users.user_id) * 100), 2
       ) AS retention_rate
   FROM dec_users
   LEFT JOIN jan_users ON dec_users.user_id = jan_users.user_id;

5. RECEIPT VALUE RANKING
   Approach:
   - Use RANK() window function
   - Partition by user_id for rank_within_user
   - No partition for overall_rank

   Example:
   SELECT
       receipt_id,
       user_id,
       total_spent,
       RANK() OVER (PARTITION BY user_id ORDER BY total_spent DESC) AS rank_within_user,
       RANK() OVER (ORDER BY total_spent DESC) AS overall_rank
   FROM receipts
   ORDER BY user_id, rank_within_user;

6. GAP ANALYSIS
   Approach:
   - Use LEAD() window function to get next scan_date
   - Calculate difference between consecutive scans
   - Filter for gaps > 7 days

   Example:
   WITH receipt_pairs AS (
       SELECT
           user_id,
           scan_date AS earlier_scan_date,
           LEAD(scan_date) OVER (PARTITION BY user_id ORDER BY scan_date) AS later_scan_date
       FROM receipts
   )
   SELECT
       user_id,
       earlier_scan_date,
       later_scan_date,
       later_scan_date - earlier_scan_date AS days_between
   FROM receipt_pairs
   WHERE later_scan_date - earlier_scan_date > 7
   ORDER BY days_between DESC;

7. STORE COMPARISON
   Approach:
   - GROUP BY store_name
   - Calculate aggregates

   Example:
   SELECT
       store_name,
       COUNT(receipt_id) AS total_receipts,
       SUM(total_spent) AS total_revenue,
       AVG(total_spent) AS avg_receipt_value,
       COUNT(DISTINCT user_id) AS unique_customers
   FROM receipts
   GROUP BY store_name
   ORDER BY total_revenue DESC;

8. WEEKLY SPENDING TREND
   Approach:
   - Use DATE_TRUNC('week', scan_date) to group by week
   - Filter for last 8 weeks
   - Calculate week_number using EXTRACT

   Example:
   SELECT
       DATE_TRUNC('week', scan_date)::DATE AS week_start_date,
       EXTRACT(WEEK FROM scan_date) AS week_number,
       SUM(total_spent) AS total_spent,
       COUNT(receipt_id) AS receipt_count
   FROM receipts
   WHERE scan_date >= CURRENT_DATE - INTERVAL '8 weeks'
   GROUP BY DATE_TRUNC('week', scan_date), EXTRACT(WEEK FROM scan_date)
   ORDER BY week_start_date DESC;

*/

-- 1. TOP SPENDING USERS
-- TODO: Implement query



-- 2. MONTHLY ACTIVE USERS
-- TODO: Implement query



-- 3. BRAND PERFORMANCE
-- TODO: Implement query



-- 4. USER RETENTION
-- TODO: Implement query



-- 5. RECEIPT VALUE RANKING
-- TODO: Implement query



-- 6. GAP ANALYSIS
-- TODO: Implement query



-- 7. STORE COMPARISON
-- TODO: Implement query



-- 8. WEEKLY SPENDING TREND
-- TODO: Implement query
