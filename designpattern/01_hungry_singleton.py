#hungry singleton
#self:instance obj
# cls:class obj
#hs:借助类对象的属性是共享的，唯一的
class Singleton(object):

    def __new__(cls):
        if  not hasattr(cls,'instance'):
            cls.instance = super(Singleton,cls).__new__(cls)


        return cls.instance




s1 = Singleton()
#first obj <__main__.Singleton object at 0x10a945b38>
print("first obj",s1)

s2 = Singleton()
#second obj <__main__.Singleton object at 0x10a945b38>
print("second obj",s2)