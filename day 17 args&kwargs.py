#Day 17 - *args & **kwargs
def sum_all(*args):
    return sum(args)

print(sum_all(1, 2, 3))  # 6
print(sum_all(10, 20))   # 30