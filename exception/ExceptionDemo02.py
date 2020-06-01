try:

    f = open('test1.txt', 'r')
    print(1 / 0)

except (NameError, ZeroDivisionError,FileNotFoundError):
    print('有错误')