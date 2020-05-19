# def return_num():
#     return 100, 200
#
#
# num1, num2 = return_num()#100, 200
# print(num1)  # 100
# print(num2)  # 200


dict1 = {'name': 'TOM', 'age': 18,'gender': 'M'}
a, b ,c= dict1

# 对字典进行拆包，取出来的是字典的key
print(a)  # name
print(b)  # age

print(dict1[a])  # TOM
print(dict1[b])  # 18