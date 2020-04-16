#一个小球从10米的高空落下，每次落地跳回原来的一半，再落下，求第10次时准备下降时，一共途径了多少路程
i = 1#i表示下降次数
height = 10
sum = 0
while i<10:
    sum+=height
    height/=2
    sum += height
    i+=1

print(sum)

