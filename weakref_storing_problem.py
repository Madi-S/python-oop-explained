import weakref


class Person:
    pass


p = Person()
w = weakref.ref(p)

print(w)
