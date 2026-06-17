# Day 52 - Email Helper
import re

def count_emails(text):
    return len(extract_emails(text))

def extract_emails(text):
    pattern = r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9.-]+'
    return re.findall(pattern, text)

def quick_demo():
    text = "Email alice@example.com and bob@test.co for help."
    emails = extract_emails(text)
    print("Demo text:", text)
    print("Found emails:", emails)
    print("Count:", count_emails(text))

if __name__ == "__main__":
    quick_demo()