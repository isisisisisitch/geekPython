# 7.计算list中各个元素出现的次数


list=['a','b','c','a','d','c']
list2=set(list)
for i in list2:
    count=0
    for j in list:
        if j==i:
            count+=1
    print(f'there will be {count} {i} in the list')