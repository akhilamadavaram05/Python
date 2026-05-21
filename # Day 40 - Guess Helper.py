# Day 40 - Guess Helper
import random

def play_round(ans):
    print("Playing a round with answer =", ans)
    for i in range(1, 101):
        if i == ans:
            print("Found at guess", i)
            break

def demo():
    ans = random.randint(1, 100)
    print("Answer is", ans)
    play_round(ans)

if __name__ == "__main__":
    demo()