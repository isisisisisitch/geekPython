#break:当满足条件时，直接跳出离它最近的一层循环
#continue：当满足条件时，跳出本次循环，然后会继续执行之后循环
sum = 0
num=1#初始条件
while num<=4:#判断条件
    if num==3:
        num += 1
        break
    sum = sum+num

    num+=1#while的步进


print(sum)