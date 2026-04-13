#Day 9 - List Loops
numbers = [1, 2, 3, 4, 5]
evens = []

for num in numbers:
    if num % 2 == 0:
        evens.append(num)

print("Evens:", evens)