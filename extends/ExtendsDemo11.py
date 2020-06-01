#不管是类属性还是实例属性，当被定义为私有时，外界都不能直接访问，
# 如果外界需要方法，类中必须提供相应的方法支持调用
class Dog(object):
    __tooth = 10#私有类属性

    @classmethod
    def get_tooth(cls):#普通类方法
        return cls.__tooth


cado = Dog()
result = cado.get_tooth()
print(result)  # 10