# 3.交换list当中index=n和index=n+1
#
# list = [0,1,2,3,4,5]
#
# list=[1,0,3,2,5,4]

list=[0,1,2,3,4,5,6]
i=0
while i<len(list)-1:
    # num=list[i]
    # list[i]=list[i+1]
    # list[i+1]=num
    list[i],list[i+1] = list[i+1], list[i]
    i+=2
print(list)

# list=[0,1,2,3,4,5,6]
# for i in range(0,len(list)-1,2):
#     temp=list[i]
#     list[i]=list[i+1]
#     list[i+1]=temp
# print(list)