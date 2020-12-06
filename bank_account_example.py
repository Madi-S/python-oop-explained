import pytz
from datetime import datetime


WHITE = '\033[1;37;40m'
GREEN = '\033[1;32;40m'
RED = '\033[1;31;40m'


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

    def showHistory(self):
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
my_acc.showHistory()
