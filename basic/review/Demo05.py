#获得用户输入，用户输入的值是#则退出，否则让用户重新输入

if __name__ == '__main__':

    ans = input('type something: ')
    if ans == "#":
        print("exit")
    else:
        print('try again')