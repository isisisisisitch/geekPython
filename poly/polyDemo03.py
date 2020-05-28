#实例对象：是通过__init__创建出来
#类对象：不需要创建的，直接通过类名就可以获取到
class Dog(object):
    #age=100

    def __init__(self):#实例化对象的时候会被自动调用--->实例对象
        self.age = 5

    def info_print(self):
        print(self.age)


cado = Dog()#__init__
print(cado.age)  # 5
print(Dog.age)  # 报错：实例属性不能通过类访问
cado.info_print()  # 5