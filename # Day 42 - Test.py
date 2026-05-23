# Day 42 - Test
import csv

def test_csv():
    with open("day42_data.csv", "r") as f:
        reader = csv.reader(f)
        rows = list(reader)
    assert len(rows) == 4  # header + 3 data rows
    print("✅ CSV rows OK")
    print("Day 42 test ok")

test_csv()