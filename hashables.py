import hashlib


# Only hashable objects can be keys in a dictionary

a = hashlib.md5('Edick'.encode('utf-8')).hexdigest()
print(a)    # 4be6dd3060a60021754651c76bf07347

# With extra space:
b = hashlib.md5('Edick '.encode('utf-8')).hexdigest()
print(b)    # 89cde7cd37585fbf5e00136d5434a4d0

print(hash(1), hash('1'))   # 1 -1486506413


class Student:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    def __hash__(self):
        return hash(self.name)

    def __eq__(self, student_obj):
        return isinstance(student_obj, Student) and self.name == student_obj.name

    # Now Student object is hashable and can be a key in a dictionary


s1 = Student('Jack')
s2 = Student('Jack')
s3 = Student('Mary')

print(s1 == s2)  # True
print(s1 == s3)  # False

print(hash(s1) == hash(s2))  # True

d = {s1: 'Johnson'}
print(d.get(s2))    # Johnson
