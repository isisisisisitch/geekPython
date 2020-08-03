#proxy

from abc import ABC,abstractmethod

class Payment(ABC):

    @abstractmethod
    def make_payment(self):
        pass


#real obj
class Bank(Payment):
    def __init__(self):
        self.account = None
        self.card = None


    def has_funds(self):
        return True



    def get_account(self):
        self.account = self.card
        return  self.account

    def make_payment(self):
        if self.has_funds():
            print("payed")
        else:
            print("rejected")


    def set_card(self,num):
        print("debit card no. "+ num+ " accepted")


#proxy

class Debit_card(Payment):

    def __init__(self):
        self.bank = Bank()

    def make_payment(self):
        num = input("enter your debit card #:")
        self.bank.set_card(num)
        self.bank.make_payment()


class Client:

    def  __init__(self):
        print("buy stuff")
        self.debit_card = Debit_card()

    def buy(self):
        self.debit_card.make_payment()



client = Client()
client.buy()



