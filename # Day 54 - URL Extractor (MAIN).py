# Day 54 - URL Extractor (MAIN)
import re

def extract_urls(text):
    pattern = r'https?://[^\s<>"{}|\\^`\[\]]+'
    return re.findall(pattern, text)

def main():
    print("URL Extractor")
    sample = """
    Check https://example.com and http://test.org/page for info.
    Visit https://github.com/user/repo today.
    Not valid: http://, https, example.com (no http)
    """
    with open("day54_sample.txt", "w") as f:
        f.write(sample)
    print("Created day54_sample.txt")

    with open("day54_sample.txt", "r") as f:
        text = f.read()

    urls = extract_urls(text)
    print("Extracted URLs:")
    for u in urls:
        print(u)

if __name__ == "__main__":
    main()