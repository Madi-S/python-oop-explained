

# class `ClassName`

class Car:
    speed = '30 km/h'


print(Car.speed)             # 30 km/h
print(Car.__name__)          # Car
print(dir(Car))              # Carr attributes
print(Car.__class__)         # <class 'type'>

c = Car()
print(c.__class__)           # <class '__main__.Car'>
print(type(c))               # <class '__main__.Car'>
print(c.__class__.__name__)  # Car

c2 = type(c)()               # the same as `c2 = Car()`
print(c2)                    # <__main__.Car object at 0x02A6E490>
print(c2.speed)              # 30 km/h
print(id(c) == id(c2))       # False
