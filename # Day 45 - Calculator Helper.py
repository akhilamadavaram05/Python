# Day 45 - Calculator Helper
def quick_demo():
    print("Quick demo:")
    print("2 + 3 =", add(2, 3))
    print("5 - 2 =", sub(5, 2))
    print("4 * 3 =", mul(4, 3))
    print("8 / 2 =", div(8, 2))

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if b == 0:
        return "Error"
    return a / b

if __name__ == "__main__":
    quick_demo()