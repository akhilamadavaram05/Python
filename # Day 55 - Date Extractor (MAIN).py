# Day 55 - Date Extractor (MAIN)
import re

def extract_dates(text):
    # Match YYYY-MM-DD, DD/MM/YYYY, MM/DD/YYYY formats
    patterns = [
        r'\d{4}-\d{2}-\d{2}',       # YYYY-MM-DD
        r'\d{2}/\d{2}/\d{4}',       # DD/MM/YYYY or MM/DD/YYYY
        r'\d{2}-\d{2}-\d{4}',       # DD-MM-YYYY or MM-DD-YYYY
    ]
    dates = []
    for pattern in patterns:
        dates.extend(re.findall(pattern, text))
    return dates

def main():
    print("Date Extractor")
    sample = """
    Meeting on 2024-01-15 and 2025-06-20.
    Birthday: 15/01/2024, Event: 20-06-2025.
    Not valid: 2024/1/15, 15-1-2024, 2024-1-1
    """
    with open("day55_sample.txt", "w") as f:
        f.write(sample)
    print("Created day55_sample.txt")

    with open("day55_sample.txt", "r") as f:
        text = f.read()

    dates = extract_dates(text)
    print("Extracted dates:")
    for d in dates:
        print(d)

if __name__ == "__main__":
    main()