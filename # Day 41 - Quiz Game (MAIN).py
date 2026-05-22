# Day 41 - Quiz Game (MAIN)
def main():
    questions = [
        {"q": "Capital of India?", "choices": ["Mumbai", "Kolkata", "New Delhi", "Chennai"], "a": 2},
        {"q": "2 + 2 = ?", "choices": ["3", "4", "5", "6"], "a": 1},
        {"q": "Python creator?", "choices": ["Guido van Rossum", "Dennis Ritchie", "Bjarne Stroustrup"], "a": 0}
    ]

    score = 0
    for q in questions:
        print(q["q"])
        for i, ch in enumerate(q["choices"], 1):
            print(f"{i}. {ch}")
        try:
            ans = int(input("Your answer: ")) - 1
            if ans == q["a"]:
                print("Correct!")
                score += 1
            else:
                print("Wrong! Correct:", q["choices"][q["a"]])
        except ValueError:
            print("Wrong!")

    print(f"Score: {score}/{len(questions)}")

if __name__ == "__main__":
    main()