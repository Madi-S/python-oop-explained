

class Validator:
    def __set_name__(self, class_owner, property_name):
        print(f'Self: {self}\nOwner: {class_owner}\nProp name: {property_name}')
        self.property_name = property_name

    def __set__(self, instance, value):
        if not isinstance(value, str):
            raise ValueError(
                f'`{self.property_name}` must be `string`. However `{type(value).__name__}` was given')
        key = f'_{self.property_name}'
        setattr(instance, key, value)
        # instance.__dict__[self.propert_name] = value

    def __get__(self, instance, class_owner):
        if instance is None:
            return self
        key = f'_{self.property_name}'
        return getattr(instance, key, None)
        # return instance.__dict__.get(self.property_name)

class Person:
    name = Validator()
    login = Validator()

# After defining name in class Person:
# Self: <__main__.Validator object at 0x0337F070>
# Owner: <class '__main__.Person'>
# Prop name: name


p = Person()
p.name = 'Maximilian'

# p.name = 302  # ValueError: `name` must be `string`. However `int` was given

print(p.__dict__)   # {'_name': 'Maximilian'}
