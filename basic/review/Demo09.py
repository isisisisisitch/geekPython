#获得用户的输入--->int--->奇偶数的判断
if __name__ == '__main__':

    age = int(input('plz input your age：'))
    if age < 18:
        print(f'your age is {age},illegal')
    elif (age >= 18) and (age <= 60):
        print(f'your age is {age},legal')
    else:
        print(f'your age is {age},retied')