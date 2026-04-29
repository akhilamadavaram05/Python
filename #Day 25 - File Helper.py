#Day 25 - File Helper
with open("numbers.txt", "w") as f:
    f.write("1\n2\n3\n")

with open("numbers.txt", "r") as f:
    lines = f.readlines()
    print("Lines:", len(lines))