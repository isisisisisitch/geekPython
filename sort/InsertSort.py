num_list = [3, 5, 6, 0, 1, 2]
for i in range(1,len(num_list)):
    for j in range (i,0,-1):
        if num_list[j]<num_list[j-1]:
            num_list[j],num_list[j-1] = num_list[j-1],num_list[j]

print(num_list)