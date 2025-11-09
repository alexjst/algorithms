#!/usr/bin/env python3
"""
Problem 14: Object Manipulation (Product Catalog)

Build a product catalog system with filtering operations.

Implement ProductCatalog class with:
- add_product(product): Add product to catalog
- get_product(product_id): Get product by ID
- filter_by_category(category): Return products in category
- filter_by_price_range(min_price, max_price): Return products in price range
- filter_by_attributes(attr_dict): Return products matching attributes
- search_by_name(query): Case-insensitive name search
- get_available_products(): Return in-stock products

Product structure:
{
    'id': 'p1',
    'name': 'Blue T-Shirt',
    'price': 19.99,
    'category': 'clothing',
    'attributes': {'size': 'M', 'color': 'blue'},
    'in_stock': True
}

Constraints:
    - 1 <= products <= 10^4
    - Product IDs are unique
    - 0 <= price <= 10^6 - TEST SCAFFOLDING (DO NOT EDIT)

================================================================================
INSTRUCTIONS:
- Implement your solution in: 14_object_manipulation_solution.py
- Run this file to test: python 14_object_manipulation.py
- To reset and practice again: just delete/reset the solution file
================================================================================
"""

# Import the solution
try:
    import importlib.util
    spec = importlib.util.spec_from_file_location(
        "solution_module",
        "14_object_manipulation_solution.py"
    )
    solution_module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(solution_module)
    ProductCatalog = solution_module.ProductCatalog
except Exception as e:
    print(f"❌ Error importing solution: {e}")
    print(f"   Make sure 14_object_manipulation_solution.py exists.")
    exit(1)

def run_tests():
    """Run test cases for ProductCatalog."""

    catalog = ProductCatalog()

    # Test Case 1: Add and retrieve
    p1 = {
        'id': 'p1', 'name': 'Blue Shirt', 'price': 20,
        'category': 'clothing', 'in_stock': True,
        'attributes': {'size': 'M', 'color': 'blue'}
    }
    catalog.add_product(p1)
    result1 = catalog.get_product('p1')
    assert result1 == p1, "Test 1 failed: product retrieval"
    print("✓ Test 1 passed: Add and retrieve product")

    # Test Case 2: Filter by category
    p2 = {
        'id': 'p2', 'name': 'Pants', 'price': 30,
        'category': 'clothing', 'in_stock': True,
        'attributes': {}
    }
    catalog.add_product(p2)
    clothing = catalog.filter_by_category('clothing')
    assert len(clothing) == 2, f"Test 2 failed: expected 2 items, got {len(clothing)}"
    print("✓ Test 2 passed: Filter by category")

    # Test Case 3: Price range filter
    results = catalog.filter_by_price_range(15, 25)
    assert len(results) == 1, f"Test 3 failed: expected 1 item, got {len(results)}"
    print("✓ Test 3 passed: Price range filter")

    # Test Case 4: Attribute filter
    results = catalog.filter_by_attributes({'color': 'blue'})
    assert len(results) == 1, f"Test 4 failed: expected 1 item, got {len(results)}"
    print("✓ Test 4 passed: Attribute filter")

    # Test Case 5: Search by name
    results = catalog.search_by_name('shirt')
    assert len(results) == 1, f"Test 5 failed: expected 1 item, got {len(results)}"
    print("✓ Test 5 passed: Name search")

    # Test Case 6: Available products
    p3 = {
        'id': 'p3', 'name': 'Hat', 'price': 15,
        'category': 'accessories', 'in_stock': False,
        'attributes': {}
    }
    catalog.add_product(p3)
    available = catalog.get_available_products()
    assert len(available) == 2, f"Test 6 failed: expected 2 items, got {len(available)}"
    print("✓ Test 6 passed: Available products filter")

    print("\n" + "="*50)
    print("All basic tests passed! ✓")
    print("="*50)



def run_custom_tests():
    """Add your own custom test cases here."""
    print("\nRunning custom tests...")

    # Add your custom test cases here

    print("No custom tests defined yet.")



if __name__ == "__main__":
    print("Testing Product Catalog Solution")
    print("="*50 + "\n")

    try:
        run_tests()
        run_custom_tests()
    except AssertionError as e:
        print(f"\n❌ Test failed: {e}")
    except Exception as e:
        print(f"\n❌ Error: {e}")
