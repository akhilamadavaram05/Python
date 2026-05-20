# Day 39 - Calculator (MAIN)
def add(a, b):      return a + b
def subtract(a, b): return a - b
def multiply(a, b): return a * b
def divide(a, b):   return a / b if b != 0 else None

def main():
    print("Calculator (+, -, *, /)")
    n1 = float(input("First number: "))
    op = input("Operator (+-*/): ")
    n2 = float(input("Second number: "))

    result = None
    if op == "+": result = add(n1, n2)
    elif op == "-": result = subtract(n1, n2)
    elif op == "*": result = multiply(n1, n2)
    elif op == "/":
        result = divide(n1, n2)
        if result is None:
            print("Error: divide by zero")
            return
    else:
        print("Invalid operator")
        return

    print(f"Result: {result}")

if __name__ == "__main__":
    main()