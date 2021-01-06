num_list = [3, 5, 6, 0, 1, 2]
for i in range(len(num_list)):
    minIndex = i

    for j in range(i + 1, len(num_list)):
        if (num_list[j] < num_list[minIndex]):
            minIndex = j

    temp = num_list[i]
    num_list[i] = num_list[minIndex]
    num_list[minIndex] = temp

# print(num_list)

def selection_sort(array):

    length = len(array)

    for cur in range(length):
        min_index = cur
        for j in range(cur + 1, length):
            if array[min_index] > array[j]:
                min_index = j

        array[min_index], array[cur] = array[cur], array[min_index]


selection_sort(num_list)
print(num_list)
