#Day 25 - Test
with open("test.txt", "w") as f:
    f.write("test")
with open("test.txt", "r") as f:
    data = f.read()
print("test" in data)
print("Day 25 test ok")