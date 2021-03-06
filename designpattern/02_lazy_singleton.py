#lazy singleton

class Singleton(object):
    #class attribute
    __instance = None

    def __init__(self):
        if not Singleton.__instance:
            print("__init__ method called")
        else:
            print("instance obj already exist!",self.get_instacne())


    @classmethod
    def get_instacne(cls):

        if not  cls.__instance:
            cls.__instance = Singleton()

        return cls.__instance



s1 = Singleton()

print("first obj created",s1.get_instacne() )

s2 = Singleton()
print("second obj created",s2.get_instacne() )