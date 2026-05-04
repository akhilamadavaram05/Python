#Day 29 - Test
class Parent:
    def hello(self):
        return "parent"

class Child(Parent):
    def hello(self):
        return "child"

c = Child()
print("child" in c.hello())
print("Day 29 test ok")