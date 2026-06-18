# Day 53 - Phone Number Extractor (MAIN)
import re

def extract_phones(text):
    # Match patterns like 1234567890, 123-456-7890, (123) 456-7890, 123.456.7890
    pattern = r'\b\d{3}[-.\s]?\d{3}[-.\s]?\d{4}\b'
    return re.findall(pattern, text)

def main():
    print("Phone Number Extractor")
    sample = """
    Call 1234567890 or 123-456-7890 for support.
    Office: (999) 888-7777, Mobile: 999.888.7777
    Not valid: 12, 1234, abc-def-ghij
    """
    with open("day53_sample.txt", "w") as f:
        f.write(sample)
    print("Created day53_sample.txt")

    with open("day53_sample.txt", "r") as f:
        text = f.read()

    phones = extract_phones(text)
    print("Extracted phone numbers:")
    for p in phones:
        print(p)

if __name__ == "__main__":
    main()