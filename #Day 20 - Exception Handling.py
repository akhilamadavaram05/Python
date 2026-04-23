#Day 20 - Exception Handling
try:
    num = int(input("Enter number: "))
    print("Double:", num * 2)
except ValueError:
    print("Not a number!")