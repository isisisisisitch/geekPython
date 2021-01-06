num_list = [3,5,6,0,1,2]
#res_list[]
#假设min=3 min=0
#num_list = [3,5,6,1,2]
num_length = len(num_list) - 1
while num_length > 0:#只有存在可比较的数

    for j in range(num_length):
        if num_list[j] > num_list[j+1]:
            temp = num_list[j]
            num_list[j] = num_list[j+1]
            num_list[j+1] = temp

    num_length-=1#1已经排好序的数


print(num_list)

#bubble sort model:排队
def bubble_sort(num_list):

    num_length = len(num_list - 1)
    while num_length < 0:
        for j in range(num_length):
            if num_list[j] > num_list[j+1]:
                num = num_list[j]
                num_list[j] = num_list[j+1]
                num_list[j+1] = num
        num_length -= 1
    return num_list