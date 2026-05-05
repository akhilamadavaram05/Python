# Calculator Helper - Interactive!
def calculate(op, a, b):
    """Helper: Calculate any operation"""
    if op == '+': return a + b
    if op == '-': return a - b  
    if op == '*': return a * b
    if op == '/':
        if b == 0: return "Error: Divide by zero!"
        return a / b
    return "Invalid operator"

# Interactive calculator
while True:
    print("\n=== Calculator Helper ===")
    num1 = float(input("First number: "))
    op = input("Operator (+-*/): ")
    num2 = float(input("Second number: "))
    
    result = calculate(op, num1, num2)
    print(f"{num1} {op} {num2} = {result}")
    
    again = input("Continue? (y/n): ")
    if again.lower() != 'y':
        break