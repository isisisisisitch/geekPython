# 1~100 Sum even nums
# while
# 1.初始表达式 i
# 2.while 条件
# 3.循环体
# 4.步进表达式

if __name__ == '__main__':
    def reverse_tri(bound):
        for i in range(bound, 0, -1):
            for j in range(i - 1):
                print(" ", end=" ")
            for n in range(i - 1, bound):
                print("*", end="   ")
            print()


    reverse_tri(7)