

class Student:
    def __init__(self, name):
        self._name = name

    def get_name(self):
        print('From get_name()')
        return self._name

    def set_name(self, name):
        print('From set_name()')
        self._name = name

    def del_name(self):
        del self._name

    # Example 1
    # name = property(fget=get_name, fset=set_name, fdel=del_name)

    # Example 2
    # name = property()
    # name = name.getter(get_name)
    # name = name.setter(set_name)

    # Example 3
    # name = property(get_name)
    # name = name.setter(set_name)

    # Example 4
    @property
    def name(self):
        return self._name

    @name.setter
    def set_name2(self, val):
        self._name = val

    # name = name.setter(set_name)


s = Student('Andrew')

print(s.name)       # From get_name()
s.name = 'Brann'    # Andrew \n From set_name()
