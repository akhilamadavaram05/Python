# Day 43 - Test
import json

def test_json_files():
    with open("day43_data.json", "r") as f:
        data = json.load(f)
    assert "name" in data
    assert "skills" in data
    print("✅ JSON keys OK")
    print("Day 43 test ok")

test_json_files()