# Day 53 - Test
from day53_helper import extract_phones, count_phones

def test_extract():
    text = "Call 1234567890 and 123-456-7890"
    phones = extract_phones(text)
    assert len(phones) == 2
    assert "1234567890" in phones
    assert "123-456-7890" in phones
    print("✅ Phone extraction OK")

def test_count():
    text = "No phones here"
    assert count_phones(text) == 0
    text = "1234567890"
    assert count_phones(text) == 1
    print("✅ Phone count OK")
    print("Day 53 test ok")

test_extract()
test_count()