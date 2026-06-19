# Day 54 - URL Helper
import re

def count_urls(text):
    return len(extract_urls(text))

def extract_urls(text):
    pattern = r'https?://[^\s<>"{}|\\^`\[\]]+'
    return re.findall(pattern, text)

def quick_demo():
    text = "Visit https://example.com and http://test.org/page"
    urls = extract_urls(text)
    print("Demo text:", text)
    print("Found URLs:", urls)
    print("Count:", count_urls(text))

if __name__ == "__main__":
    quick_demo()