

class Person:
    name = 'Peter'


print(Person.__dict__)

p1 = Person()
p2 = Person()

print(id(p1), id(p2))           # 52094480 52094096
print(p1.name, p2.name)         # Peter Peter
print(id(p1.name), id(p2.name)) # 27980928 27980928 - the same object is called

print(p1.__dict__, p2.__dict__)  # {} {}

# Class attributes - create defaults for instances
# Thus, each instance is created with an eye to create unique attributes

p1.name = 'Max'
p2.name = 'John'
p2.age = 21

print(p1.__dict__, p2.__dict__)  # {'name': 'Max'} {'name': 'John', 'age': 21}
print(Person.__dict__)
# {'__module__': '__main__', 'name': 'Peter', '__dict__': <attribute '__dict__' of 'Person' objects>, '__weakref__': <attribute '__weakref__' of 'Person' objects>, '__doc__': None}

# Firstly, classes are callable objects - an instance is received
# Instances are not intertwined with each other
# If instance has no attributes it will them in Class