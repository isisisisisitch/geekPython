# 10.list=[1,2,3,4,5,6,7]
#
# Random = 3<len(list)list中 每3个数相加
#
# list=[6,15,7]


import random

list = [1, 2, 3, 4, 5, 6, 7]
randnum = random.randint(1, len(list))
print(randnum)
i = 0
if randnum % 2 == 0:
    while i < int((len(list) / randnum) + 1):
        list1 = list[i:i + randnum]
        num = 0
        if len(list1) < randnum:
            break
        for j in list1:
            num += j
            list.remove(j)
        print(num)
        list.insert(i, num)
        i += 1
else:
    while i < (len(list) / randnum):
        list1 = list[i:i + randnum]
        num = 0
        if len(list1) < randnum:
            break
        for j in list1:
            num += j
            list.remove(j)
        list.insert(i, num)
        i += 1
print(list)
