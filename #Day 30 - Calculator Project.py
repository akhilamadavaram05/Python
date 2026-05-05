#Day 30 - Calculator Project
class Calculator:
    def __init__(self):
        self.history = []
    
    def add(self, a, b):
        result = a + b
        self.history.append(f"{a}+{b}={result}")
        return result
    
    def subtract(self, a, b):
        result = a - b
        self.history.append(f"{a}-{b}={result}")
        return result
    
    def show_history(self):
        for op in self.history:
            print(op)

calc = Calculator()
print("5+3 =", calc.add(5, 3))
print("10-4 =", calc.subtract(10, 4))
print("History:")
calc.show_history()