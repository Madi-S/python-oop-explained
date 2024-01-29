name = 'Ahmed'


class Person:
    name = 'Moji'

    def print_name(self):
        print(name)


p = Person()
p.print_name()  # Ahmed


x = 1


def print_x():
    x = x + 1   # UnboundLocalError: local variable 'x' referenced before assignment
    print(x)


# print_x()


class Car:
    colour = 'black'

    @classmethod
    def set_colour(cls, colour):
        cls.colour = colour


c = Car()
print(Car().colour)             # blac
c.colour = 'white'
print(Car().colour, c.colour)   # black white
c.set_colour('orange')
print(Car().colour, c.colour)   # orange white
print(Car.__dict__, c.__dict__)
'''
{'__module__': '__main__', 'colour': 'orange', 'set_colour': <classmethod object at 0x02F5E088>, '__dict__': <attribute '__dict__' of 'Car' objects>, '__weakref__': <attribute '__weakref__' of 'Car' objects>, '__doc__': None}
 {'colour': 'white'}
'''
