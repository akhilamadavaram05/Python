# Day 59 - Frequency Counter (MAIN)
from collections import Counter

def word_frequency(text):
    words = [w.lower().strip(".,!?;:\"'()[]{}") for w in text.split()]
    words = [w for w in words if w]
    return Counter(words)

def main():
    print("Word Frequency Counter")
    sample = """
    Python is fun. Python is powerful!
    Fun projects help learn Python better.
    """
    with open("day59_sample.txt", "w") as f:
        f.write(sample)
    print("Created day59_sample.txt")

    with open("day59_sample.txt", "r") as f:
        text = f.read()

    freq = word_frequency(text)
    print("Word frequencies:")
    for word, count in freq.most_common():
        print(f"{word}: {count}")

if __name__ == "__main__":
    main()