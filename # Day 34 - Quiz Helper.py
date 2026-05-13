# Day 34 - Quiz Helper
from day34 import Quiz

def timed_quiz():
    print("Timed quiz disabled in simple helper — using normal quiz.")
    Quiz().run()

def sample_questions():
    return [
        {"q":"Largest planet?", "choices":["Earth","Mars","Jupiter","Venus"], "a":2},
        {"q":"HTML stands for?", "choices":["Hyperlinks...","HyperText Markup Language","Home Tool Markup","None"], "a":1}
    ]

if __name__ == "__main__":
    print("1. Play default quiz\n2. Play sample questions")
    c = input("Choice: ")
    if c == "2":
        Quiz(sample_questions()).run()
    else:
        Quiz().run()