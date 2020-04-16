num_list = [3, 5, 6, 0, 1, 2]
for i in range(len(num_list)):
    minIndex = i

    for j in range(i + 1, len(num_list)):
        if (num_list[j] < num_list[minIndex]):
            minIndex = j

    temp = num_list[i]
    num_list[i] = num_list[minIndex]
    num_list[minIndex] = temp

print(num_list)