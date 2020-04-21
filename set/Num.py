list1 = ['a', 'b', 'c', 'd', 'e']
num_set1 = {1,2,3,4}
for i in enumerate(num_set1):
    print(i)

for index, num in enumerate(num_set1, start=5):
    print(f'下标是{index}, 对应的数字是{num}')