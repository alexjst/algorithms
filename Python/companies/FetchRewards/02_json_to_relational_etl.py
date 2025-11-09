#!/usr/bin/env python3
"""
Problem 2: JSON to Relational ETL

Actual Fetch Rewards take-home assessment pattern - transform semi-structured
JSON receipt data into a normalized relational schema.

Problem Description:
-------------------
You are given JSON data representing receipt scans. Your task is to:
1. Design a relational schema to store this data
2. Write an ETL script to transform JSON to relational format
3. Handle missing/invalid data gracefully
4. Ensure data quality and integrity

Sample JSON Data:
-----------------
{
  "receipt_id": "R001",
  "scan_date": "2025-01-05T14:30:00Z",
  "store": {
    "name": "Target",
    "location": "San Francisco, CA"
  },
  "user": {
    "user_id": "U123",
    "email": "user@example.com"
  },
  "items": [
    {
      "barcode": "012345678901",
      "description": "Organic Milk",
      "quantity": 2,
      "unit_price": 3.50,
      "final_price": 7.00,
      "brand": {
        "brand_id": "B001",
        "name": "Organic Valley",
        "category": "Dairy"
      }
    },
    {
      "barcode": "012345678902",
      "description": "Bread",
      "quantity": 1,
      "unit_price": 3.99,
      "final_price": 3.99,
      "brand": {
        "brand_id": "B002",
        "name": "Wonder Bread",
        "category": "Bakery"
      }
    }
  ],
  "total_spent": 10.99,
  "points_earned": 50
}

Requirements:
------------
1. Design relational schema with appropriate tables:
   - receipts
   - items
   - brands
   - users (optional, can be simplified)

2. Implement ETL functions:
   - load_json(filepath) -> List[Dict]
   - transform_receipt(receipt_json) -> Dict[str, List[Dict]]
   - validate_data(data) -> Tuple[bool, List[str]]

3. Handle edge cases:
   - Missing fields (e.g., brand_id missing)
   - Invalid data types
   - Duplicate records
   - NULL values

4. Output format:
   - Dictionary with table names as keys
   - Lists of dictionaries representing rows

Expected Output Schema:
----------------------
{
  "receipts": [
    {
      "receipt_id": "R001",
      "user_id": "U123",
      "scan_date": "2025-01-05T14:30:00Z",
      "store_name": "Target",
      "store_location": "San Francisco, CA",
      "total_spent": 10.99,
      "points_earned": 50
    }
  ],
  "items": [
    {
      "item_id": 1,  # Generated
      "receipt_id": "R001",
      "barcode": "012345678901",
      "description": "Organic Milk",
      "quantity": 2,
      "unit_price": 3.50,
      "final_price": 7.00,
      "brand_id": "B001"
    },
    {
      "item_id": 2,
      "receipt_id": "R001",
      "barcode": "012345678902",
      "description": "Bread",
      "quantity": 1,
      "unit_price": 3.99,
      "final_price": 3.99,
      "brand_id": "B002"
    }
  ],
  "brands": [
    {
      "brand_id": "B001",
      "brand_name": "Organic Valley",
      "category": "Dairy"
    },
    {
      "brand_id": "B002",
      "brand_name": "Wonder Bread",
      "category": "Bakery"
    }
  ]
}

Time Limit: 90-120 minutes
Expected: Working ETL with validation, good code structure, documentation
"""

try:
    import importlib.util
    spec = importlib.util.spec_from_file_location("solution_module",
                                                   "02_json_to_relational_etl_solution.py")
    solution_module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(solution_module)
    load_json = solution_module.load_json
    transform_receipt = solution_module.transform_receipt
    validate_data = solution_module.validate_data
except Exception as e:
    print(f"❌ Error importing solution: {e}")
    exit(1)

import json
import tempfile
import os

def test_json_to_relational():
    print("Testing JSON to Relational ETL...")
    print()

    # Test 1: Basic single receipt transformation
    print("Test 1: Single receipt transformation")
    receipt1 = {
        "receipt_id": "R001",
        "scan_date": "2025-01-05T14:30:00Z",
        "store": {"name": "Target", "location": "San Francisco, CA"},
        "user": {"user_id": "U123", "email": "user@example.com"},
        "items": [
            {
                "barcode": "012345678901",
                "description": "Milk",
                "quantity": 2,
                "unit_price": 3.50,
                "final_price": 7.00,
                "brand": {"brand_id": "B001", "name": "Organic Valley", "category": "Dairy"}
            }
        ],
        "total_spent": 7.00,
        "points_earned": 20
    }

    result1 = transform_receipt(receipt1)
    assert "receipts" in result1, "Test 1a failed: missing receipts table"
    assert "items" in result1, "Test 1b failed: missing items table"
    assert "brands" in result1, "Test 1c failed: missing brands table"
    assert len(result1["receipts"]) == 1, "Test 1d failed"
    assert result1["receipts"][0]["receipt_id"] == "R001", "Test 1e failed"
    assert len(result1["items"]) == 1, "Test 1f failed"
    assert len(result1["brands"]) == 1, "Test 1g failed"
    print("✓ Test 1 passed")
    print()

    # Test 2: Multiple items
    print("Test 2: Multiple items")
    receipt2 = {
        "receipt_id": "R002",
        "scan_date": "2025-01-06T10:00:00Z",
        "store": {"name": "Walmart", "location": "New York, NY"},
        "user": {"user_id": "U456"},
        "items": [
            {
                "barcode": "111",
                "description": "Item 1",
                "quantity": 1,
                "unit_price": 5.00,
                "final_price": 5.00,
                "brand": {"brand_id": "B001", "name": "Brand A", "category": "Cat A"}
            },
            {
                "barcode": "222",
                "description": "Item 2",
                "quantity": 2,
                "unit_price": 3.00,
                "final_price": 6.00,
                "brand": {"brand_id": "B002", "name": "Brand B", "category": "Cat B"}
            }
        ],
        "total_spent": 11.00,
        "points_earned": 30
    }

    result2 = transform_receipt(receipt2)
    assert len(result2["items"]) == 2, "Test 2a failed: should have 2 items"
    assert len(result2["brands"]) == 2, "Test 2b failed: should have 2 brands"
    print("✓ Test 2 passed")
    print()

    # Test 3: Missing optional fields
    print("Test 3: Missing optional fields")
    receipt3 = {
        "receipt_id": "R003",
        "scan_date": "2025-01-07T12:00:00Z",
        "store": {"name": "CVS"},  # Missing location
        "user": {"user_id": "U789"},
        "items": [
            {
                "barcode": "333",
                "description": "Item 3",
                "quantity": 1,
                "unit_price": 10.00,
                "final_price": 10.00,
                # Missing brand
            }
        ],
        "total_spent": 10.00
        # Missing points_earned
    }

    result3 = transform_receipt(receipt3)
    # Should handle missing fields gracefully
    assert result3["receipts"][0]["receipt_id"] == "R003", "Test 3 failed"
    print("✓ Test 3 passed")
    print()

    # Test 4: Data validation
    print("Test 4: Data validation")
    valid_data = {
        "receipts": [{"receipt_id": "R001", "user_id": "U123"}],
        "items": [{"item_id": 1, "receipt_id": "R001"}],
        "brands": [{"brand_id": "B001", "brand_name": "Brand"}]
    }
    is_valid, errors = validate_data(valid_data)
    assert is_valid or len(errors) == 0, "Test 4a failed: should be valid"

    invalid_data = {
        "receipts": [],  # Empty receipts
        "items": [{"item_id": 1}],  # Missing receipt_id
    }
    is_valid2, errors2 = validate_data(invalid_data)
    assert not is_valid2 or len(errors2) > 0, "Test 4b failed: should be invalid"
    print("✓ Test 4 passed")
    print()

    # Test 5: Load from JSON file
    print("Test 5: Load from JSON file")
    sample_receipts = [receipt1, receipt2]

    # Create temporary JSON file
    with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as f:
        json.dump(sample_receipts, f)
        temp_file = f.name

    try:
        loaded = load_json(temp_file)
        assert len(loaded) == 2, "Test 5a failed"
        assert loaded[0]["receipt_id"] == "R001", "Test 5b failed"
        assert loaded[1]["receipt_id"] == "R002", "Test 5c failed"
        print("✓ Test 5 passed")
    finally:
        os.unlink(temp_file)
    print()

    # Test 6: Duplicate brand handling
    print("Test 6: Duplicate brand handling")
    receipt6 = {
        "receipt_id": "R006",
        "scan_date": "2025-01-08T12:00:00Z",
        "store": {"name": "Store"},
        "user": {"user_id": "U999"},
        "items": [
            {
                "barcode": "A",
                "description": "Item A",
                "quantity": 1,
                "unit_price": 1.00,
                "final_price": 1.00,
                "brand": {"brand_id": "B001", "name": "Same Brand", "category": "Cat"}
            },
            {
                "barcode": "B",
                "description": "Item B",
                "quantity": 1,
                "unit_price": 1.00,
                "final_price": 1.00,
                "brand": {"brand_id": "B001", "name": "Same Brand", "category": "Cat"}  # Duplicate
            }
        ],
        "total_spent": 2.00,
        "points_earned": 10
    }

    result6 = transform_receipt(receipt6)
    # Should deduplicate brands
    assert len(result6["brands"]) == 1, f"Test 6 failed: should deduplicate brands, got {len(result6['brands'])}"
    print("✓ Test 6 passed")
    print()

    print("All tests passed! ✓")
    print()
    print("Next Steps:")
    print("1. Review your code for edge cases")
    print("2. Add error handling for malformed JSON")
    print("3. Consider adding logging")
    print("4. Write documentation for your schema design")
    print("5. Consider performance optimizations for large datasets")

if __name__ == "__main__":
    test_json_to_relational()
