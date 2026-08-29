import sys
import os
import unittest

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from src.data.cleaner import remove_pii

class TestPIIRedaction(unittest.TestCase):
    def test_phone_numbers(self):
        cases = [
            ("(555) 123-4567", "[PHONE_REDACTED]"),
            ("555-123-4567", "[PHONE_REDACTED]"),
            ("5551234567", "[PHONE_REDACTED]"),
            ("+1 555-123-4567", "[PHONE_REDACTED]"),
            ("Call me at (555) 123-4567.", "Call me at [PHONE_REDACTED].")
        ]
        for original, expected in cases:
            self.assertEqual(remove_pii(original), expected)

    def test_id_numbers(self):
        cases = [
            ("123456789012", "[PHONE_REDACTED]"), # 12-digit matched by flat sequence
            ("ID is 123-45-6789.", "ID is [ID_REDACTED].")
        ]
        for original, expected in cases:
            self.assertEqual(remove_pii(original), expected)
            
    def test_emails(self):
        self.assertEqual(remove_pii("john.doe@example.com"), "[EMAIL_REDACTED]")

    def test_safe_numbers_preserved(self):
        cases = [
            "Worker fell 20ft from scaffold.",
            "Pressure reached 100 psi.",
            "Panel was 230V.",
            "Incident happened in 2026.",
            "He was 5 feet away."
        ]
        for text in cases:
            self.assertEqual(remove_pii(text), text)

if __name__ == "__main__":
    unittest.main()
