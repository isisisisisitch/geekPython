import random


# 1.1.1 产生一个随机数list（len=10）
#
# 1.2 不能用min
list=[]
bound = 100
min= bound
for i in range(11):
    list.append(random.randint(0,bound))#bound=100
    if min>list[i]:
        min=list[i]
print(list)
print(min)