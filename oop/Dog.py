class Dog():
    def __init__(self,weight,age):

        self.weight = weight
        self.age = age

    def __str__(self):#当实现了__str__方法后，再调用print()打印对象的时候，将会按照__str__方法实现的逻辑进行print
        return f'Dog weight is {self.weight} Dog age is {self.age}'

    def __del__(self):
        print(f'{self}对象已经被删除')

cado = Dog(50,2)
print(cado)#<__main__.Dog object at 0x10ad887b8> Dog weight is 50 Dog age is 2
