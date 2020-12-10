# __get()__ __set__() or __del__() -> this is a descriptor


# class Person:
#     def __init__(self, first_name, second_name):
#         self._first_name = first_name
#         self._second_name = second_name
#         self._full_name = None
#
#     @property
#     def first_name(self):
#         return self._first_name
#
#     @first_name.setter
#     def first_name(self, value):
#         self._first_name = value
#         self._full_name = None
#
#     @property
#     def second_name(self):
#         return self._second_name
#
#     @second_name.setter
#     def second_name(self, value):
#         self._second_name = value
#         self._full_name = None

# Is reduced to:

from random import randint, choice
from time import time_ns


class StringDescriptor:
    def __init__(self, value=None):
        if value:
            self.set(value)

    def set(self, value):
        self._value = value

    def get(self):
        return self._value


class Person:
    def __init__(self, name, surname):
        self.name = StringDescriptor(name)
        self.surname = StringDescriptor(surname)


p = Person('Sam', 'Serious')

print(p.name, p.surname)
# <__main__.StringDescriptor object at 0x033FF0E8> <__main__.StringDescriptor object at 0x033FF160>
print(p.name.get())     # Sam
p.surname.set('Pussy')
print(p.surname.get())  # Pussy


class Epoch:
    def __get__(self, istance, class_owner):
        return int(time_ns())


class MyClock:
    epoch = Epoch()


m = MyClock()

for _ in range(10):
    print(m.epoch)


class Game:
    @property
    def rock_paper_scissors(self):
        return choice(['Rock', 'Paper', 'Scissors'])

    @property
    def flip_coin(self):
        return choice(['Heads', 'Tails'])

    @property
    def dice(self):
        return randint(1, 6)


g = Game()

print(g.rock_paper_scissors)
print(g.dice)
print(g.dice)
print(g.flip_coin)


class Choice:
    def __init__(self, *choices):
        self._choices = choices

    def __get__(self, obj, owner):
        return choice(self._choices)


class AnotherGame:
    dice = Choice(1, 2, 3, 4, 5, 6, 7)
    flip = Choice('Heads', 'Tails')
    rps = Choice('Rock', 'Paper', 'Scissors')

    def __get__(self, obj, owner):
        print('Here!', obj, owner)


a = AnotherGame()

print(a.dice)
print(a.flip)
