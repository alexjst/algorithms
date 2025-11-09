#!/usr/bin/env python3
"""
Problem 4: Data Quality Monitoring

DataHub monitors data quality metrics over time to detect anomalies.
Implement a system to track metrics and detect significant changes.

Requirements:
- Track metrics over time (row count, null percentage, distinct values)
- Calculate rolling statistics (mean, standard deviation)
- Detect anomalies using Z-score (values beyond threshold)
- Return alerts for anomalous metrics

Example:
    monitor = DataQualityMonitor(window_size=5, threshold=2.0)

    # Normal metrics
    monitor.add_metric("table1", "row_count", 1000)
    monitor.add_metric("table1", "row_count", 1050)
    monitor.add_metric("table1", "row_count", 980)
    monitor.add_metric("table1", "row_count", 1020)
    monitor.add_metric("table1", "row_count", 1010)

    # Anomalous metric
    result = monitor.add_metric("table1", "row_count", 5000)
    # Returns: {"is_anomaly": True, "z_score": 3.5, ...}

Time Complexity: O(w) where w is window size
Space Complexity: O(t × m × w) where t is tables, m is metrics, w is window
"""

# Import the solution
try:
    import importlib.util
    spec = importlib.util.spec_from_file_location(
        "solution_module",
        "04_data_quality_monitoring_solution.py"
    )
    solution_module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(solution_module)
    DataQualityMonitor = solution_module.DataQualityMonitor
except Exception as e:
    print(f"❌ Error importing solution: {e}")
    print(f"   Make sure 04_data_quality_monitoring_solution.py exists.")
    exit(1)

def test_data_quality_monitoring():
    """Test the data quality monitoring implementation."""

    print("Testing Data Quality Monitoring...")
    print()

    # Test 1: No anomaly with stable metrics
    print("Test 1: No anomaly with stable metrics")
    monitor1 = DataQualityMonitor(window_size=3, threshold=2.0)
    monitor1.add_metric("table1", "row_count", 100)
    monitor1.add_metric("table1", "row_count", 105)
    result1 = monitor1.add_metric("table1", "row_count", 98)
    assert result1["is_anomaly"] == False, f"Test 1 failed: should not detect anomaly in stable data"
    print("✓ Test 1 passed: No false positive on stable metrics")
    print()

    # Test 2: Detect anomaly with spike
    print("Test 2: Detect anomaly with spike")
    monitor2 = DataQualityMonitor(window_size=5, threshold=2.0)
    monitor2.add_metric("table2", "row_count", 1000)
    monitor2.add_metric("table2", "row_count", 1050)
    monitor2.add_metric("table2", "row_count", 980)
    monitor2.add_metric("table2", "row_count", 1020)
    monitor2.add_metric("table2", "row_count", 1010)
    result2 = monitor2.add_metric("table2", "row_count", 5000)
    assert result2["is_anomaly"] == True, f"Test 2 failed: should detect anomaly with spike"
    assert result2["z_score"] > 2.0, f"Test 2 failed: z_score should be > 2.0, got {result2.get('z_score', 0)}"
    print("✓ Test 2 passed: Anomaly detected with spike")
    print()

    # Test 3: Detect anomaly with drop
    print("Test 3: Detect anomaly with drop")
    monitor3 = DataQualityMonitor(window_size=4, threshold=2.0)
    monitor3.add_metric("table3", "null_pct", 0.05)
    monitor3.add_metric("table3", "null_pct", 0.06)
    monitor3.add_metric("table3", "null_pct", 0.04)
    monitor3.add_metric("table3", "null_pct", 0.05)
    result3 = monitor3.add_metric("table3", "null_pct", 0.50)
    assert result3["is_anomaly"] == True, f"Test 3 failed: should detect anomaly with drop"
    print("✓ Test 3 passed: Anomaly detected with drop")
    print()

    # Test 4: Different metrics for same table
    print("Test 4: Different metrics for same table")
    monitor4 = DataQualityMonitor(window_size=3, threshold=2.0)
    monitor4.add_metric("table4", "row_count", 1000)
    monitor4.add_metric("table4", "null_pct", 0.05)
    result4a = monitor4.add_metric("table4", "row_count", 1010)
    result4b = monitor4.add_metric("table4", "null_pct", 0.06)
    assert result4a["is_anomaly"] == False, "Test 4a failed: row_count should be stable"
    assert result4b["is_anomaly"] == False, "Test 4b failed: null_pct should be stable"
    print("✓ Test 4 passed: Different metrics tracked independently")
    print()

    # Test 5: Insufficient data for detection
    print("Test 5: Insufficient data (window not full)")
    monitor5 = DataQualityMonitor(window_size=5, threshold=2.0)
    result5 = monitor5.add_metric("table5", "row_count", 1000)
    assert result5["is_anomaly"] == False, "Test 5 failed: should not detect anomaly with insufficient data"
    print("✓ Test 5 passed: Insufficient data handled gracefully")
    print()

    print("All tests passed! ✓")

if __name__ == "__main__":
    test_data_quality_monitoring()
