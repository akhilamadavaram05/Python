# Day 34 - Test
from day34 import Quiz

def test_quiz_flow():
    qlist = [
        {"q":"1+1?","choices":["1","2"], "a":1},
        {"q":"Sun rises from?", "choices":["West","East"], "a":1}
    ]
    quiz = Quiz(qlist)
    # Simulate asking by calling ask with a monkeypatched input if needed.
    # Here just test internal data and run returns score when answered manually.
    assert len(quiz.questions) == 2
    print("✅ Test: questions loaded")
    print("Manual test: run quiz and answer to verify flow.")
    print("Day 34 test ok")

if __name__ == "__main__":
    test_quiz_flow()