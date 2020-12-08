

class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname


class Student(Person):
    def __init__(self, name, surname, student_id):
        super().__init__(name, surname)
        self.student_id = student_id


class Employee(Person):
    def __init__(self, name, surname, emp_id):
        super().__init__(name, surname)
        self.emp_id = emp_id

# s = Student()

# Super can overwrite self values.
# To avoid super().__init__() must be called first:


class Somebody(Person):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.name = name + surname


class Feature1:
    def say(self):
        print(f'Bound with {self}')


class Feature2(Feature1):
    def say(self):
        print('Feature2')
        super().say()


f = Feature2()
f.say()
# Feature2
# Bound with <__main__.Feature2 object at 0x0303F220> - this id is Feature2's instance id in spite of Parent method was called
