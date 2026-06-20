# Day 55 - Date Helper
import re

def count_dates(text):
    return len(extract_dates(text))

def extract_dates(text):
    patterns = [
        r'\d{4}-\d{2}-\d{2}',
        r'\d{2}/\d{2}/\d{4}',
        r'\d{2}-\d{2}-\d{4}',
    ]
    dates = []
    for pattern in patterns:
        dates.extend(re.findall(pattern, text))
    return dates

def quick_demo():
    text = "Meeting on 2024-01-15 and 15/01/2024"
    dates = extract_dates(text)
    print("Demo text:", text)
    print("Found dates:", dates)
    print("Count:", count_dates(text))

if __name__ == "__main__":
    quick_demo()