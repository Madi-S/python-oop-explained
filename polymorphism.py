

class DebitCard:
    money = '10000$'

    def __add__(self, value):
        if not isinstance(value, int):
            raise TypeError('Specify money amount as integer')
        self.money = str(int(self.money[:-1]) + value) + '$'

    def __str__(self):
        return f'You debit card has {self.money}'

    def __eq__(self, c):
        if not isinstance(c, DebitCard):
            raise TypeError('Pass only DebitCard instance')
        if int(self.money[:-1]) == int(c.money[:-1]):
            return 'They are equal', True
        return 'They are not  equal', False


c1 = DebitCard()
c2 = DebitCard()

# c1 + '10000'      # TypeError: Specify money amount as integer
c1 + 10000
print(c1.money)     # 20000$
print(c1)           # You debit card has 20000$

print(c2 == c1)     # ('They are not  equal', False)
