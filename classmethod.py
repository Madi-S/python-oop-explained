

class Student:

    def __init__(self, name):
        self.name = name

    @classmethod
    def from_file(cls, file_path):
        with open(file_path) as f:
            name = f.read().strip()
        return cls(name=name)

    @classmethod
    def from_obj(cls, obj):
        if hasattr(obj, 'name'):
            name = getattr(obj, 'name')
            return cls(name=name)
        return cls



class Name:
    name = 'John'

s = Student('Max')
print(s.name)       # Max

s = Student.from_obj(Name)
print(s.name)       # John

s = Student.from_file('name.txt')
print(s.name)       # Nick
