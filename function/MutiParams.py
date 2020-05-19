# def user_info(*args):
#     print(args)
#
#
# # ('TOM',)
# user_info('TOM')
# # ('TOM', 18)
# user_info('TOM', 18)
#
# def add(*args):
#     sum = 0
#     for i in range(len(args)):
#         sum+=args[i]
#
#     return sum
#
#
# sum = add(1,2,3,4)
# print(sum)



def user_info(**kwargs):
    print(kwargs)


# {'name': 'TOM', 'age': 18, 'id': 110}
user_info(name='TOM', age=18, id=110)