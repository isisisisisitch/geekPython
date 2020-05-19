#python支持对类属性进行外部添加和获取
class Washer():
    def __init__(self,width,height):
        self.width = width
        self.height = height


washer = Washer(10, 100)  # 由于我们实现了__init__方法，这个方法在对象创建的时候，被自动被解析器调用：初始化类对象的
print(f'washer width is {washer.width}')
print(f'washer width is {washer.height}')
print(washer)#<__main__.Washer object at 0x10e7ab160>




#     def __init__(self):
#         self.width = 500
#         self.height = 800
#
#
# washer = Washer(10,100)#由于我们实现了__init__方法，这个方法在对象创建的时候，被自动被解析器调用：初始化类对象的
# print(f'washer width is {washer.width}')
# print(f'washer width is {washer.height}')


#     def wash(self):
#         print("wash clothes")
#         print(self.width)
#
#         print(self.height)
#
#
#
# washer = Washer()
# washer.width = 200
# washer.height = 1000
# washer.wash()
#
#
#
# print(f'washer width is {washer.width}')
# print(f'washer width is {washer.height}')