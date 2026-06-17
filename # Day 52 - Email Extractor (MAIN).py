# Day 52 - Email Extractor (MAIN)
import re

def extract_emails(text):
    pattern = r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9.-]+'
    return re.findall(pattern, text)

def main():
    print("Email Extractor")
    # Create sample text
    sample = """
    Contact us at support@example.com or sales@company.co.
    For help write to help.me@test-domain.org.
    Not an email: abc@, @x.com, user@.com
    """
    with open("day52_sample.txt", "w") as f:
        f.write(sample)
    print("Created day52_sample.txt")

    with open("day52_sample.txt", "r") as f:
        text = f.read()

    emails = extract_emails(text)
    print("Extracted emails:")
    for e in emails:
        print(e)

if __name__ == "__main__":
    main()