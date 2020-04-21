# 9.list = [1,1]  n = 5  list = [1,1,2,3,5,8]

list=[1,1]
num=int(input('how many times you wanna repeat???'))
for i in range(num-1):#num-1  相加的次数
    list.append(list[i]+list[i+1])
print(list)