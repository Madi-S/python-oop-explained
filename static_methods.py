# `@staticmethod` decorator


class Telephone:
    def sayHello(self):
        print('Hello')

    @staticmethod
    def sayBye():
        print('Bye Bye')


# What if we do not need to get data of an instance? (when `self` parameter is not mandatory)
# Then staticmethod is gonna be used, which does not take `self` parameter

t1 = Telephone()
t1.sayBye()      # No error with `@staticmethod`

# Using `@staticmethod` reduces load/memory usage

t2 = Telephone()
# False, their ids differ from each other (multiple methods used to perform a single task)
print(id(t1.sayHello) == id(t2.sayHello))
# True, identical ids, thus, method is the same and we do not overload memory with useless stuff (when using lots of intances)
print(id(t1.sayBye) == id(t2.sayBye))

print(type(t1.sayBye))
# Also, note that `@staticmethod` is a function  - <class 'function'>