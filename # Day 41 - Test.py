# Day 41 - Test
def test_quiz_structure():
    questions = [
        {"q": "2+2?", "choices": ["3", "4"], "a": 1},
        {"q": "Sun rises from?", "choices": ["West", "East"], "a": 1}
    ]
    assert len(questions) == 2
    print("✅ Question list structure OK")

    print("Day 41 test ok")

test_quiz_structure()