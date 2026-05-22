# Day 41 - Quiz Helper
from day41 import main

def demo_quiz():
    print("Running a demo quiz directly.")
    main()

def sample_questions():
    return [
        {"q": "Which planet is largest?", "choices": ["Earth", "Mars", "Jupiter", "Venus"], "a": 2},
        {"q": "HTML stands for?", "choices": ["Hyperlinks", "HyperText Markup Language", "Home Tool Markup"], "a": 1}
    ]

if __name__ == "__main__":
    print("1. Play default quiz\n2. Play sample questions")
    c = input("Choice: ")
    if c == "2":
        print("Switching to sample questions not implemented in minimal helper.")
    demo_quiz()