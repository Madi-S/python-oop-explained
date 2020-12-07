

class God:
    def say(self):
        print('I am God')


class Mother(God):
    def say(self):
        print('I am Mother')


class Father(God):
    def say(self):
        print('I am Father')


class Kid(Father, Mother):
    pass


k = Kid()
k.say()     # 'I am Father' (obeys mro() - Method Resolution Order)

# Because `Father` was specifed first (most left class will be dominant)
# Thus, the order plays a significant role in inheritance
# It goes from left -> right

print(k.__class__.mro())  # Ther order python will use to find `say` method:
# -> [<class '__main__.Kid'>, <class '__main__.Father'>, <class '__main__.Mother'>, <class '__main__.God'>, <class 'object'>]


class NameMixin:
    name = 'Not Specified'

    def show_name(self):
        if self.name == 'Not Specified':
            raise ValueError('Name must be specified')
        print(f'My name is {self.name}')


class Employee(NameMixin):
    def __init__(self, name):
        self.name = name


e = Employee('Maximilian')
e.show_name()    # My name is Maximilian
