# 4.list=[[3,1],2,3,[2,4],5,1] sublist len = 2
#
# list=[1,1,2,3,4,4,51]


list1=[[2,1],2,3,[2,4],5,1]
for i in range(len(list1)):
    if type(list1[i])==list:
        list2=list1.pop(i)
        for j in range(list2[0]):
            list1.insert(i,list2[1])
print(list1)

# list1=[[2,1],2,3,[2,4],5,1]
# for i in range(len(list1)):
#     if type(list1[i])==list:
#         list2=list1.pop(i)
#         for j in range(len(list2)):
#             list1.insert(i,list2[1])
# print(list1)