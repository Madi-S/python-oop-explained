import sys
import ctypes
from time import time_ns


class Epoch:
    def __get__(self, instance, class_owner):
        #print(f'Self: {self}\nInstance: {instance}\nOwner: {class_owner}')
        print(f'Self id: {id(self)}')
        if instance is None:
            return self
        return int(time_ns())

    def __set__(self, instance, value):
        pass


class MyTime:
    epoch = Epoch()


m = MyTime()

print(m.epoch)
# Self: <__main__.Epoch object at 0x0113E610>
# Instance: <__main__.MyTime object at 0x0339F070>
# Owner: <class '__main__.MyTime'>

print(MyTime.epoch)  # No instance here (None)
# Self: <__main__.Epoch object at 0x0113E610>
# Instance: None
# Owner: <class '__main__.Mytime'>


class IntDescriptor:
    def __init__(self):
        self._values = {}

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


v1 = Vector()
v2 = Vector()

# v1.x = 10
# v2.x = 30
#
# print(v1.x, v2.x)   # 30 30 (Both instances share with each other)

v1.x = 103
v2.x = 403

print(v1.x, v2.x)     # 103 403 (Now they are different)
print(Vector.x._values)
# {<__main__.Vector object at 0x0351F148>: 103, <__main__.Vector object at 0x0351F190>: 403}


val = 'JohnSon'

print(sys.getrefcount(val))


def ref_count(obj_id):
    return ctypes.c_long.from_address(obj_id).value


print(ref_count(id(val)))
