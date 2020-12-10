import weakref


class Person:
    pass


p = Person()
w = weakref.ref(p)

print(w)    # <weakref at 0x039CEDC0; to 'Person' at 0x036BE610>
print(hex(id(p)))                                  # 0x36be610

del p
print(w)    # dead reference
print(w())  # None

p2 = Person()
d = weakref.WeakKeyDictionary()
d[p2] = 33
print(d.get(p2))    # 33
# print(dir(d))

print(d.keyrefs())  # [<weakref at 0x0371B7F8; to 'Person' at 0x033FE610>]
del p2
print(d.keyrefs())  # []


class Storage:
    def __init__(self, number):
        self.pwd = oct(number)

    def __eq__(self, obj):
        return isinstance(obj, Storage) and obj.pwd == self.pwd

    def __hash__(self):
        return hash(self.pwd)


s = Storage(433)
print(hash(s))


# Then our modified example from previous tutorial:
class IntDescriptor:
    def __init__(self):
        # Modified here! from simple dict to WeakRefDictionary
        self._values = weakref.WeakKeyDictionary()

    def __set__(self, instance, value):
        self._values[instance] = value

    def __get__(self, instance, class_owner):
        if instance is None:
            print('Call from Class')
            return self

        print('Call from instance')
        return self._values.get(instance)


class Vector:
    x = IntDescriptor()
    y = IntDescriptor()


v = Vector()
print(hex(id(v)))  # 0x363fa48

v.x = 66
print(v.x)    # 66
print(Vector.x._values.keyrefs())
# [<weakref at 0x03654A78; to 'Vector' at 0x0363FA48>]
del v

print(Vector.x._values.keyrefs())[]
