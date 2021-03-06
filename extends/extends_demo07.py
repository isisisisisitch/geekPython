#子类调用父类的方法:super()
#子类使用父类的方法:实现子类自己的逻辑
class Master(object):
    def __init__(self):
        self.kongfu = '[Master method]'

    def make_cake(self):
        print(f'{self.kongfu} to make cake')


class School(Master):
    def __init__(self):
        self.kongfu = '[bytetube method]'

    def make_cake(self):
        print(f'{self.kongfu} to make cake')

        # 方法2.1
        # super(School, self).__init__()
        # super(School, self).make_cake()

        # 方法2.2
        # super().__init__()
        # super().make_cake()


class Prentice(School,Master):
    def __init__(self):
        self.kongfu = '[original method]'

    def make_cake(self):
        self.__init__()
        print(f'{self.kongfu} to make cake')
       # super().__init__()
        super().make_cake()


prentice = Prentice()

prentice.make_cake()
    # 子类调用父类的同名方法和属性：把父类的同名属性和方法再次封装
    # def make_master_cake(self):
    #     Master.__init__(self)
    #     Master.make_cake(self)
    #
    # def make_school_cake(self):
    #     School.__init__(self)
    #     School.make_cake(self)

    # 一次性调用父类的同名属性和方法
    # def make_old_cake(self):
        # 方法一：代码冗余；父类类名如果变化，这里代码需要频繁修改
        # Master.__init__(self)
        # Master.make_cake(self)
        # School.__init__(self)
        # School.make_cake(self)

        # 方法二: super()
        # 方法2.1 super(当前类名, self).函数()
        # super(Prentice, self).__init__()
        # super(Prentice, self).make_cake()

        # 方法2.2 super().函数()



