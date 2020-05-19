# 当定义类之后，想使用类中的成员方法，我们需要先创建类对象
class Person():
    def sleep(self):
        s = 10
        print("person can sleep")
        print(self)#<__main__.Person object at 0x102372160>


jim = Person()
jim.sleep()
print(jim)#<__main__.Person object at 0x102372160>

