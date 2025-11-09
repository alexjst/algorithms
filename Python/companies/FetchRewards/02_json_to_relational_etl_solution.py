#!/usr/bin/env python3
"""Solution for Problem 2: JSON to Relational ETL"""

import json
from typing import List, Dict, Tuple, Any

def load_json(filepath: str) -> List[Dict]:
    """
    Load JSON data from file.

    TODO: Implement JSON file loading
    Hints:
    1. Open file and use json.load()
    2. Handle file not found errors
    3. Handle malformed JSON
    4. Return list of receipt dictionaries

    Example:
    try:
        with open(filepath, 'r') as f:
            data = json.load(f)
        return data if isinstance(data, list) else [data]
    except FileNotFoundError:
        print(f"Error: File {filepath} not found")
        return []
    except json.JSONDecodeError as e:
        print(f"Error: Invalid JSON - {e}")
        return []

    Args:
        filepath: Path to JSON file

    Returns:
        List of receipt dictionaries
    """
    pass

def transform_receipt(receipt_json: Dict) -> Dict[str, List[Dict]]:
    """
    Transform single receipt JSON to relational format.

    TODO: Implement transformation
    Hints:
    1. Extract receipt-level data for receipts table
    2. Extract item-level data for items table
    3. Extract brand data for brands table (deduplicate)
    4. Handle missing fields with .get() and default values
    5. Generate item_id for items (can use enumerate)

    Schema Design:
    receipts: receipt_id, user_id, scan_date, store_name, store_location,
              total_spent, points_earned

    items: item_id, receipt_id, barcode, description, quantity,
           unit_price, final_price, brand_id

    brands: brand_id, brand_name, category

    Example:
    result = {
        "receipts": [],
        "items": [],
        "brands": []
    }

    # Extract receipt data
    receipt_data = {
        "receipt_id": receipt_json.get("receipt_id"),
        "user_id": receipt_json.get("user", {}).get("user_id"),
        "scan_date": receipt_json.get("scan_date"),
        "store_name": receipt_json.get("store", {}).get("name"),
        "store_location": receipt_json.get("store", {}).get("location"),
        "total_spent": receipt_json.get("total_spent"),
        "points_earned": receipt_json.get("points_earned", 0)
    }
    result["receipts"].append(receipt_data)

    # Extract items and brands
    brands_seen = {}  # Track brands to avoid duplicates

    for idx, item in enumerate(receipt_json.get("items", [])):
        item_data = {
            "item_id": idx + 1,
            "receipt_id": receipt_json.get("receipt_id"),
            "barcode": item.get("barcode"),
            "description": item.get("description"),
            "quantity": item.get("quantity"),
            "unit_price": item.get("unit_price"),
            "final_price": item.get("final_price"),
            "brand_id": item.get("brand", {}).get("brand_id")
        }
        result["items"].append(item_data)

        # Extract brand if present
        brand = item.get("brand")
        if brand and brand.get("brand_id"):
            brand_id = brand["brand_id"]
            if brand_id not in brands_seen:
                brand_data = {
                    "brand_id": brand_id,
                    "brand_name": brand.get("name"),
                    "category": brand.get("category")
                }
                result["brands"].append(brand_data)
                brands_seen[brand_id] = True

    return result

    Args:
        receipt_json: Receipt data as dictionary

    Returns:
        Dictionary with keys: receipts, items, brands
        Each value is a list of dictionaries representing rows
    """
    pass

def validate_data(data: Dict[str, List[Dict]]) -> Tuple[bool, List[str]]:
    """
    Validate transformed data.

    TODO: Implement validation
    Hints:
    1. Check required tables exist (receipts, items, brands)
    2. Check receipts table not empty
    3. Check all items have receipt_id
    4. Check all brands have brand_id
    5. Check data types are correct
    6. Check referential integrity (items.receipt_id exists in receipts)

    Example:
    errors = []

    # Check required tables
    required_tables = ["receipts", "items", "brands"]
    for table in required_tables:
        if table not in data:
            errors.append(f"Missing required table: {table}")

    # Check receipts not empty
    if "receipts" in data and len(data["receipts"]) == 0:
        errors.append("Receipts table is empty")

    # Check items have receipt_id
    if "items" in data:
        for idx, item in enumerate(data["items"]):
            if "receipt_id" not in item or item["receipt_id"] is None:
                errors.append(f"Item at index {idx} missing receipt_id")

    # Check brands have brand_id
    if "brands" in data:
        for idx, brand in enumerate(data["brands"]):
            if "brand_id" not in brand or brand["brand_id"] is None:
                errors.append(f"Brand at index {idx} missing brand_id")

    # Check referential integrity
    if "receipts" in data and "items" in data:
        receipt_ids = {r["receipt_id"] for r in data["receipts"]}
        for item in data["items"]:
            if item.get("receipt_id") not in receipt_ids:
                errors.append(f"Item references non-existent receipt: {item.get('receipt_id')}")

    return len(errors) == 0, errors

    Args:
        data: Transformed data dictionary

    Returns:
        Tuple of (is_valid, list_of_error_messages)
    """
    pass
