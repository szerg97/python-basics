class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)


class Student(Person):
    pass


stud = Student('Bianka', 'Horvath')
print('The student is', stud.firstname, stud.lastname)
