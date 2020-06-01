#实例对象可以调用公有类属性以及类方法和公有实例属性以及实例方法
class Dog(object):
    tooth = 10#类属性

    @classmethod
    def get_tooth(cls):#普通类方法
        return cls.tooth


cado = Dog()
print(cado.tooth)
result = cado.get_tooth()
print(result)