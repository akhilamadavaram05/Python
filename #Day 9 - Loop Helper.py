#Day 9 - Loop Helper
def get_evens(numbers):
    result = []
    for n in numbers:
        if n % 2 == 0:
            result.append(n)
    return result

print("Evens:", get_evens([1, 2, 3, 4, 5]))