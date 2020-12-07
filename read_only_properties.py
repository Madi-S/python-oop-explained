

class House:
    def __init__(self, price):
        self._price = price

    @property
    def price(self):
        print('From property getter')
        return self._price


h = House(10009)
print(h.price)
# h.price = 10000 will raise AttributeError: can't set attribute


class Person:
    def __init__(self, first_name, second_name):
        self._first_name = first_name
        self._second_name = second_name
        self._full_name = None

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        self._first_name = value
        self._full_name = None

    @property
    def second_name(self):
        return self._second_name

    @second_name.setter
    def second_name(self, value):
        self._second_name = value
        self._full_name = None

    @property
    def full_name(self):
        if self._full_name is None:
            self._full_name = self._first_name + ' ' + self._second_name
        return self._full_name


p = Person('Sam', 'Serious')
print(p.full_name)              # Sam Serious
p.second_name = 'Pussy'
print(p.full_name)              # Sam Pussy
