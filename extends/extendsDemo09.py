class Master(object):
    def __init__(self):
        self.kongfu = '[Master method]'

    def make_cake(self):
        print(f'{self.kongfu} to make cake')


class School(object):
    def __init__(self):
        self.kongfu = '[bytetube method]'

    def make_cake(self):
        print(f'{self.kongfu} to make cake')


class Prentice(School, Master):
    def __init__(self):
        self.kongfu = '[original method]'#共有属性
        self.__money = 2000000#私有属性

    # 获取私有属性
    def get_money(self):
        return self.__money

    # 修改私有属性
    def set_money(self,m):
        self.__money = m

    def __info_print(self):
        print(self.kongfu)
        print(self.__money)

    def make_cake(self):
        self.__init__()
        self.kongfu = '[original method]'


    def make_master_cake(self):
        Master.__init__(self)
        Master.make_cake(self)

    def make_school_cake(self):
        School.__init__(self)
        School.make_cake(self)


# 徒孙类
class Grand(Prentice):
    pass


# prentice = Prentice()
# prentice.set_money(10)
# print(prentice.get_money())
grand = Grand()
# 调用get_money函数获取私有属性money的值
print(grand.get_money())
# 调用set_money函数修改私有属性money的值
grand.set_money(200)
print(grand.get_money())