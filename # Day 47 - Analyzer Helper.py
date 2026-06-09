# Day 47 - Analyzer Helper
from collections import Counter

def top_words(text, n=3):
    words = [w.lower() for w in text.split() if w]
    return Counter(words).most_common(n)

def analyze_file(filename, n=3):
    with open(filename, "r") as f:
        text = f.read()
    print(f"Analysis of {filename}:")
    print("Lines:", len(text.splitlines()))
    print("Words:", len([w for w in text.split() if w]))
    print("Chars:", len(text))
    print(f"Top {n} words:", top_words(text, n))

if __name__ == "__main__":
    analyze_file("day47_sample.txt")