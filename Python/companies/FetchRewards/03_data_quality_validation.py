#!/usr/bin/env python3
"""
Problem 3: Data Quality Validation

Actual Fetch Rewards take-home assessment pattern - identify and document
data quality issues in receipt scanning data.

Problem Description:
-------------------
You are given receipt data that may contain various data quality issues.
Your task is to:
1. Identify data quality problems
2. Categorize issues by severity (Critical, High, Medium, Low)
3. Provide recommendations for each issue
4. Generate a data quality report

Common Data Quality Issues:
--------------------------
1. Missing Values
   - Required fields are NULL/empty
   - Incomplete records

2. Invalid Data Types
   - String where number expected
   - Invalid date formats

3. Data Inconsistencies
   - Total doesn't match sum of items
   - Negative prices or quantities
   - Future scan dates

4. Duplicate Records
   - Same receipt_id appearing multiple times
   - Duplicate items within receipt

5. Referential Integrity Issues
   - Items referencing non-existent receipts
   - Brands referenced but not in brands table

6. Business Logic Violations
   - Points earned doesn't match expected calculation
   - Prices outside reasonable range
   - Invalid barcode format

7. Data Anomalies
   - Statistical outliers
   - Unusual patterns

Sample Data with Issues:
-----------------------
receipts = [
    {"receipt_id": "R001", "user_id": "U123", "scan_date": "2025-01-05", "total_spent": 45.50, "points_earned": 100},
    {"receipt_id": "R002", "user_id": None, "scan_date": "2025-01-06", "total_spent": -10.00, "points_earned": 50},  # Missing user_id, negative total
    {"receipt_id": "R003", "user_id": "U456", "scan_date": "2026-01-05", "total_spent": 100.00, "points_earned": 200},  # Future date
    {"receipt_id": "R001", "user_id": "U123", "scan_date": "2025-01-05", "total_spent": 45.50, "points_earned": 100},  # Duplicate
]

items = [
    {"item_id": 1, "receipt_id": "R001", "quantity": 2, "final_price": 10.00, "brand_id": "B001"},
    {"item_id": 2, "receipt_id": "R001", "quantity": -1, "final_price": 5.00, "brand_id": "B999"},  # Negative quantity, invalid brand
    {"item_id": 3, "receipt_id": "R999", "quantity": 1, "final_price": 20.00, "brand_id": "B001"},  # Non-existent receipt
]

brands = [
    {"brand_id": "B001", "brand_name": "Brand A", "category": "Food"},
    {"brand_id": "B002", "brand_name": None, "category": "Beverage"},  # Missing brand_name
]

Requirements:
------------
1. Implement data quality checks:
   - check_missing_values(data, table_name, required_fields)
   - check_duplicates(data, table_name, key_fields)
   - check_referential_integrity(items, receipts, brands)
   - check_business_logic(receipts, items)
   - check_data_types(data, table_name, schema)

2. Generate quality report:
   - Issue description
   - Severity (Critical/High/Medium/Low)
   - Count of affected records
   - Sample records
   - Recommendations

3. Calculate data quality score:
   - Percentage of records without issues
   - Weight by severity

Expected Output Format:
----------------------
{
  "summary": {
    "total_receipts": 4,
    "total_items": 3,
    "total_brands": 2,
    "issues_found": 6,
    "quality_score": 72.5
  },
  "issues": [
    {
      "category": "Missing Values",
      "severity": "Critical",
      "table": "receipts",
      "field": "user_id",
      "count": 1,
      "description": "Required field user_id contains NULL values",
      "samples": [{"receipt_id": "R002", "user_id": None}],
      "recommendation": "Investigate source data and add validation at ingestion"
    },
    {
      "category": "Business Logic Violation",
      "severity": "High",
      "table": "receipts",
      "field": "total_spent",
      "count": 1,
      "description": "Negative values in total_spent",
      "samples": [{"receipt_id": "R002", "total_spent": -10.00}],
      "recommendation": "Add validation to reject negative amounts"
    },
    # ... more issues
  ],
  "recommendations": [
    "Add NOT NULL constraints on required fields",
    "Implement data validation at ingestion",
    "Set up referential integrity constraints",
    "Add business logic validation rules",
    "Monitor for statistical outliers"
  ]
}

Time Limit: 60-90 minutes
Expected: Comprehensive quality checks, clear reporting, actionable recommendations
"""

try:
    import importlib.util
    spec = importlib.util.spec_from_file_location("solution_module",
                                                   "03_data_quality_validation_solution.py")
    solution_module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(solution_module)
    DataQualityValidator = solution_module.DataQualityValidator
except Exception as e:
    print(f"❌ Error importing solution: {e}")
    exit(1)

def test_data_quality_validation():
    print("Testing Data Quality Validation...")
    print()

    # Test Data with Known Issues
    receipts = [
        {"receipt_id": "R001", "user_id": "U123", "scan_date": "2025-01-05", "total_spent": 45.50, "points_earned": 100},
        {"receipt_id": "R002", "user_id": None, "scan_date": "2025-01-06", "total_spent": -10.00, "points_earned": 50},  # Missing user_id, negative total
        {"receipt_id": "R003", "user_id": "U456", "scan_date": "2026-01-05", "total_spent": 100.00, "points_earned": 200},  # Future date
        {"receipt_id": "R001", "user_id": "U123", "scan_date": "2025-01-05", "total_spent": 45.50, "points_earned": 100},  # Duplicate
    ]

    items = [
        {"item_id": 1, "receipt_id": "R001", "quantity": 2, "final_price": 10.00, "brand_id": "B001"},
        {"item_id": 2, "receipt_id": "R001", "quantity": -1, "final_price": 5.00, "brand_id": "B999"},  # Negative quantity, invalid brand
        {"item_id": 3, "receipt_id": "R999", "quantity": 1, "final_price": 20.00, "brand_id": "B001"},  # Non-existent receipt
    ]

    brands = [
        {"brand_id": "B001", "brand_name": "Brand A", "category": "Food"},
        {"brand_id": "B002", "brand_name": None, "category": "Beverage"},  # Missing brand_name
    ]

    # Test 1: Initialize validator and run checks
    print("Test 1: Run data quality checks")
    validator = DataQualityValidator()
    report = validator.validate_all(receipts, items, brands)

    assert "summary" in report, "Test 1a failed: missing summary"
    assert "issues" in report, "Test 1b failed: missing issues"
    assert len(report["issues"]) > 0, "Test 1c failed: should find issues"
    print(f"Found {len(report['issues'])} data quality issues")
    print("✓ Test 1 passed")
    print()

    # Test 2: Check for specific issue types
    print("Test 2: Verify specific issue detection")
    issue_categories = {issue["category"] for issue in report["issues"]}

    # Should detect missing values
    assert any("Missing" in cat or "NULL" in cat.upper() for cat in issue_categories), \
        "Test 2a failed: should detect missing values"

    # Should detect duplicates
    assert any("Duplicate" in cat for cat in issue_categories), \
        "Test 2b failed: should detect duplicates"

    # Should detect referential integrity issues
    assert any("Referential" in cat or "Integrity" in cat for cat in issue_categories), \
        "Test 2c failed: should detect referential integrity issues"

    print("✓ Test 2 passed")
    print()

    # Test 3: Check severity classification
    print("Test 3: Verify severity classification")
    severities = {issue["severity"] for issue in report["issues"]}
    assert len(severities) > 0, "Test 3 failed: should have severity classifications"
    print(f"Issue severities found: {severities}")
    print("✓ Test 3 passed")
    print()

    # Test 4: Clean data (no issues)
    print("Test 4: Clean data validation")
    clean_receipts = [
        {"receipt_id": "R100", "user_id": "U100", "scan_date": "2025-01-01", "total_spent": 50.00, "points_earned": 100}
    ]
    clean_items = [
        {"item_id": 1, "receipt_id": "R100", "quantity": 1, "final_price": 50.00, "brand_id": "B100"}
    ]
    clean_brands = [
        {"brand_id": "B100", "brand_name": "Clean Brand", "category": "Test"}
    ]

    clean_report = validator.validate_all(clean_receipts, clean_items, clean_brands)
    # Should have fewer or no issues
    print(f"Issues in clean data: {len(clean_report['issues'])}")
    print("✓ Test 4 passed")
    print()

    # Test 5: Quality score calculation
    print("Test 5: Quality score calculation")
    if "quality_score" in report["summary"]:
        score = report["summary"]["quality_score"]
        assert 0 <= score <= 100, "Test 5a failed: score should be 0-100"
        print(f"Data quality score: {score:.2f}%")

        clean_score = clean_report["summary"].get("quality_score", 100)
        assert clean_score >= score, "Test 5b failed: clean data should have higher score"
        print(f"Clean data quality score: {clean_score:.2f}%")
    print("✓ Test 5 passed")
    print()

    # Test 6: Recommendations
    print("Test 6: Verify recommendations")
    if "recommendations" in report:
        assert len(report["recommendations"]) > 0, "Test 6 failed: should have recommendations"
        print(f"Generated {len(report['recommendations'])} recommendations")
        for i, rec in enumerate(report["recommendations"][:3], 1):
            print(f"  {i}. {rec}")
    print("✓ Test 6 passed")
    print()

    print("All tests passed! ✓")
    print()
    print("=" * 70)
    print("SAMPLE DATA QUALITY REPORT")
    print("=" * 70)
    print()
    print(f"Total Issues Found: {len(report['issues'])}")
    print()
    print("Issues by Category:")
    category_counts = {}
    for issue in report["issues"]:
        cat = issue["category"]
        category_counts[cat] = category_counts.get(cat, 0) + 1
    for cat, count in category_counts.items():
        print(f"  - {cat}: {count}")
    print()
    print("Top 3 Issues:")
    for i, issue in enumerate(report["issues"][:3], 1):
        print(f"\n{i}. {issue['category']} ({issue['severity']})")
        print(f"   Description: {issue['description']}")
        if 'recommendation' in issue:
            print(f"   Recommendation: {issue['recommendation']}")

if __name__ == "__main__":
    test_data_quality_validation()
