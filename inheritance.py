

class Telephone:
    number = '01124356'

    def hello(self):
        print('Hello?')


class Smartphone(Telephone):
    pass


s = Smartphone()
print(dir(s))       # 'hello', 'number' in it

print(s.number)     # 01124356
s.hello()           # Hello?

print(s.__dict__)   # {}

print(Telephone.__dict__)
# 'number': '01124356', 'hello': <function Telephone.hello at 0x036E8D18>

# Firstly, python searches for 'number' in instance environment.
# Then, after it found nothing, it goes to class environment to look for 'number' and 'hello()'.
# None, then it goes to the parent class. It found 'number' and 'hello()' in here.

print(dir(object))

# All created classes implicitly inherit from 'object' class.


# Another example of inheritance

class Enemy:
    colour = 'red'
    dieable = True


class Soldier(Enemy):
    health = 125
    damage = 16


class Tiger(Enemy):
    health = 85
    damage = 31


s = Soldier()
t = Tiger()

print(isinstance(s, Enemy))     # True
print(isinstance(t, Enemy))     # True

print(type(s))                  # <class '__main__.Soldier'>
print(type(t))                  # <class '__main__.Tiger'>

print(isinstance(s, type(t)))   # False

# Nested inheritence


class Grandfather:
    pass


class Father(Grandfather):
    pass


class Son(Father):
    pass


s = Son()

print(isinstance(s, Son), isinstance(s, Father), isinstance(s, Grandfather))
# True True True

print(issubclass(Son, Father), issubclass(Father, Grandfather))
# True True


# Overload
class NPC:
    health = 320

    def greet(self):
        print('Greetings!')


class NPC_2(NPC):
    def greet(self):
        print('Howdy!')


n = NPC_2()
n.greet()       # Howdy!

print(NPC_2.__dict__['greet'])  # <function NPC_2.greet at 0x012C8A48>


# Another example


class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f'Hello from {self.name}')


class Student(Person):
    pass


s = Student('Peter')
s.greet()           # Hello from Peter (Person instance goes to greet's self)

