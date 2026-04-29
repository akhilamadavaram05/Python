#Day 25 - File Handling
with open("data.txt", "w") as f:
    f.write("Hello Python!\n")

with open("data.txt", "r") as f:
    content = f.read()
    print(content)