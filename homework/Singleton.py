# # class Instance(object):
# #     def __new__(cls):
# #         if not hasattr(cls,"instance"):
# #             cls.instance=super(Instance,cls).__new__(cls)
# #         return cls.instance
# #
# # instance1=Instance()
# # print("first example:",instance1)
# #
# # instance2=Instance()
# # print("second example:",instance2)
#
# # class Instance(object):
# #     __instance=None
# #     def __init__(self):
# #         if not Instance.__instance:
# #             print("method called")
# #         else:
# #             print("instance is already exist", self.get_instance())
# #
# #     @classmethod
# #     def get_instance(cls):
# #         if not cls.__instance:
# #             cls.__instance=Instance()
# #         return cls.__instance
# #
# # instance1=Instance()
# # print("created seconde object",instance1)
# # print("created first object",Instance.get_instance())
# # instance2=Instance()
# # print("created seconde object",instance2)
#
# from abc import ABC,abstractmethod
#
# class factory(object):
#     def get_toy_sales(self,toys):
#         return toys.sales()
#
# class Toys(ABC):
#     @abstractmethod
#     def sales(self):
#         pass
#
# class robot:
#     def sales(self):
#         return "sell robot"
#
# class ball:
#     def sales(self):
#         return "sell ball"
#
# fac=factory()
# rob=robot()
# bal=ball()
# print(fac.get_toy_sales(rob))
# print(fac.get_toy_sales(bal))
from abc import ABC ,abstractmethod
class Bank():
    def __init__(self):
        self.card = None

    def fund(self):
        return True

    def account(self):
         self.account=self.card
         return self.account
    def payment(self):
        if self.fund():
            print("have money")
        else:
            print("no money")


class Pelple():
    def __init__(self):
        print("buy")




class Debit_card(Bank):



     def pay(self,card):
         number=input("card number")
         self.card
