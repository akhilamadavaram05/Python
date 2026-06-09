# Day 47 - Test
from day47 import count_words, count_lines, count_chars

def test_word_counter():
    text = "Hello world\nThis is line 2"
    assert count_words(text) == 6
    assert count_lines(text) == 2
    assert count_chars(text) == len(text)
    print("✅ Word counter tests OK")
    print("Day 47 test ok")

test_word_counter()