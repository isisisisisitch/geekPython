# list=[7,2,8,4,9,6]
# for i in range (list):
#
list=[7,2,8,4,9,6]
def Bubblesort(list):
    for i in range(len(list)-1,0,-1):
        for j in range(i):
            if list[j]>list[j+1]:
                num=list[j]
                list[j]=list[j+1]
                list[j+1]=num
    return list

# print(Bubblesort(list))


def Insertsort(list):
    for i in range(1,len(list)):
        for j in range(i,0,-1):
            if list[j-1]>list[j]:
                list[j],list[j-1]=list[j-1],list[j]
    return list
# print(Insertsort(list))


def selectsort(list):
    for i in range(len(list)):
        minIndex=i
        for j in range(i+1,len(list)):
            if list[j]<list[minIndex]:
               minIndex=j
        list[i],list[minIndex]=list[minIndex],list[i]
    return list
print(selectsort(list))
