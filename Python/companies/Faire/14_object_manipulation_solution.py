#!/usr/bin/env python3
"""
Solution for Problem 14: Object Manipulation (Product Catalog)

TODO: Implement the ProductCatalog class below.
"""

from typing import List, Dict, Optional


class ProductCatalog:
    def __init__(self):
        """Initialize empty product catalog."""
        # TODO: Initialize data structures
        pass

    def add_product(self, product: Dict) -> None:
        """Add a product to catalog."""
        # TODO: Implement
        pass

    def get_product(self, product_id: str) -> Optional[Dict]:
        """Get product by ID."""
        # TODO: Implement
        return None

    def filter_by_category(self, category: str) -> List[Dict]:
        """Return all products in a category."""
        # TODO: Implement
        return []

    def filter_by_price_range(self, min_price: float, max_price: float) -> List[Dict]:
        """Return products within price range."""
        # TODO: Implement
        return []

    def filter_by_attributes(self, attr_dict: Dict[str, str]) -> List[Dict]:
        """Return products matching all given attributes."""
        # TODO: Implement
        return []

    def search_by_name(self, query: str) -> List[Dict]:
        """Return products with name containing query (case-insensitive)."""
        # TODO: Implement
        return []

    def get_available_products(self) -> List[Dict]:
        """Return all in-stock products."""
        # TODO: Implement
        return []
