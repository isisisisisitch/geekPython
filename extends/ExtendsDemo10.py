
class Dog(object):
    age=10#类属性

    def __init__(self):#魔法方法/实例方法（self）只有对象才有self
        self.age = 5

    def info_print(self):#实例方法
        print(self.age)  #实例属性

    @classmethod
    def info_print(cls):#类方法
        print(cls.age)#类属性

cado = Dog()  # Dog()是创建实例对象时所调用的构造方法，内部会自动调用 __init__
print(cado.age)  # 5
print(Dog.age)  # 报错：实例属性不能通过类访问
# cado.info_print()  # 5
# Dog.info_print()