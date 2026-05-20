# Day 39 - Calculator Helper
from day39 import add, subtract, multiply, divide

def batch_calc():
    ops = [
        (10, 5, "+"),
        (10, 5, "-"),
        (10, 5, "*"),
        (10, 5, "/")
    ]
    for n1, n2, op in ops:
        if op == "+": r = add(n1, n2)
        elif op == "-": r = subtract(n1, n2)
        elif op == "*": r = multiply(n1, n2)
        elif op == "/": r = divide(n1, n2)
        print(f"{n1} {op} {n2} = {r}")

if __name__ == "__main__":
    batch_calc()