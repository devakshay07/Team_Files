import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from src.data.cleaner import remove_pii

def test_pii():
    cases = [
        ("Contact John at john.doe@oil-company.com for info.", "Contact John at [EMAIL_REDACTED] for info."),
        ("Phone: +1 (555) 123-4567.", "Phone: [PHONE_REDACTED]."),
        ("Call me at 9876543210 immediately.", "Call me at [PHONE_REDACTED] immediately."), # Indian format
        ("Employee ID 123-45-6789 was involved.", "Employee ID [ID_REDACTED] was involved."),
        ("Send to user123@sub.domain.co.uk please.", "Send to [EMAIL_REDACTED] please.")
    ]
    
    failures = 0
    for input_text, expected in cases:
        result = remove_pii(input_text)
        if result != expected:
            print(f"FAILED.\nInput: {input_text}\nExpected: {expected}\nGot: {result}")
            failures += 1
            
    if failures == 0:
        print("PII Redaction Tests Passed.")
    else:
        print(f"{failures} PII tests failed.")
        sys.exit(1)

if __name__ == "__main__":
    test_pii()
