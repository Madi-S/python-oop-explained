

class Student:
    def setName(self):
        self.name = 'Mark'

    def displayName(self):
        print(self.name)


s = Student()
s.setName()  # is equalent to    `s.name = 'Mark'``
s.displayName() # Mark  (will hit an Attribute Error if `seName()` method was not called before)



# Other way to do it with `__init__` - instance initializing method (executed an instance is created)


class Student2():
    def __init__(self, name):
        self.name = name

    def displayName(self):
        print(self.name)


s2 = Student('Carl')
s2.displayName()


