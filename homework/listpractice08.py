# 8.list=[[1,2,3],[2,3,4],[3,4,5]]  8.1 list=[6,9,12] 8.2  打印出相加和最大的sublist[3,4,5]

list=[[1,2,3],[2,3,4],[3,4,5]]
max=0
for i in range(len(list)):
    new_list=list[i]
    list[i]=sum(new_list[:])
    if i==0:
        max=list[i]
    elif list[i-1]<list[i]:
        max=new_list
print(list)
print(max)