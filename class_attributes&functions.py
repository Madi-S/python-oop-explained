

class Car:
    colour = 'grey'


# ready-only dictionary (values cannot be change/added/removed)
print(Car.__dict__)
# {'__module__': '__main__', 'colour': 'grey', '__dict__': <attribute '__dict__' of 'Car' objects>, '__weakref__': <attribute '__weakref__' of 'Car' objects>, '__doc__': None}
print(Car.__dict__['colour'])
print(Car.colour)

# Car.__dict__['colour'] = 'black'
# TypeError: 'mappingproxy' object does not support item assignment

Car.price = 20000    # Assign class attributes
print(Car.__dict__)  # 'price': 20000 - a new one

setattr(Car, 'speed', '50 km/h')
print(getattr(Car, 'speed'))  # 50 km/h
delattr(Car, 'colour')
# print(getattr(Car, 'colour')) # AttributeError: type object 'Car' has no attribute 'colour'


class Employee:
    name = 'John'

    def work():
        print('Working')


Employee.work()             # Working
print(Employee.__dict__)    # 'work': <function Employee.work at 0x02DB9D18>
