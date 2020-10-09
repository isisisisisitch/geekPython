# name = "abcdefg"
# #序列[开始位置下标:结束位置下标:步长]
# print(name[2:5:1])  # cde
# print(name[2:5])  # cde
# print(name[:5])  # abcde
# print(name[1:])  # bcdefg
# print(name[:])  # abcdefg
# print(name[::2])  # aceg
# print(name[:-1])  # abcdef, 负1表示倒数第一个数据
# print(name[-4:-1])  # def
# print(name[::-1])  # gfedcba

def remove_kIndex_from_str(str,index):

    left_part = str[0:index]
    right_part = str[index+1:]
    return left_part + right_part


print(remove_kIndex_from_str("bytetube",2))