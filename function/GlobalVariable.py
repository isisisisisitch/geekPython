# # 定义全局变量a
# # a = 100
# #
# #
# # def testA():
# #     a = 10#就近原则 如果局部变量和全局变量同名时，会发生就近现象
# #     print(a)  # 访问全局变量a，并打印变量a存储的数据
# #
# #
# # def testB():
# #     print(a)  # 访问全局变量a，并打印变量a存储的数据
# #
# #
# # testA()  # 10(3)
# # testB()  # 100(2) none

a = 100


def testA():
    print(a)


def testB():
    # global 关键字声明a是全局变量
    global a
    a = 200
    print(a)


testA()  #
testB()  #

print(f'全局变量a = {a}')  # 全局变量a = 200