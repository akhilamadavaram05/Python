# Day 55 - Test
from day55_helper import extract_dates, count_dates

def test_extract():
    text = "2024-01-15 and 15/01/2024"
    dates = extract_dates(text)
    assert len(dates) == 2
    assert "2024-01-15" in dates
    assert "15/01/2024" in dates
    print("✅ Date extraction OK")

def test_count():
    text = "No dates here"
    assert count_dates(text) == 0
    text = "2024-01-15"
    assert count_dates(text) == 1
    print("✅ Date count OK")
    print("Day 55 test ok")

test_extract()
test_count()