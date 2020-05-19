import random


# 1.1.1 产生一个随机数list（len=10）
#
# 1.2 不能用min
# list=[]
# bound = 100
# min= bound
# for i in range(11):
#     list.append(random.randint(0,bound))#bound=100
#     if min>list[i]:
#         min=list[i]
# print(list)
# print(min)

#generateRandList
def generateRandList(size,bound):
    """ this method is to generate a random list
    size:it's the cap of list
    bound:random num's range
    """
    list = []
    for i in range(size):
        list.append(random.randint(0, bound))

    return list


def getMin(list):
    min= 999999
    for i in range(len(list)):
        if min > list[i]:
            min = list[i]

    return min

list=generateRandList(11,100)
print(list)

min = getMin(list)
print(min)

help(generateRandList)