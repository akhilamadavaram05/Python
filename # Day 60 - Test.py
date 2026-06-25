# Day 60 - Test
from day60_helper import seed_sample, load_notes, search_notes

def test_search():
    seed_sample()
    notes = load_notes()
    results = search_notes(notes, "python")
    assert len(results) == 1
    assert results[0]["title"] == "Python"
    print("✅ Search OK")
    print("Day 60 test ok")

test_search()