# 3 + 2 + 1
def sum_numbers(num):
    # 1.如果是1，直接返回1 -- 出口
    if num == 1:
        return 1
    # 2.如果不是1，重复执行累加并返回结果
    return num + sum_numbers(num-1)


sum_result = sum_numbers(3)
# 输出结果为6
print(sum_result)
