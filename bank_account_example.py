import pytz
from datetime import datetime


RED = '\033[1;31;40m'
GREEN = '\033[1;32;40m'
WHITE = '\033[1;37;40m'


class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance
        self.__history = []
        print(
            f'{RED}Bank Account initialized with name {name} with start balance {balance}')

    def deposit(self, amount):
        self.__balance += amount
        self.__history.append(
            ('+', amount, self._get_current_time()))
        print(f'{GREEN}Balance after deposit: {self.__balance}')

    def withdraw(self, amount):
        if self.__balance >= amount:
            self.__balance -= amount
            self.__history.append(
                ('-', amount, self._get_current_time()))
            print(f'{RED}Balance after withdraw: {self.__balance}')
        else:
            print(
                f'{WHITE}Error occured. Amount: {amount} > Balance: {self.__balance}')

    def show_history(self):
        for sign, amount, date in self.__history:
            colour = GREEN if sign == '+' else RED
            print(f'{colour}{sign}{amount} {WHITE}on {date.astimezone()}')

    @staticmethod
    def _get_current_time():
        return pytz.utc.localize(datetime.utcnow())


my_acc = BankAccount('John', 2436)
my_acc.deposit(2000)
my_acc.withdraw(150)
my_acc.deposit(3000)
my_acc.withdraw(3500)
my_acc.show_history()

my_acc.__balance = 10000

print(my_acc.__dict__)

'''

{'name': 'John', '_BankAccount__balance': 3786, 
'_BankAccount__history': 
[('+', 2000, datetime.datetime(2020, 12, 6, 8, 8, 29, 880939, tzinfo=<UTC>)),
('-', 150, datetime.datetime(2020, 12, 6, 8, 8, 29, 880939, tzinfo=<UTC>)), 
('+', 3000, datetime.datetime(2020, 12, 6, 8, 8, 29, 881939, tzinfo=<UTC>)), 
('-', 3500, datetime.datetime(2020, 12, 6, 8, 8, 29, 881939, tzinfo=<UTC>))],
'__balance': 10000}

'''
