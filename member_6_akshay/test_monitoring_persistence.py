import sys
import os
import unittest
import json

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from src.analytics.monitoring import DriftMonitor

class TestMonitoringPersistence(unittest.TestCase):
    def setUp(self):
        self.test_log = "test_monitoring.jsonl"
        if os.path.exists(self.test_log):
            os.remove(self.test_log)
            
    def tearDown(self):
        if os.path.exists(self.test_log):
            os.remove(self.test_log)

    def test_persistence_survives_restart(self):
        # Instance 1 logs predictions
        monitor1 = DriftMonitor(log_path=self.test_log)
        monitor1.log_prediction("HIGH", True)
        monitor1.log_prediction("LOW", False)
        
        self.assertEqual(monitor1.total_predictions, 2)
        self.assertEqual(monitor1.human_reviews_requested, 1)
        
        # Instance 2 (simulate restart) should load from file
        monitor2 = DriftMonitor(log_path=self.test_log)
        
        self.assertEqual(monitor2.total_predictions, 2)
        self.assertEqual(monitor2.human_reviews_requested, 1)
        self.assertEqual(monitor2.risk_distribution["HIGH"], 1)
        self.assertEqual(monitor2.risk_distribution["LOW"], 1)

if __name__ == "__main__":
    unittest.main()
