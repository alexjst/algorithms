#!/usr/bin/env python3
"""Solution for Problem 3: Data Quality Validation"""

from typing import List, Dict, Any, Set
from datetime import datetime
from collections import defaultdict

class DataQualityValidator:
    def __init__(self):
        """
        Initialize data quality validator.

        TODO: Implement initialization
        Hints:
        1. Store issues list
        2. Define severity levels
        3. Define required fields for each table

        Example:
        self.issues = []
        self.severity_weights = {
            "Critical": 1.0,
            "High": 0.75,
            "Medium": 0.5,
            "Low": 0.25
        }
        self.required_fields = {
            "receipts": ["receipt_id", "user_id", "scan_date", "total_spent"],
            "items": ["item_id", "receipt_id", "quantity", "final_price"],
            "brands": ["brand_id", "brand_name"]
        }
        """
        pass

    def check_missing_values(self, data: List[Dict], table_name: str) -> None:
        """
        Check for missing/NULL values in required fields.

        TODO: Implement missing value check
        Hints:
        1. Get required fields for this table
        2. For each record, check if required fields are present and not None
        3. Collect records with missing values
        4. Add to self.issues

        Example:
        required_fields = self.required_fields.get(table_name, [])
        missing_records = []

        for record in data:
            for field in required_fields:
                if field not in record or record[field] is None or record[field] == "":
                    missing_records.append({
                        "record": record,
                        "missing_field": field
                    })

        if missing_records:
            self.issues.append({
                "category": "Missing Values",
                "severity": "Critical",
                "table": table_name,
                "count": len(missing_records),
                "description": f"Required fields contain NULL/missing values",
                "samples": missing_records[:5],  # Show first 5
                "recommendation": "Add NOT NULL constraints and validation at ingestion"
            })

        Args:
            data: List of records
            table_name: Name of table being checked
        """
        pass

    def check_duplicates(self, data: List[Dict], table_name: str, key_fields: List[str]) -> None:
        """
        Check for duplicate records.

        TODO: Implement duplicate check
        Hints:
        1. Create set to track seen keys
        2. For each record, create key tuple from key_fields
        3. If key already seen, it's a duplicate
        4. Add to self.issues

        Example:
        seen_keys = set()
        duplicates = []

        for record in data:
            key = tuple(record.get(field) for field in key_fields)
            if key in seen_keys:
                duplicates.append(record)
            else:
                seen_keys.add(key)

        if duplicates:
            self.issues.append({
                "category": "Duplicate Records",
                "severity": "High",
                "table": table_name,
                "count": len(duplicates),
                "description": f"Duplicate records found based on {', '.join(key_fields)}",
                "samples": duplicates[:5],
                "recommendation": "Add unique constraints and deduplication logic"
            })

        Args:
            data: List of records
            table_name: Name of table
            key_fields: Fields that should be unique
        """
        pass

    def check_referential_integrity(self, items: List[Dict], receipts: List[Dict], brands: List[Dict]) -> None:
        """
        Check referential integrity between tables.

        TODO: Implement referential integrity check
        Hints:
        1. Create set of valid receipt_ids from receipts
        2. Create set of valid brand_ids from brands
        3. Check each item references valid receipt and brand
        4. Collect orphaned records
        5. Add to self.issues

        Example:
        receipt_ids = {r["receipt_id"] for r in receipts if "receipt_id" in r}
        brand_ids = {b["brand_id"] for b in brands if "brand_id" in b}

        orphaned_receipts = []
        invalid_brands = []

        for item in items:
            # Check receipt reference
            if item.get("receipt_id") not in receipt_ids:
                orphaned_receipts.append(item)

            # Check brand reference
            if item.get("brand_id") and item.get("brand_id") not in brand_ids:
                invalid_brands.append(item)

        if orphaned_receipts:
            self.issues.append({
                "category": "Referential Integrity",
                "severity": "Critical",
                "table": "items",
                "count": len(orphaned_receipts),
                "description": "Items reference non-existent receipts",
                "samples": orphaned_receipts[:5],
                "recommendation": "Add foreign key constraints and validate references"
            })

        if invalid_brands:
            self.issues.append({
                "category": "Referential Integrity",
                "severity": "Medium",
                "table": "items",
                "count": len(invalid_brands),
                "description": "Items reference non-existent brands",
                "samples": invalid_brands[:5],
                "recommendation": "Validate brand_id against brands table before insertion"
            })

        Args:
            items: List of item records
            receipts: List of receipt records
            brands: List of brand records
        """
        pass

    def check_business_logic(self, receipts: List[Dict], items: List[Dict]) -> None:
        """
        Check business logic rules.

        TODO: Implement business logic checks
        Hints:
        1. Check for negative values (total_spent, quantity, prices)
        2. Check for future dates
        3. Check reasonable ranges
        4. Verify calculations (total = sum of items)

        Example:
        # Check negative values in receipts
        negative_totals = [r for r in receipts if r.get("total_spent", 0) < 0]
        if negative_totals:
            self.issues.append({
                "category": "Business Logic Violation",
                "severity": "High",
                "table": "receipts",
                "count": len(negative_totals),
                "description": "Negative values in total_spent",
                "samples": negative_totals[:5],
                "recommendation": "Add validation to reject negative amounts"
            })

        # Check future dates
        today = datetime.now().date()
        future_dates = []
        for r in receipts:
            try:
                scan_date = datetime.fromisoformat(str(r.get("scan_date"))).date()
                if scan_date > today:
                    future_dates.append(r)
            except (ValueError, TypeError):
                pass

        if future_dates:
            self.issues.append({
                "category": "Business Logic Violation",
                "severity": "Medium",
                "table": "receipts",
                "count": len(future_dates),
                "description": "Scan dates in the future",
                "samples": future_dates[:5],
                "recommendation": "Add date validation to ensure dates are not in future"
            })

        # Check negative quantities in items
        negative_qty = [i for i in items if i.get("quantity", 0) < 0]
        if negative_qty:
            self.issues.append({
                "category": "Business Logic Violation",
                "severity": "High",
                "table": "items",
                "count": len(negative_qty),
                "description": "Negative quantities",
                "samples": negative_qty[:5],
                "recommendation": "Add validation to reject negative quantities"
            })

        Args:
            receipts: List of receipt records
            items: List of item records
        """
        pass

    def calculate_quality_score(self, total_records: int) -> float:
        """
        Calculate overall data quality score.

        TODO: Implement quality score calculation
        Hints:
        1. Weight issues by severity
        2. Calculate percentage of clean records
        3. Return score 0-100

        Example:
        if total_records == 0:
            return 100.0

        weighted_issues = 0
        for issue in self.issues:
            weight = self.severity_weights.get(issue["severity"], 0.5)
            weighted_issues += issue["count"] * weight

        # Score = (1 - weighted_issues/total) * 100
        score = max(0, (1 - weighted_issues / total_records) * 100)
        return round(score, 2)

        Args:
            total_records: Total number of records checked

        Returns:
            Quality score (0-100)
        """
        pass

    def generate_recommendations(self) -> List[str]:
        """
        Generate actionable recommendations.

        TODO: Implement recommendations
        Hints:
        1. Group issues by category
        2. Provide specific recommendations for each category
        3. Prioritize by severity

        Example:
        recommendations = set()

        for issue in self.issues:
            if issue.get("recommendation"):
                recommendations.add(issue["recommendation"])

        # Add general recommendations
        if any(i["category"] == "Missing Values" for i in self.issues):
            recommendations.add("Implement data validation at ingestion layer")

        return sorted(list(recommendations))

        Returns:
            List of recommendations
        """
        pass

    def validate_all(self, receipts: List[Dict], items: List[Dict], brands: List[Dict]) -> Dict:
        """
        Run all validation checks and generate report.

        TODO: Implement full validation
        Hints:
        1. Reset issues list
        2. Run all check methods
        3. Calculate quality score
        4. Generate recommendations
        5. Format report

        Example:
        self.issues = []

        # Run all checks
        self.check_missing_values(receipts, "receipts")
        self.check_missing_values(items, "items")
        self.check_missing_values(brands, "brands")
        self.check_duplicates(receipts, "receipts", ["receipt_id"])
        self.check_duplicates(items, "items", ["item_id"])
        self.check_duplicates(brands, "brands", ["brand_id"])
        self.check_referential_integrity(items, receipts, brands)
        self.check_business_logic(receipts, items)

        # Calculate metrics
        total_records = len(receipts) + len(items) + len(brands)
        quality_score = self.calculate_quality_score(total_records)
        recommendations = self.generate_recommendations()

        # Generate report
        report = {
            "summary": {
                "total_receipts": len(receipts),
                "total_items": len(items),
                "total_brands": len(brands),
                "issues_found": len(self.issues),
                "quality_score": quality_score
            },
            "issues": self.issues,
            "recommendations": recommendations
        }

        return report

        Args:
            receipts: List of receipt records
            items: List of item records
            brands: List of brand records

        Returns:
            Data quality report dictionary
        """
        pass
