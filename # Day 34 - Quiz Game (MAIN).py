# Day 34 - Quiz Game (MAIN)
import random

class Quiz:
    def __init__(self, questions=None):
        # questions: list of dicts {"q": str, "choices": [..], "a": index}
        self.questions = questions or [
            {"q": "Capital of India?", "choices": ["Mumbai","Kolkata","New Delhi","Chennai"], "a": 2},
            {"q": "2 + 2 = ?", "choices": ["3","4","5","6"], "a": 1},
            {"q": "Python creator?", "choices": ["Guido van Rossum","Dennis Ritchie","Bjarne Stroustrup","James Gosling"], "a": 0}
        ]
        random.shuffle(self.questions)
    
    def ask(self, qobj):
        print("\n" + qobj["q"])
        for i, ch in enumerate(qobj["choices"], 1):
            print(f"  {i}. {ch}")
        while True:
            try:
                ans = int(input("Your answer (1-4): "))
                if 1 <= ans <= len(qobj["choices"]):
                    return ans-1
            except ValueError:
                pass
            print("Enter a number from 1 to", len(qobj["choices"]))
    
    def run(self):
        score = 0
        for q in self.questions:
            ans = self.ask(q)
            if ans == q["a"]:
                print("Correct!")
                score += 1
            else:
                print("Wrong! Correct:", q["choices"][q["a"]])
        print(f"\nFinal score: {score}/{len(self.questions)}")
        return score

if __name__ == "__main__":
    Quiz().run()