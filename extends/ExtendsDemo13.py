class Dog(object):

    tooth = 10  # 类属性

    def __init__(self):  # 魔法方法/实例方法（self）只有对象才有self
        self.age = 5

    @staticmethod
    def info_print():#静态方法中，如果想获取类属性或者实例属性，通过创建类对象或者实例对象即可完成
        cado = Dog()
        a = cado.age #python是一门动态语言，没有静态变量，所以根本无法获取静态值
        return a


cado = Dog()
# 静态方法既可以使用对象访问又可以使用类访问
print(cado.info_print())
print(Dog.info_print())
