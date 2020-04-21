# 2.  2.1给定2个list 2.2从这2个list当中取出公共部分
#
# list1=[1,2,3,4]
#
# list2=[1,2,5]
#
# Com = [1,2]

list1=[1,2,3,4]
list2=[1,2,5]
com=[]
for i in range(len(list1)):
    for j in range(len(list2)):
        if list2[j]==list1[i]:
            com.append(list2[j])
print(com)