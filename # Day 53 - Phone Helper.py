# Day 53 - Phone Helper
import re

def count_phones(text):
    return len(extract_phones(text))

def extract_phones(text):
    pattern = r'\b\d{3}[-.\s]?\d{3}[-.\s]?\d{4}\b'
    return re.findall(pattern, text)

def quick_demo():
    text = "Call 1234567890 or 123-456-7890 today."
    phones = extract_phones(text)
    print("Demo text:", text)
    print("Found phones:", phones)
    print("Count:", count_phones(text))

if __name__ == "__main__":
    quick_demo()