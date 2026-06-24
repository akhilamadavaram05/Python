# Day 59 - Test
from day59_helper import word_frequency, top_n_words

def test_frequency():
    text = "Python python data data data fun!"
    freq = word_frequency(text)
    assert freq["python"] == 2
    assert freq["data"] == 3
    assert freq["fun"] == 1
    print("✅ Frequency counts OK")

def test_top_words():
    text = "a a b c c c"
    top = top_n_words(text, 2)
    assert top[0] == ("c", 3)
    assert top[1] == ("a", 2)
    print("✅ Top words OK")
    print("Day 59 test ok")

test_frequency()
test_top_words()