#获得用户的输入--->int--->奇偶数的判断
if __name__ == '__main__':

    def oe_judge(num):
        if num.isnumeric():
            num = int(num)
            if num % 2 == 0:
                return "even"
            else:
                return "odd"
        return "invalid input"


    print(oe_judge("10"))