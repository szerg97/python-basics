class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print("Hello, my name is", self.name, ", I am ", self.age, "old.")


p1 = Person("John", 41)
print(p1.name)
print(p1.age)
p1.introduce()
