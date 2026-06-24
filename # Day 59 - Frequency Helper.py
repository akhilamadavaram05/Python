# Day 59 - Frequency Helper
from collections import Counter

def word_frequency(text):
    words = [w.lower().strip(".,!?;:\"'()[]{}") for w in text.split()]
    words = [w for w in words if w]
    return Counter(words)

def top_n_words(text, n=3):
    return word_frequency(text).most_common(n)

def quick_demo():
    text = "Python python data data data fun!"
    print("Demo text:", text)
    print("Frequency:", word_frequency(text))
    print("Top 3:", top_n_words(text, 3))

if __name__ == "__main__":
    quick_demo()