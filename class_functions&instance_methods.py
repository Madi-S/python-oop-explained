

class Person:
    def hello():
        print('Hello')


print(Person.hello)  # <function Person.hello at 0x03719CD0>

p = Person()

print(p.hello)  # <bound method Person.hello of <__main__.Person object at 0x013ABB80>>
print(hex(id(p)))   # 0x341e610

Person.hello()
# p.hello()       # TypeError: hello() takes 0 positional arguments but 1 was given
print(type(p.hello))        # <class 'method'> in instances
print(type(Person.hello))   # <class 'function'> in class

print(dir(Person.hello))
print(dir(p.hello))         # there is `__self__`


# p.hello == Person.hello(p) - this is method

print(p.hello.__self__)  # <__main__.Person object at 0x0345E610>
print(hex(id(p)))       # 0x345e610

# <function Person.hello at 0x02FE9CD0> (to which id of p.__self__ is passed)
print(p.hello.__func__)


class Car:
    # def drive(instance):
    #     print(instance)
    def drive(self):
        print(self)


c = Car()
c.drive()   # <__main__.Car object at 0x032FE058> hex(id(c))
# instance (self) is passed to get access to instace data, attrs