#!/usr/bin/env python3
"""
Solution for Problem 4: Data Quality Monitoring

TODO: Implement the DataQualityMonitor class below.
"""

from typing import Dict
from collections import deque
import statistics

class DataQualityMonitor:
    """
    Monitor data quality metrics and detect anomalies using statistical methods.

    Args:
        window_size: Number of historical values to consider for statistics
        threshold: Z-score threshold for anomaly detection (typically 2.0 or 3.0)
    """

    def __init__(self, window_size: int, threshold: float):
        """Initialize the monitor."""
        # TODO: Implement initialization
        # You'll need to store:
        # - Window size and threshold
        # - Historical metrics for each (table, metric_name) pair
        pass

    def add_metric(self, table_name: str, metric_name: str, value: float) -> Dict:
        """
        Add a metric value and check for anomalies.

        Args:
            table_name: Name of the table
            metric_name: Name of the metric (e.g., "row_count", "null_pct")
            value: Metric value

        Returns:
            Dictionary with:
            - "is_anomaly": bool
            - "z_score": float (if enough data)
            - "mean": float (if enough data)
            - "std_dev": float (if enough data)
        """
        # TODO: Implement anomaly detection
        # Hints:
        # 1. Store the metric value in the rolling window
        # 2. If window has enough data (>= 2 values):
        #    a. Calculate mean and standard deviation of previous values
        #    b. Calculate Z-score: (value - mean) / std_dev
        #    c. If |z_score| > threshold, it's an anomaly
        # 3. Add current value to window (maintain window_size limit)
        # 4. Return result dictionary
        pass
