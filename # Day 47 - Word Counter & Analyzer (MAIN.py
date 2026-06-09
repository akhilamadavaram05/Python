# Day 47 - Word Counter & Analyzer (MAIN)

def count_words(text):
    # Split by whitespace and filter empty strings
    return len([w for w in text.split() if w])

def count_lines(text):
    return len(text.splitlines())

def count_chars(text):
    return len(text)

def main():
    print("Text Word Counter & Analyzer")
    # Create a sample text file
    sample = "Hello world\nThis is line 2\nLine 3 with 5 words"
    with open("day47_sample.txt", "w") as f:
        f.write(sample)
    print("Created day47_sample.txt")

    with open("day47_sample.txt", "r") as f:
        text = f.read()

    words = count_words(text)
    lines = count_lines(text)
    chars = count_chars(text)

    print(f"Lines: {lines}")
    print(f"Words: {words}")
    print(f"Characters: {chars}")

if __name__ == "__main__":
    main()